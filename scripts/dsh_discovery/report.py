"""Structured, atomically persisted reports for discovery runs."""

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

_REPORT_VERSION = 1


@dataclass(frozen=True)
class DiscoveryReport:
    started_at: datetime
    finished_at: datetime
    mode: str
    source_results: Sequence[Mapping[str, Any]] = field(default_factory=tuple)
    actions: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        for timestamp in (self.started_at, self.finished_at):
            if timestamp.tzinfo is None or timestamp.utcoffset() is None:
                raise ValueError("report timestamps must be timezone-aware")
        return {
            "version": _REPORT_VERSION,
            "started_at": self.started_at.isoformat(),
            "finished_at": self.finished_at.isoformat(),
            "mode": self.mode,
            "source_results": [dict(result) for result in self.source_results],
            "actions": dict(self.actions),
        }


def save_report(path: Path, report: DiscoveryReport) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(report.to_dict(), handle, indent=2, sort_keys=True)
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
