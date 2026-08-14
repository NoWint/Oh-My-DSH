"""Black-box tests for the discovery operational entrypoints."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


class DiscoveryCliTests(unittest.TestCase):
    def test_direct_script_dry_run_works_from_repo_root(self) -> None:
        repo = Path(__file__).parents[1]
        result = subprocess.run(
            ["python3", "-B", "scripts/dsh_discovery.py", "--dry-run", "--fixtures"],
            cwd=repo,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_direct_script_dry_run_works_from_tmp(self) -> None:
        repo = Path(__file__).parents[1]
        result = subprocess.run(["python3", "-B", str(repo / "scripts/dsh_discovery.py"), "--dry-run", "--fixtures", "--repo", str(repo)], cwd="/tmp", text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_dry_run_creates_no_lock_or_runtime_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            module = _load_cli_module()
            self.assertEqual(module.main(["--dry-run", "--repo", str(root)]), 0)
            self.assertFalse((root / "var").exists())

    def test_dry_run_never_writes_runtime_files_or_pushes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "var").mkdir()
            module = _load_cli_module()
            result = module.main(["--dry-run", "--fixtures", "--repo", str(root)])
            self.assertEqual(result, 0)
            self.assertFalse((root / "var/dsh-discovery-state.json").exists())
            self.assertFalse((root / "var/dsh-discovery-report.json").exists())


class InstallerTests(unittest.TestCase):
    def test_check_rejects_non_private_env_file_without_installing(self) -> None:
        import os
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            env_file = root / ".env"
            env_file.write_text("GITHUB_TOKEN=test\n", encoding="utf-8")
            os.chmod(env_file, 0o644)
            script = Path(__file__).parents[1] / "scripts/install-hourly-discovery.sh"
            result = subprocess.run([str(script), "check", str(env_file)], text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("0600", result.stderr)


def _load_cli_module():
    import importlib.util
    path = Path(__file__).parents[1] / "scripts/dsh_discovery.py"
    spec = importlib.util.spec_from_file_location("dsh_discovery_cli", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module
