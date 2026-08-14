"""Bounded, dependency-free discovery source adapters."""

from __future__ import annotations

import base64
import json
import math
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Mapping

from .models import Candidate
from .normalization import is_dsh_relevant, normalize_repository_url


@dataclass(frozen=True)
class FakeResponse:
    status: int
    body: Any
    headers: Mapping[str, str] | None = None


@dataclass(frozen=True)
class HttpResponse:
    status: int
    body: bytes
    headers: Mapping[str, str]


class HttpError(Exception):
    pass


class HttpClient:
    USER_AGENT = "Oh-My-DSH-discovery/1.0"

    def __init__(self, transport: Callable[[urllib.request.Request, float], Any] | None = None, *, timeout: float = 20.0, max_retries: int = 2, max_retry_delay: float = 5.0, sleep: Callable[[float], None] = time.sleep) -> None:
        self.transport = transport or self._urlopen
        timeout = float(timeout)
        if not math.isfinite(timeout) or timeout <= 0:
            raise ValueError("timeout must be a finite positive number")
        self.timeout = timeout
        self.max_retries = max(0, int(max_retries))
        self.max_retry_delay = max(0.0, float(max_retry_delay))
        self.sleep = sleep
        self.last_attempts = 0

    def get(self, url: str, *, headers: Mapping[str, str] | None = None, max_attempts: int | None = None) -> HttpResponse:
        return self.request(url, headers=headers, max_attempts=max_attempts)

    def request(self, url: str, *, headers: Mapping[str, str] | None = None, data: bytes | None = None, max_attempts: int | None = None) -> HttpResponse:
        request_headers = {"User-Agent": self.USER_AGENT, "Accept": "application/json, application/xml, text/xml"}
        request_headers.update(headers or {})
        request = urllib.request.Request(url, data=data, headers=request_headers, method="POST" if data is not None else "GET")
        attempts = min(self.max_retries + 1, max(1, max_attempts or self.max_retries + 1))
        for attempt in range(attempts):
            self.last_attempts = attempt + 1
            try:
                response = self.transport(request, self.timeout)
                status, body, response_headers = self._unpack(response)
                if self._retryable(status, response_headers) and attempt + 1 < attempts:
                    self.sleep(self._retry_delay(response_headers, attempt))
                    continue
                if status >= 400:
                    raise HttpError(f"HTTP status {status}")
                return HttpResponse(status, body, response_headers)
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                if attempt + 1 < attempts:
                    self.sleep(min(self.max_retry_delay, float(2**attempt)))
                    continue
                raise HttpError(f"request failed: {type(exc).__name__}") from None
        raise HttpError("request failed")

    @staticmethod
    def _unpack(response: Any) -> tuple[int, bytes, Mapping[str, str]]:
        if isinstance(response, FakeResponse):
            body = response.body if isinstance(response.body, bytes) else json.dumps(response.body).encode("utf-8")
            return response.status, body, response.headers or {}
        return getattr(response, "status", response.getcode()), response.read(), dict(getattr(response, "headers", {}))

    @staticmethod
    def _retryable(status: int, headers: Mapping[str, str]) -> bool:
        if status == 429 or status >= 500:
            return True
        return status == 403 and (headers.get("Retry-After") is not None or headers.get("X-RateLimit-Remaining") == "0")

    def _retry_delay(self, headers: Mapping[str, str], attempt: int) -> float:
        try:
            retry_after = float(headers.get("Retry-After", ""))
        except ValueError:
            retry_after = 0.0
        return min(self.max_retry_delay, max(0.0, retry_after, float(2**attempt)))

    @staticmethod
    def _urlopen(request: urllib.request.Request, timeout: float) -> Any:
        return urllib.request.urlopen(request, timeout=timeout)


class SourceStatus(str, Enum):
    OK = "ok"
    ERROR = "error"
    SKIPPED = "skipped"


@dataclass(frozen=True)
class DiscoveryHit:
    candidate: Candidate
    url: str = ""
    metadata: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class SourceResult:
    source: str
    status: SourceStatus
    hits: tuple[DiscoveryHit, ...] = ()
    message: str = ""


@dataclass(frozen=True)
class SourceCredentials:
    github_token: str | None = None
    gitlab_token: str | None = None
    reddit_client_id: str | None = None
    reddit_client_secret: str | None = None


class _Source:
    name = "source"
    pages = 1
    request_budget = 1

    def __init__(self, client: HttpClient, *, pages: int | None = None, credentials: SourceCredentials | None = None) -> None:
        self.client = client
        self.pages = min(self.pages, max(0, pages if pages is not None else self.pages))
        self.credentials = credentials or SourceCredentials()
        self._attempts = 0

    def _request(self, url: str, *, headers: Mapping[str, str] | None = None, data: bytes | None = None) -> HttpResponse:
        remaining = self.request_budget - self._attempts
        if remaining <= 0:
            raise HttpError("source request budget exhausted")
        before = self.client.max_retries + 1
        allowed = min(before, remaining)
        try:
            return self.client.request(url, headers=headers, data=data, max_attempts=allowed)
        finally:
            self._attempts += self.client.last_attempts

    def _hit(self, *, name: str, description: str, url: str, metadata: Mapping[str, Any] | None = None) -> DiscoveryHit | None:
        topics = tuple((metadata or {}).get("topics", ()))
        if not is_dsh_relevant(name=name, description=description, topics=topics):
            return None
        return DiscoveryHit(Candidate(normalize_repository_url(url), name, description, self.name, dict(metadata or {})), url, metadata)

    def _error(self, exc: Exception) -> SourceResult:
        return SourceResult(self.name, SourceStatus.ERROR, message=f"{type(exc).__name__}: source response unavailable")


class GitHubSource(_Source):
    name, pages, request_budget = "github", 2, 2

    def discover(self) -> SourceResult:
        try:
            hits = []
            for page in range(self.pages):
                params = urllib.parse.urlencode({"q": "dsh OR deepseek-harness", "sort": "updated", "per_page": 30, "page": page + 1})
                headers = {"Authorization": f"Bearer {self.credentials.github_token}"} if self.credentials.github_token else {}
                for item in json.loads(self._request(f"https://api.github.com/search/repositories?{params}", headers=headers).body).get("items", []):
                    hit = self._hit(name=item.get("name", ""), description=item.get("description") or "", url=item.get("html_url", ""), metadata={"topics": item.get("topics", [])})
                    if hit: hits.append(hit)
            return SourceResult(self.name, SourceStatus.OK, tuple(hits))
        except (HttpError, ValueError, TypeError, KeyError, AttributeError) as exc: return self._error(exc)


class GitLabSource(GitHubSource):
    name = "gitlab"
    def discover(self) -> SourceResult:
        try:
            hits = []
            for page in range(self.pages):
                query = urllib.parse.urlencode({"search": "dsh", "per_page": 20, "page": page + 1})
                headers = {"PRIVATE-TOKEN": self.credentials.gitlab_token} if self.credentials.gitlab_token else {}
                for item in json.loads(self._request(f"https://gitlab.com/api/v4/projects?{query}", headers=headers).body):
                    hit = self._hit(name=item.get("name", ""), description=item.get("description") or "", url=item.get("web_url", ""))
                    if hit: hits.append(hit)
            return SourceResult(self.name, SourceStatus.OK, tuple(hits))
        except (HttpError, ValueError, TypeError, KeyError, AttributeError) as exc: return self._error(exc)


class HackerNewsSource(_Source):
    name, request_budget = "hackernews", 6
    def discover(self) -> SourceResult:
        try:
            hits = []
            for kind in ("newstories", "askstories", "showstories"):
                ids = json.loads(self._request(f"https://hacker-news.firebaseio.com/v0/{kind}.json").body)
                if ids and self._attempts < self.request_budget:
                    item = json.loads(self._request(f"https://hacker-news.firebaseio.com/v0/item/{ids[0]}.json").body)
                    hit = self._hit(name=item.get("title", ""), description=item.get("text", "") or "", url=item.get("url", f"https://news.ycombinator.com/item?id={ids[0]}"))
                    if hit: hits.append(hit)
            return SourceResult(self.name, SourceStatus.OK, tuple(hits))
        except (HttpError, ValueError, TypeError, KeyError, AttributeError) as exc: return self._error(exc)


class LobstersSource(_Source):
    name = "lobsters"
    def discover(self) -> SourceResult:
        try:
            root = ET.fromstring(self._request("https://lobste.rs/rss").body)
            hits = []
            for item in root.findall(".//item"):
                hit = self._hit(name=item.findtext("title", ""), description=item.findtext("description", ""), url=item.findtext("link", ""))
                if hit: hits.append(hit)
            return SourceResult(self.name, SourceStatus.OK, tuple(hits))
        except (HttpError, ET.ParseError, ValueError, TypeError, AttributeError) as exc: return self._error(exc)


class StackExchangeSource(GitHubSource):
    name = "stackexchange"
    def discover(self) -> SourceResult:
        try:
            hits = []
            for page in range(self.pages):
                query = urllib.parse.urlencode({"order": "desc", "sort": "activity", "intitle": "deepseek harness", "site": "stackoverflow", "pagesize": 20, "page": page + 1})
                for item in json.loads(self._request(f"https://api.stackexchange.com/2.3/search/advanced?{query}").body).get("items", []):
                    hit = self._hit(name=item.get("title", ""), description=item.get("body_markdown", "") or "", url=item.get("link", ""))
                    if hit: hits.append(hit)
            return SourceResult(self.name, SourceStatus.OK, tuple(hits))
        except (HttpError, ValueError, TypeError, KeyError, AttributeError) as exc: return self._error(exc)


class RedditSource(_Source):
    name, request_budget = "reddit", 2
    def discover(self) -> SourceResult:
        if not (self.credentials.reddit_client_id and self.credentials.reddit_client_secret):
            return SourceResult(self.name, SourceStatus.SKIPPED, message="official OAuth configuration absent")
        try:
            basic = base64.b64encode(f"{self.credentials.reddit_client_id}:{self.credentials.reddit_client_secret}".encode()).decode()
            token = json.loads(self._request("https://www.reddit.com/api/v1/access_token", headers={"Authorization": f"Basic {basic}", "Content-Type": "application/x-www-form-urlencoded"}, data=b"grant_type=client_credentials").body)["access_token"]
            payload = json.loads(self._request("https://oauth.reddit.com/search.json?q=dsh+OR+deepseek-harness&limit=25", headers={"Authorization": f"Bearer {token}"}).body)
            hits = []
            for child in payload.get("data", {}).get("children", []):
                item = child.get("data", {})
                hit = self._hit(name=item.get("title", ""), description=item.get("selftext", "") or "", url=f"https://www.reddit.com{item.get('permalink', '')}")
                if hit: hits.append(hit)
            return SourceResult(self.name, SourceStatus.OK, tuple(hits))
        except (HttpError, ValueError, TypeError, KeyError, AttributeError) as exc: return self._error(exc)
