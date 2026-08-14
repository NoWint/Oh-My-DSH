"""Canonicalization and conservative DSH relevance helpers."""

from __future__ import annotations

import hashlib
import re
from urllib.parse import unquote, urlsplit

from .models import Candidate, RepositoryCoordinate

_TOKEN_RE = re.compile(r"[A-Za-z0-9_\-]{8,}")
_DSH_EXACT_RE = re.compile(r"(?<![a-z0-9])dsh(?![a-z0-9])", re.IGNORECASE)
_STRONG_RE = re.compile(
    r"(?:deepseek[\s_-]+harness|deepseek-harness|dsh[\s_-]+plugin|dsh[\s_-]+native|dsh[\s_-]+web)",
    re.IGNORECASE,
)


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
    if host not in {"github.com", "gitlab.com"}:
        return None
    parts = [part for part in path.strip("/").split("/") if part]
    if len(parts) < 2:
        return None
    parts[-1] = parts[-1].removesuffix(".git")
    if not parts[-1]:
        return None
    owner = "/".join(parts[:-1])
    return RepositoryCoordinate(host=host, owner=owner, repository=parts[-1])


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
