"""Canonical public-host repository validation and candidate deduplication."""

from __future__ import annotations

import base64
import binascii
import json
import re
from dataclasses import dataclass
from enum import Enum
from typing import Any, Iterable
from urllib.parse import quote

from .models import Candidate, RepositoryCoordinate
from .sources import HttpClient, HttpError


class EvidenceClass(str, Enum):
    VALIDATED = "validated"
    PROBABLE = "probable"
    LEAD = "lead"
    REJECTED = "rejected"


@dataclass(frozen=True)
class ValidationResult:
    candidate: Candidate
    classification: EvidenceClass
    reason: str
    evidence: tuple[str, ...] = ()


_DSH = r"(?:DeepSeek[\s_-]+Harness|\bDSH\b)"
_NEGATIVE_EVIDENCE = re.compile(r"\b(?:not supported|does not support|no support|without support|unrelated to|mentions?|comparison|compare)\b", re.IGNORECASE)
_AFFIRMATIVE_EVIDENCE = re.compile(
    rf"(?:\b(?:provides?|implements?|integrates?|installs?|adds?|extends?)\b[^.\n]{{0,100}}{_DSH}|{_DSH}[^.\n]{{0,100}}\b(?:plugin|integration|extension)\b)",
    re.IGNORECASE,
)


class RepositoryValidator:
    """Validates only canonical, publicly accessible GitHub/GitLab projects."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    @staticmethod
    def deduplicate(candidates: Iterable[Candidate]) -> tuple[tuple[Candidate, ...], tuple[Candidate, ...]]:
        seen: set[str] = set()
        kept: list[Candidate] = []
        duplicates: list[Candidate] = []
        for candidate in candidates:
            if candidate.coordinate is None or candidate.coordinate.as_key() in seen:
                duplicates.append(candidate)
                continue
            seen.add(candidate.coordinate.as_key())
            kept.append(candidate)
        return tuple(kept), tuple(duplicates)

    def validate(self, candidate: Candidate) -> ValidationResult:
        coordinate = candidate.coordinate
        if coordinate is None:
            return self._rejected(candidate, "repository URL is not canonical")
        if coordinate.host == "github.com":
            return self._validate_github(candidate, coordinate)
        if coordinate.host == "gitlab.com":
            return self._validate_gitlab(candidate, coordinate)
        return self._rejected(candidate, "unsupported repository host")

    def _validate_github(self, candidate: Candidate, coordinate: RepositoryCoordinate) -> ValidationResult:
        endpoint = f"https://api.github.com/repos/{quote(coordinate.owner, safe='')}/{quote(coordinate.repository, safe='')}"
        payload = self._get_object(candidate, endpoint)
        if payload is None:
            return self._rejected(candidate, "repository inaccessible or malformed metadata")
        reason = self._metadata_rejection(payload, coordinate, "full_name", github=True)
        if reason:
            return self._rejected(candidate, reason)
        readme = self._get_object(candidate, endpoint + "/readme")
        if readme is None:
            return self._rejected(candidate, "README inaccessible or malformed")
        text = self._readme_text(readme)
        if text is None:
            return self._rejected(candidate, "README malformed")
        if _has_affirmative_integration_evidence(text):
            return ValidationResult(candidate, EvidenceClass.VALIDATED, "explicit DSH integration evidence", ("README",))
        return ValidationResult(candidate, EvidenceClass.LEAD, "no explicit DSH integration evidence")

    def _validate_gitlab(self, candidate: Candidate, coordinate: RepositoryCoordinate) -> ValidationResult:
        project = quote(f"{coordinate.owner}/{coordinate.repository}", safe="")
        payload = self._get_object(candidate, f"https://gitlab.com/api/v4/projects/{project}")
        if payload is None:
            return self._rejected(candidate, "repository inaccessible or malformed metadata")
        reason = self._metadata_rejection(payload, coordinate, "path_with_namespace", github=False)
        if reason:
            return self._rejected(candidate, reason)
        description = payload.get("description")
        if not isinstance(description, str):
            return self._rejected(candidate, "repository metadata malformed")
        if _has_affirmative_integration_evidence(description):
            return ValidationResult(candidate, EvidenceClass.PROBABLE, "public metadata indicates DSH integration", ("metadata",))
        if _NEGATIVE_EVIDENCE.search(description):
            return self._rejected(candidate, "no affirmative DSH integration evidence")
        return ValidationResult(candidate, EvidenceClass.LEAD, "no explicit DSH integration evidence")

    def _get_object(self, candidate: Candidate, url: str) -> dict[str, Any] | None:
        try:
            response = self.client.get(url)
            if response.status != 200:
                return None
            payload = json.loads(response.body)
        except (HttpError, UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError):
            return None
        return payload if isinstance(payload, dict) else None

    @staticmethod
    def _metadata_rejection(payload: dict[str, Any], coordinate: RepositoryCoordinate, identity_key: str, *, github: bool) -> str:
        identity = payload.get(identity_key)
        if not isinstance(identity, str) or identity.lower() != f"{coordinate.owner}/{coordinate.repository}".lower():
            return "canonical repository identity mismatch"
        if payload.get("archived") is not False:
            return "repository is archived or metadata malformed"
        if github:
            if payload.get("fork") is not False:
                return "repository is a fork or metadata malformed"
            if payload.get("mirror") not in (False, None) or payload.get("mirror_url") not in (None, ""):
                return "repository is a mirror"
            if payload.get("private") is not False or payload.get("visibility") != "public":
                return "explicit public status is required"
            topics = payload.get("topics")
            if topics is not None and (not isinstance(topics, list) or not all(isinstance(topic, str) for topic in topics)):
                return "repository metadata malformed"
        else:
            if payload.get("forked_from_project") not in (None, False):
                return "repository is a fork"
            if payload.get("mirror") not in (False, None) or payload.get("mirror_project_id") not in (None, 0):
                return "repository is a mirror"
            if payload.get("visibility") != "public":
                return "explicit public status is required"
            tags = payload.get("tag_list")
            if tags is not None and (not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags)):
                return "repository metadata malformed"
        return ""

    @staticmethod
    def _readme_text(payload: dict[str, Any]) -> str | None:
        content = payload.get("content")
        encoding = payload.get("encoding")
        if not isinstance(content, str):
            return None
        if encoding is None:
            return content
        if encoding != "base64":
            return None
        try:
            return base64.b64decode(content, validate=True).decode("utf-8")
        except (binascii.Error, UnicodeDecodeError, ValueError):
            return None

    @staticmethod
    def _rejected(candidate: Candidate, reason: str) -> ValidationResult:
        return ValidationResult(candidate, EvidenceClass.REJECTED, reason)


def _has_affirmative_integration_evidence(text: str) -> bool:
    return bool(_AFFIRMATIVE_EVIDENCE.search(text) and not _NEGATIVE_EVIDENCE.search(text))
