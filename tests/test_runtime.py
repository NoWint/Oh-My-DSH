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
            root = Path(directory)
            (root / "var").mkdir()
            path = Path("var/report.json")
            report = DiscoveryReport(
                started_at=datetime(2026, 8, 14, tzinfo=timezone.utc),
                finished_at=datetime(2026, 8, 14, 1, tzinfo=timezone.utc),
                mode="dry-run",
                source_results=[{"source": "github", "status": "ok", "hits": 2}],
                actions={"readme_updated": False, "pushed": False},
            )
            old = Path.cwd()
            try:
                import os
                os.chdir(root)
                save_report(path, report)
            finally:
                os.chdir(old)
            self.assertEqual(json.loads((root / path).read_text(encoding="utf-8"))["version"], 1)
            self.assertFalse(list((root / "var").glob(".report.json.*.tmp")))

    def test_report_redacts_nested_secrets_and_secret_shaped_values(self) -> None:
        report = DiscoveryReport(
            started_at=datetime(2026, 8, 14, tzinfo=timezone.utc),
            finished_at=datetime(2026, 8, 14, 1, tzinfo=timezone.utc),
            mode="live",
            source_results=[{"source": "github", "status": "ok", "hits": 1, "message": {"api_token": "ghp_abcdefghijklmnopqrstuvwxyz", "note": "safe"}}],
            actions={"pushed": False, "readme_updated": False},
        )
        payload = report.to_dict()
        self.assertEqual(payload["source_results"][0]["message"]["api_token"], "[REDACTED]")
        self.assertEqual(payload["source_results"][0]["message"]["note"], "safe")

    def test_report_rejects_invalid_v1_mode_and_schema(self) -> None:
        base = dict(started_at=datetime(2026, 8, 14, tzinfo=timezone.utc), finished_at=datetime(2026, 8, 14, 1, tzinfo=timezone.utc), source_results=[], actions={})
        with self.assertRaises(ValueError):
            DiscoveryReport(mode="unknown", **base).to_dict()
        with self.assertRaises(ValueError):
            DiscoveryReport(mode="live", source_results=[{"source": "github", "status": "bad", "hits": 1}], actions={}, **{key: value for key, value in base.items() if key not in ("source_results", "actions")}).to_dict()
        with self.assertRaises(ValueError):
            DiscoveryReport(mode="live", source_results=[{"source": "github", "status": "ok", "hits": 1, "unexpected": True}], actions={}, **{key: value for key, value in base.items() if key not in ("source_results", "actions")}).to_dict()

    def test_report_rejects_absolute_traversal_and_symlink_escape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "var").mkdir()
            report = DiscoveryReport(datetime.now(timezone.utc), datetime.now(timezone.utc), "live")
            old = Path.cwd()
            try:
                import os
                os.chdir(root)
                for path in (Path("../escape.json"), Path("/tmp/escape.json")):
                    with self.assertRaises(ValueError):
                        save_report(path, report)
                (root / "var" / "link").symlink_to(root / "outside", target_is_directory=False)
                with self.assertRaises(ValueError):
                    save_report(Path("var/link/report.json"), report)
            finally:
                os.chdir(old)

    def test_report_replace_fsync_failure_is_tolerated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "var").mkdir()
            report = DiscoveryReport(datetime.now(timezone.utc), datetime.now(timezone.utc), "live")
            old = Path.cwd()
            try:
                import os
                os.chdir(root)
                save_report(Path("var/report.json"), report, directory_fsync=lambda _: (_ for _ in ()).throw(OSError("unsupported")))
                self.assertTrue((root / "var/report.json").exists())
            finally:
                os.chdir(old)


class GitOpsTests(unittest.TestCase):
    def test_prepare_refuses_uncontrolled_dirty_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            runner = _RecordingRunner({
                ("status", "--porcelain=v1"): " M README.md\n?? secrets.txt\n",
            })

            with self.assertRaisesRegex(GitSafetyError, "uncontrolled changes"):
                GitOps(repo, runner=runner).prepare()

            self.assertEqual(
                runner.calls,
                [("diff", "--cached", "--quiet"), ("branch", "--show-current"), ("status", "--porcelain=v1")],
            )

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
    def test_commit_skips_push_when_only_controlled_runtime_files_changed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runner = _RecordingRunner({
                ("status", "--porcelain=v1"): "?? var/dsh-discovery-state.json\n?? var/dsh-discovery-report.json\n",
            })

            pushed = GitOps(Path(directory), runner=runner).commit_and_push("No catalog update")

            self.assertFalse(pushed)
            self.assertIn(("fetch", "origin", "main"), runner.calls)
            self.assertNotIn(("push", "origin", "HEAD:main"), runner.calls)

    def test_prepare_refuses_branch_behind_origin_main(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runner = _RecordingRunner({
                ("status", "--porcelain=v1"): "",
                ("rev-parse", "HEAD"): "old-tip\n",
                ("rev-parse", "origin/main"): "new-tip\n",
            })

            with self.assertRaisesRegex(GitSafetyError, "does not match"):
                GitOps(Path(directory), runner=runner).prepare()

            self.assertIn(("fetch", "origin", "main"), runner.calls)
    def test_prepare_refuses_pre_existing_staged_changes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runner = _RecordingRunner({
                ("diff", "--cached", "--quiet"): (1, "", ""),
            })

            with self.assertRaisesRegex(GitSafetyError, "staged changes"):
                GitOps(Path(directory), runner=runner).prepare()

            self.assertEqual(runner.calls, [("diff", "--cached", "--quiet")])

    def test_prepare_refuses_non_main_branch_or_divergent_tip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for outputs, expected in (
                ({("diff", "--cached", "--quiet"): (0, "", ""), ("branch", "--show-current"): "feature\n"}, "main branch"),
                ({("diff", "--cached", "--quiet"): (0, "", ""), ("branch", "--show-current"): "main\n", ("status", "--porcelain=v1"): "", ("rev-parse", "HEAD"): "local\n", ("rev-parse", "origin/main"): "remote\n"}, "does not match"),
            ):
                with self.subTest(expected=expected), self.assertRaisesRegex(GitSafetyError, expected):
                    GitOps(Path(directory), runner=_RecordingRunner(outputs)).prepare()


class _RecordingRunner:
    def __init__(self, outputs: dict[tuple[str, ...], str | tuple[int, str, str]]) -> None:
        self.outputs = outputs
        self.calls: list[tuple[str, ...]] = []

    def __call__(self, arguments: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
        command = tuple(arguments[1:])
        self.calls.append(command)
        output = self.outputs.get(command)
        if output is None:
            defaults = {
                ("diff", "--cached", "--quiet"): (0, "", ""),
                ("branch", "--show-current"): "main\n",
                ("rev-parse", "HEAD"): "tip\n",
                ("rev-parse", "origin/main"): "tip\n",
            }
            output = defaults.get(command, "")
        if isinstance(output, tuple):
            return subprocess.CompletedProcess(arguments, *output)
        return subprocess.CompletedProcess(arguments, 0, output, "")
