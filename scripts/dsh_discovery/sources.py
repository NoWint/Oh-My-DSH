"""Bounded, dependency-free discovery source adapters."""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Mapping

from .models import Candidate
from .normalization import normalize_repository_url


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

    def __init__(self, transport: Callable[[urllib.request.Request, float], Any] | None = None, *, timeout: float = 20.0, max_retries: int = 2, sleep: Callable[[float], None] = time.sleep) -> None:
        self.transport = transport or self._urlopen
        self.timeout = max(0.1, float(timeout))
        self.max_retries = max(0, int(max_retries))
        self.sleep = sleep

    def get(self, url: str, *, headers: Mapping[str, str] | None = None) -> HttpResponse:
        return self.request(url, headers=headers)

    def request(self, url: str, *, headers: Mapping[str, str] | None = None, data: bytes | None = None) -> HttpResponse:
        request_headers = {"User-Agent": self.USER_AGENT, "Accept": "application/json, application/xml, text/xml"}
        request_headers.update(headers or {})
        request = urllib.request.Request(url, data=data, headers=request_headers, method="POST" if data is not None else "GET")
        for attempt in range(self.max_retries + 1):
            try:
                response = self.transport(request, self.timeout)
                if isinstance(response, FakeResponse):
                    body = response.body if isinstance(response.body, bytes) else json.dumps(response.body).encode("utf-8")
                    if response.status in {429, 403} or response.status >= 500:
                        if attempt < self.max_retries:
                            self.sleep(0)
                            continue
                        raise HttpError(f"HTTP status {response.status}")
                    return HttpResponse(response.status, body, response.headers or {})
                status = getattr(response, "status", response.getcode())
                body = response.read()
                if status in {429, 403} or status >= 500:
                    if attempt < self.max_retries:
                        self.sleep(0)
                        continue
                    raise HttpError(f"HTTP status {status}")
                return HttpResponse(status, body, dict(getattr(response, "headers", {})))
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                if attempt < self.max_retries:
                    self.sleep(0)
                    continue
                raise HttpError(f"request failed: {type(exc).__name__}") from None
        raise HttpError("request failed")

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


class _Source:
    name = "source"
    pages = 1
    query_budget = 1
    request_budget = 1

    def __init__(self, client: HttpClient, *, pages: int | None = None) -> None:
        self.client = client
        self.pages = min(self.pages, max(0, pages if pages is not None else self.pages))

    def _request(self, url: str, *, headers: Mapping[str, str] | None = None) -> HttpResponse:
        return self.client.get(url, headers=headers)

    def _error(self, exc: Exception) -> SourceResult:
        return SourceResult(self.name, SourceStatus.ERROR, message=f"{type(exc).__name__}: source response unavailable")


class GitHubSource(_Source):
    name = "github"
    pages = 2
    query_budget = 1
    request_budget = 2

    def discover(self) -> SourceResult:
        hits = []
        try:
            for page in range(self.pages):
                params = urllib.parse.urlencode({"q": "dsh OR deepseek-harness", "sort": "updated", "per_page": 30, "page": page + 1})
                headers = {"Authorization": f"Bearer {token}"} if (token := os.environ.get("GITHUB_TOKEN")) else {}
                payload = json.loads(self._request(f"https://api.github.com/search/repositories?{params}", headers=headers).body)
                for item in payload.get("items", []):
                    coordinate = normalize_repository_url(item.get("html_url", ""))
                    if coordinate:
                        hits.append(DiscoveryHit(Candidate(coordinate, item.get("name", ""), item.get("description") or "", self.name, {"topics": item.get("topics", [])}), item.get("html_url", "")))
            return SourceResult(self.name, SourceStatus.OK, tuple(hits))
        except (HttpError, ValueError, TypeError, KeyError, AttributeError) as exc:
            return self._error(exc)


class GitLabSource(_Source):
    name = "gitlab"
    pages = 2
    query_budget = 1
    request_budget = 2

    def discover(self) -> SourceResult:
        hits = []
        try:
            for page in range(self.pages):
                query = urllib.parse.urlencode({"search": "dsh", "per_page": 20, "page": page + 1})
                headers = {"PRIVATE-TOKEN": token} if (token := os.environ.get("GITLAB_TOKEN")) else {}
                payload = json.loads(self._request(f"https://gitlab.com/api/v4/projects?{query}", headers=headers).body)
                for item in payload:
                    url = item.get("web_url", "")
                    hits.append(DiscoveryHit(Candidate(normalize_repository_url(url), item.get("name", ""), item.get("description") or "", self.name), url))
            return SourceResult(self.name, SourceStatus.OK, tuple(hits))
        except (HttpError, ValueError, TypeError, KeyError, AttributeError) as exc:
            return self._error(exc)


class HackerNewsSource(_Source):
    name = "hackernews"
    request_budget = 3

    def discover(self) -> SourceResult:
        hits = []
        try:
            for kind in ("newstories", "askstories", "showstories"):
                ids = json.loads(self._request(f"https://hacker-news.firebaseio.com/v0/{kind}.json").body)
                for item_id in ids[:10]:
                    hits.append(
                        DiscoveryHit(
                            Candidate(None, f"{kind}:{item_id}", "", self.name),
                            f"https://news.ycombinator.com/item?id={item_id}",
                        )
                    )
            return SourceResult(self.name, SourceStatus.OK, tuple(hits))
        except (HttpError, ValueError, TypeError, KeyError, AttributeError) as exc:
            return self._error(exc)


class LobstersSource(_Source):
    name = "lobsters"
    request_budget = 1

    def discover(self) -> SourceResult:
        try:
            root = ET.fromstring(self._request("https://lobste.rs/rss").body)
            hits = tuple(DiscoveryHit(Candidate(None, item.findtext("title", ""), item.findtext("description", ""), self.name), item.findtext("link", "")) for item in root.findall(".//item"))
            return SourceResult(self.name, SourceStatus.OK, hits)
        except (HttpError, ET.ParseError, ValueError, TypeError, AttributeError) as exc:
            return self._error(exc)


class StackExchangeSource(_Source):
    name = "stackexchange"
    pages = 2
    request_budget = 2

    def discover(self) -> SourceResult:
        try:
            hits = []
            for page in range(self.pages):
                query = urllib.parse.urlencode({"order": "desc", "sort": "activity", "intitle": "deepseek harness", "site": "stackoverflow", "pagesize": 20, "page": page + 1})
                payload = json.loads(self._request(f"https://api.stackexchange.com/2.3/search/advanced?{query}").body)
                for item in payload.get("items", []):
                    hits.append(DiscoveryHit(Candidate(None, item.get("title", ""), item.get("body_markdown", "") or "", self.name), item.get("link", "")))
            return SourceResult(self.name, SourceStatus.OK, tuple(hits))
        except (HttpError, ValueError, TypeError, KeyError, AttributeError) as exc:
            return self._error(exc)


class RedditSource(_Source):
    name = "reddit"
    request_budget = 2

    def discover(self) -> SourceResult:
        client_id = os.environ.get("REDDIT_CLIENT_ID")
        client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
        if not (client_id and client_secret):
            return SourceResult(self.name, SourceStatus.SKIPPED, message="official OAuth configuration absent")
        try:
            credentials = f"{client_id}:{client_secret}".encode("utf-8")
            authorization = "Basic " + __import__("base64").b64encode(credentials).decode("ascii")
            token_payload = json.loads(self.client.request(
                "https://www.reddit.com/api/v1/access_token",
                headers={"Authorization": authorization, "Content-Type": "application/x-www-form-urlencoded"},
                data=b"grant_type=client_credentials",
            ).body)
            access_token = token_payload["access_token"]
            payload = json.loads(self._request(
                "https://oauth.reddit.com/search.json?q=dsh+OR+deepseek-harness&limit=25",
                headers={"Authorization": f"Bearer {access_token}"},
            ).body)
            hits = tuple(
                DiscoveryHit(Candidate(None, item.get("title", ""), item.get("selftext", "") or "", self.name), f"https://www.reddit.com{item.get('permalink', '')}")
                for item in payload.get("data", {}).get("children", [])
                for item in [item.get("data", {})]
            )
            return SourceResult(self.name, SourceStatus.OK, hits)
        except (HttpError, ValueError, TypeError, KeyError, AttributeError) as exc:
            return self._error(exc)
