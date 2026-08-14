#!/usr/bin/env python3
"""Run the bounded DSH discovery pipeline safely."""

from __future__ import annotations

import argparse
import fcntl
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

_REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(_REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPOSITORY_ROOT))

from scripts.dsh_discovery.report import DiscoveryReport, save_report
from scripts.dsh_discovery.state import DiscoveryState, save_state


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--fixtures", action="store_true")
    arguments = parser.parse_args(argv)
    repo = arguments.repo.resolve()
    if arguments.dry_run or arguments.fixtures:
        return 0
    lock_path = repo / "var/dsh-discovery.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return 0
        try:
            mode = "live"
            now = datetime.now(timezone.utc)
            old = Path.cwd()
            try:
                os.chdir(repo)
                save_state(Path("var/dsh-discovery-state.json"), DiscoveryState(updated_at=now))
                save_report(Path("var/dsh-discovery-report.json"), DiscoveryReport(now, now, mode, (), {"readme_updated": False, "pushed": False, "state_updated": True, "report_written": True}))
            finally:
                os.chdir(old)
            return 0
        finally:
            fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


if __name__ == "__main__":
    raise SystemExit(main())
