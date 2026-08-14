"""Structured, atomically persisted reports for discovery runs."""

from __future__ import annotations

import json
import os
import re
import tempfile
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

_REPORT_VERSION = 1
_MODES = {"live", "dry-run", "fixtures"}
_SOURCE_KEYS = {"source", "status", "hits", "message"}
_STATUS = {"ok", "error", "skipped"}
_SECRET_KEYS = re.compile(r"(?:token|secret|password|authorization|api[_-]?key|credential|private[_-]?key)", re.I)
_SECRET_VALUES = re.compile(r"(?:gh[pousr]_[A-Za-z0-9_]+|glpat-[A-Za-z0-9_-]+|bearer\s+\S+|(?:token|secret|password|api[_-]?key)\s*[:=]\s*\S+)", re.I)


@dataclass(frozen=True)
class DiscoveryReport:
    started_at: datetime
    finished_at: datetime
    mode: str
    source_results: Sequence[Mapping[str, Any]] = field(default_factory=tuple)
    actions: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        if self.mode not in _MODES:
            raise ValueError("report mode is invalid")
        for timestamp in (self.started_at, self.finished_at):
            if timestamp.tzinfo is None or timestamp.utcoffset() is None:
                raise ValueError("report timestamps must be timezone-aware")
        if not isinstance(self.source_results, (list, tuple)) or not isinstance(self.actions, Mapping):
            raise ValueError("report v1 schema is invalid")
        sources = []
        for result in self.source_results:
            if not isinstance(result, Mapping) or not set(result).issubset(_SOURCE_KEYS) or not {"source", "status", "hits"}.issubset(result):
                raise ValueError("report source schema is invalid")
            if not isinstance(result["source"], str) or result["status"] not in _STATUS or type(result["hits"]) is not int or result["hits"] < 0:
                raise ValueError("report source values are invalid")
            sources.append(_redact(dict(result)))
        return {
            "version": _REPORT_VERSION,
            "started_at": self.started_at.isoformat(),
            "finished_at": self.finished_at.isoformat(),
            "mode": self.mode,
            "source_results": sources,
            "actions": _redact(dict(self.actions)),
        }


def save_report(path: Path, report: DiscoveryReport, *, runtime_root: Path = Path("var"), directory_fsync: Callable[[int], None] | None = None) -> None:
    if path.is_absolute():
        raise ValueError("report path must be relative to runtime root")
    root = runtime_root.resolve()
    destination = path.resolve()
    try:
        destination.relative_to(root)
    except ValueError:
        raise ValueError("report path escapes runtime root") from None
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.parent.is_symlink() or any(parent.is_symlink() for parent in destination.relative_to(root).parents if parent != Path(".")):
        raise ValueError("report path traverses a symlink")
    fd, temporary = tempfile.mkstemp(prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(report.to_dict(), handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
        try:
            _sync_directory(destination.parent, directory_fsync)
        except OSError:
            pass
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def _sync_directory(path: Path, callback: Callable[[int], None] | None) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        (callback or os.fsync)(fd)
    finally:
        os.close(fd)


def _redact(value: Any, key: str = "") -> Any:
    if _SECRET_KEYS.search(key):
        return "[REDACTED]"
    if isinstance(value, Mapping):
        return {str(item_key): _redact(item_value, str(item_key)) for item_key, item_value in value.items()}
    if isinstance(value, list):
        return [_redact(item, key) for item in value]
    if isinstance(value, tuple):
        return [_redact(item, key) for item in value]
    if isinstance(value, str) and _SECRET_VALUES.search(value):
        return "[REDACTED]"
    return value
