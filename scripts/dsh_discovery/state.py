"""Versioned, atomically persisted discovery state."""

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_STATE_VERSION = 1


@dataclass(frozen=True)
class DiscoveryState:
    seen_fingerprints: set[str] = field(default_factory=set)
    updated_at: datetime | None = None
    version: int = _STATE_VERSION

    def to_dict(self) -> dict[str, Any]:
        if self.version != _STATE_VERSION:
            raise ValueError(f"unsupported discovery state version: {self.version}")
        updated = self.updated_at or datetime.now(timezone.utc)
        if updated.tzinfo is None or updated.utcoffset() is None:
            raise ValueError("discovery state timestamp must be timezone-aware")
        return {
            "version": self.version,
            "seen_fingerprints": sorted(self.seen_fingerprints),
            "updated_at": updated.astimezone(timezone.utc).isoformat(),
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "DiscoveryState":
        expected_keys = {"version", "seen_fingerprints", "updated_at"}
        if set(payload) != expected_keys:
            raise ValueError("discovery state has an invalid schema")
        if type(payload["version"]) is not int or payload["version"] != _STATE_VERSION:
            raise ValueError(f"unsupported discovery state version: {payload['version']}")
        fingerprints = payload["seen_fingerprints"]
        if not isinstance(fingerprints, list) or not all(isinstance(item, str) for item in fingerprints):
            raise ValueError("discovery state fingerprints must be a list of strings")
        raw_updated = payload["updated_at"]
        if not isinstance(raw_updated, str):
            raise ValueError("discovery state timestamp must be an ISO timestamp string")
        try:
            updated = datetime.fromisoformat(raw_updated)
        except ValueError as error:
            raise ValueError("discovery state timestamp must be ISO 8601") from error
        if updated.tzinfo is None or updated.utcoffset() is None:
            raise ValueError("discovery state timestamp must be timezone-aware")
        return cls(seen_fingerprints=set(fingerprints), updated_at=updated, version=_STATE_VERSION)


def load_state(path: Path) -> DiscoveryState:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return DiscoveryState()
    if not isinstance(payload, dict):
        raise ValueError("discovery state must be a JSON object")
    return DiscoveryState.from_dict(payload)


def save_state(path: Path, state: DiscoveryState) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(state.to_dict(), handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise
