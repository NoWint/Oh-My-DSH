"""Versioned, atomically persisted discovery state."""

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class DiscoveryState:
    seen_fingerprints: set[str] = field(default_factory=set)
    updated_at: datetime | None = None
    version: int = 1

    def to_dict(self) -> dict[str, Any]:
        updated = self.updated_at or datetime.now(timezone.utc)
        return {
            "version": self.version,
            "seen_fingerprints": sorted(self.seen_fingerprints),
            "updated_at": updated.astimezone(timezone.utc).isoformat(),
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "DiscoveryState":
        raw_updated = payload.get("updated_at")
        updated = datetime.fromisoformat(raw_updated) if raw_updated else None
        return cls(
            seen_fingerprints=set(payload.get("seen_fingerprints", [])),
            updated_at=updated,
            version=int(payload.get("version", 1)),
        )


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
