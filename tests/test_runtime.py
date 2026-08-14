"""Isolated tests for the hourly discovery runtime."""

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from scripts.dsh_discovery.gitops import GitOps, GitSafetyError
from scripts.dsh_discovery.report import DiscoveryReport, save_report


class RuntimeReportTests(unittest.TestCase):
    def test_atomic_report_records_structured_run_outcome(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            report = DiscoveryReport(
                started_at=datetime(2026, 8, 14, tzinfo=timezone.utc),
                finished_at=datetime(2026, 8, 14, 1, tzinfo=timezone.utc),
                mode="dry-run",
                source_results=[{"source": "github", "status": "ok", "hits": 2}],
                actions={"readme_updated": False, "pushed": False},
            )

            save_report(path, report)

            self.assertEqual(
                json.loads(path.read_text(encoding="utf-8")),
                {
                    "actions": {"pushed": False, "readme_updated": False},
                    "finished_at": "2026-08-14T01:00:00+00:00",
                    "mode": "dry-run",
                    "source_results": [{"hits": 2, "source": "github", "status": "ok"}],
                    "started_at": "2026-08-14T00:00:00+00:00",
                    "version": 1,
                },
            )
            self.assertFalse(list(Path(directory).glob(".report.json.*.tmp")))


class GitOpsTests(unittest.TestCase):
    def test_prepare_refuses_uncontrolled_dirty_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            runner = _RecordingRunner({
                ("status", "--porcelain=v1"): " M README.md\n?? secrets.txt\n",
            })

            with self.assertRaisesRegex(GitSafetyError, "uncontrolled changes"):
                GitOps(repo, runner=runner).prepare()

            self.assertEqual(runner.calls, [("status", "--porcelain=v1")])

    def test_commit_stages_only_generated_whitelist_and_pushes_material_update(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            runner = _RecordingRunner({
                ("status", "--porcelain=v1"): " M README.md\n?? data/dsh-discovery.json\n?? var/dsh-discovery-state.json\n",
                ("diff", "--name-only", "origin/main...HEAD"): "",
                ("diff", "--cached", "--name-only"): "README.md\ndata/dsh-discovery.json\n",
            })
            git = GitOps(repo, runner=runner)

            pushed = git.commit_and_push("Update discovery catalog")

            self.assertTrue(pushed)
            self.assertIn(("add", "--", "README.md", "data/dsh-discovery.json"), runner.calls)
            self.assertIn(("push", "origin", "HEAD:main"), runner.calls)
            self.assertNotIn(("add", "--", "var/dsh-discovery-state.json"), runner.calls)


class _RecordingRunner:
    def __init__(self, outputs: dict[tuple[str, ...], str]) -> None:
        self.outputs = outputs
        self.calls: list[tuple[str, ...]] = []

    def __call__(self, arguments: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
        command = tuple(arguments[1:])
        self.calls.append(command)
        return subprocess.CompletedProcess(arguments, 0, self.outputs.get(command, ""), "")
