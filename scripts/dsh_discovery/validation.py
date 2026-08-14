"""Canonical public-host repository validation and candidate deduplication."""

from __future__ import annotations

import base64
import json
from dataclasses import dataclass
from enum import Enum
from typing import Iterable
from urllib.parse import quote

from .models import Candidate, RepositoryCoordinate
from .normalization import is_dsh_relevant
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


class RepositoryValidator:
    """Validates canonical GitHub/GitLab repository coordinates via injected HTTP."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    @staticmethod
    def deduplicate(candidates: Iterable[Candidate]) -> tuple[tuple[Candidate, ...], tuple[Candidate, ...]]:
        seen: set[str] = set()
        kept: list[Candidate] = []
        duplicates: list[Candidate] = []
        for candidate in candidates:
            if candidate.coordinate is None:
                duplicates.append(candidate)
                continue
            key = candidate.coordinate.as_key()
            if key in seen:
                duplicates.append(candidate)
            else:
                seen.add(key)
                kept.append(candidate)
        return tuple(kept), tuple(duplicates)

    def validate(self, candidate: Candidate) -> ValidationResult:
        coordinate = candidate.coordinate
        if coordinate is None:
            return ValidationResult(candidate, EvidenceClass.REJECTED, "repository URL is not canonical")
        if coordinate.host == "github.com":
            return self._validate_github(candidate, coordinate)
        if coordinate.host == "gitlab.com":
            return self._validate_gitlab(candidate, coordinate)
        return ValidationResult(candidate, EvidenceClass.REJECTED, "unsupported repository host")

    def _validate_github(self, candidate: Candidate, coordinate: RepositoryCoordinate) -> ValidationResult:
        url = f"https://api.github.com/repos/{quote(coordinate.owner, safe='')}/{quote(coordinate.repository, safe='')}"
        try:
            response = self.client.get(url)
        except HttpError:
            return ValidationResult(candidate, EvidenceClass.REJECTED, "repository inaccessible")
        if response.status != 200:
            return ValidationResult(candidate, EvidenceClass.REJECTED, "repository inaccessible")
        payload = self._payload(response.body)
        rejection = self._rejection_reason(payload, github=True)
        if rejection:
            return ValidationResult(candidate, EvidenceClass.REJECTED, rejection)
        metadata_text = self._metadata_text(candidate, payload)
        if is_dsh_relevant(name=candidate.name, description=metadata_text, topics=tuple(payload.get("topics", ()))):
            try:
                readme = self.client.get(url + "/readme")
                if readme.status == 200 and self._readme_has_evidence(self._payload(readme.body)):
                    return ValidationResult(candidate, EvidenceClass.VALIDATED, "explicit DSH integration evidence", ("README",))
            except HttpError:
                pass
        return ValidationResult(candidate, EvidenceClass.LEAD, "no explicit DSH integration evidence")

    def _validate_gitlab(self, candidate: Candidate, coordinate: RepositoryCoordinate) -> ValidationResult:
        project = quote(f"{coordinate.owner}/{coordinate.repository}", safe="")
        try:
            response = self.client.get(f"https://gitlab.com/api/v4/projects/{project}")
        except HttpError:
            return ValidationResult(candidate, EvidenceClass.REJECTED, "repository inaccessible")
        if response.status != 200:
            return ValidationResult(candidate, EvidenceClass.REJECTED, "repository inaccessible")
        payload = self._payload(response.body)
        rejection = self._rejection_reason(payload, github=False)
        if rejection:
            return ValidationResult(candidate, EvidenceClass.REJECTED, rejection)
        text = self._metadata_text(candidate, payload)
        if is_dsh_relevant(name=candidate.name, description=text, topics=tuple(payload.get("tag_list", ()))):
            return ValidationResult(candidate, EvidenceClass.PROBABLE, "public metadata indicates DSH integration", ("metadata",))
        return ValidationResult(candidate, EvidenceClass.LEAD, "no explicit DSH integration evidence")

    @staticmethod
    def _payload(body: bytes) -> dict:
        payload = json.loads(body)
        return payload if isinstance(payload, dict) else {}

    @staticmethod
    def _metadata_text(candidate: Candidate, payload: dict) -> str:
        return " ".join(str(payload.get(key) or "") for key in ("description", "readme_url", "name", "path_with_namespace")) + " " + candidate.description

    @staticmethod
    def _rejection_reason(payload: dict, *, github: bool) -> str:
        if payload.get("archived"):
            return "repository is archived"
        if payload.get("fork") or payload.get("forked_from_project"):
            return "repository is a fork"
        if payload.get("mirror") or payload.get("mirror_url"):
            return "repository is a mirror"
        if payload.get("private") or payload.get("visibility") not in (None, "public"):
            return "repository is inaccessible"
        return ""

    @staticmethod
    def _readme_has_evidence(payload: dict) -> bool:
        content = payload.get("content", "")
        if payload.get("encoding") == "base64" and isinstance(content, str):
            try:
                content = base64.b64decode(content).decode("utf-8", "replace")
            except ValueError:
                return False
        return is_dsh_relevant(name="README", description=str(content))
