"""Canonicalization and conservative DSH relevance helpers."""

from __future__ import annotations

import hashlib
import re
from urllib.parse import urlsplit

from .models import Candidate, RepositoryCoordinate

_DSH_EXACT_RE = re.compile(r"(?<![a-z0-9])dsh(?![a-z0-9])", re.IGNORECASE)
_STRONG_RE = re.compile(
    r"(?:deepseek[\s_-]+harness|deepseek-harness|dsh[\s_-]+plugin|dsh[\s_-]+native|dsh[\s_-]+web)",
    re.IGNORECASE,
)
_GITLAB_CONTENT_PAGE_ACTIONS = frozenset({"blob", "raw", "tree"})


def redact_token(token: str | None) -> str | None:
    if token is None:
        return None
    if len(token) < 8:
        return "***"
    return f"{token[:4]}…{token[-4:]}"


def normalize_repository_url(value: str) -> RepositoryCoordinate | None:
    raw = value.strip()
    if raw.startswith("git@") and ":" in raw:
        host, path = raw[4:].split(":", 1)
    else:
        parsed = urlsplit(raw)
        host = parsed.hostname or ""
        path = parsed.path
    host = host.lower().rstrip(".")
    if host == "github.com":
        return _normalize_github_path(path)
    if host == "gitlab.com":
        return _normalize_gitlab_path(path)
    return None


def _normalize_github_path(path: str) -> RepositoryCoordinate | None:
    parts = [part for part in path.strip("/").split("/") if part]
    if len(parts) != 2:
        return None
    owner, repository = parts
    repository = repository.removesuffix(".git")
    if not owner or not repository:
        return None
    return RepositoryCoordinate(host="github.com", owner=owner, repository=repository)


def _normalize_gitlab_path(path: str) -> RepositoryCoordinate | None:
    parts = [part for part in path.strip("/").split("/") if part]
    if "-" in parts:
        separator = parts.index("-")
        page_parts = parts[separator + 1 :]
        if page_parts and page_parts[0] not in _GITLAB_CONTENT_PAGE_ACTIONS:
            return None
        parts = parts[:separator]
    if len(parts) < 2:
        return None
    *owner_parts, repository = parts
    repository = repository.removesuffix(".git")
    if not owner_parts or not repository:
        return None
    return RepositoryCoordinate(
        host="gitlab.com", owner="/".join(owner_parts), repository=repository
    )


def is_dsh_relevant(*, name: str, description: str = "", topics: tuple[str, ...] = ()) -> bool:
    text = " ".join((name, description, *topics))
    if _STRONG_RE.search(text):
        return True
    return bool(_DSH_EXACT_RE.search(name) and any(
        marker in text.lower() for marker in ("deepseek", "harness", "plugin")
    ))


def candidate_fingerprint(candidate: Candidate) -> str:
    if candidate.coordinate is not None:
        identity = candidate.coordinate.as_key()
    else:
        identity = "|".join((candidate.source.lower(), candidate.name.strip().lower()))
    return hashlib.sha256(identity.encode("utf-8")).hexdigest()
