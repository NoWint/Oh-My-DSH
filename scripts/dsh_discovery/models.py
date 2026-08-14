"""Typed repository and discovery candidate models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RepositoryCoordinate:
    host: str
    owner: str
    repository: str

    def as_key(self) -> str:
        return f"{self.host}/{self.owner}/{self.repository}".lower()


@dataclass(frozen=True)
class Candidate:
    coordinate: RepositoryCoordinate | None
    name: str
    description: str = ""
    source: str = ""
    metadata: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "coordinate": None if self.coordinate is None else {
                "host": self.coordinate.host,
                "owner": self.coordinate.owner,
                "repository": self.coordinate.repository,
            },
            "name": self.name,
            "description": self.description,
            "source": self.source,
            "metadata": self.metadata or {},
        }
