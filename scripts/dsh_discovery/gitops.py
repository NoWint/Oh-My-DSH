"""Safe, narrow Git operations for discovery publication."""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path
from typing import Callable, Sequence


class GitSafetyError(RuntimeError):
    pass


CommandRunner = Callable[..., subprocess.CompletedProcess[str]]


class GitOps:
    """Permit only a current, whitelisted fast-forward publication."""

    GENERATED_PREFIXES = ("var/dsh-discovery-",)
    PUBLISHABLE = {"README.md", "data/dsh-discovery.json"}

    def __init__(self, repo: Path, *, runner: CommandRunner | None = None) -> None:
        self.repo = repo
        self.runner = runner or self._run

    def prepare(self) -> None:
        if self._command("diff", "--cached", "--quiet", check=False).returncode != 0:
            raise GitSafetyError("pre-existing staged changes are not permitted")
        if self._output("branch", "--show-current").strip() != "main":
            raise GitSafetyError("publication requires the main branch")
        dirty = self._dirty_paths()
        uncontrolled = [path for path in dirty if not self._is_controlled(path)]
        if uncontrolled:
            raise GitSafetyError("uncontrolled changes in worktree: " + ", ".join(uncontrolled))
        self._command("fetch", "origin", "main")
        head = self._output("rev-parse", "HEAD").strip()
        remote = self._output("rev-parse", "origin/main").strip()
        if not head or head != remote:
            raise GitSafetyError("local main tip does not match fetched origin/main")

    def commit_and_push(self, message: str) -> bool:
        self.prepare()
        dirty = self._dirty_paths()
        publishable = sorted(path for path in dirty if path in self.PUBLISHABLE)
        if not publishable:
            return False
        before_head = self._output("rev-parse", "HEAD").strip()
        index_backup = self._backup_index()
        self._command("add", "--", *publishable)
        staged = self._output("diff", "--cached", "--name-only").splitlines()
        if not staged or any(path not in self.PUBLISHABLE for path in staged):
            raise GitSafetyError("staged files are outside the discovery publication whitelist")
        self._command("commit", "-m", message)
        try:
            self._command("push", "origin", "HEAD:main")
        except Exception:
            self._command("reset", "--mixed", before_head)
            self._restore_index(index_backup)
            raise
        finally:
            if index_backup is not None:
                _, backup = index_backup
                if backup.exists():
                    backup.unlink()
        return True

    def _backup_index(self) -> tuple[Path, Path] | None:
        index = self._index_path()
        if index is None:
            return None
        descriptor, name = tempfile.mkstemp(prefix="dsh-discovery-index-", dir=index.parent)
        backup = Path(name)
        try:
            with os.fdopen(descriptor, "wb") as destination:
                if index.exists():
                    destination.write(index.read_bytes())
                destination.flush()
                os.fsync(destination.fileno())
        except Exception:
            backup.unlink(missing_ok=True)
            raise
        return index, backup

    def _restore_index(self, index_backup: tuple[Path, Path] | None) -> None:
        if index_backup is not None:
            index, backup = index_backup
            os.replace(backup, index)

    def _index_path(self) -> Path | None:
        result = self._command("rev-parse", "--git-path", "index", check=False)
        location = result.stdout.strip()
        if result.returncode != 0 or not location:
            return None
        index = Path(location)
        if not index.is_absolute():
            index = self.repo / index
        return index if index.exists() else None

    def _dirty_paths(self) -> list[str]:
        result = self._output("status", "--porcelain=v1")
        paths: list[str] = []
        for line in result.splitlines():
            if len(line) < 4:
                raise GitSafetyError("unparseable git status output")
            path = line[3:]
            if " -> " in path:
                raise GitSafetyError("renamed files are not permitted")
            paths.append(path)
        return paths

    def _is_controlled(self, path: str) -> bool:
        return path in self.PUBLISHABLE or path.startswith(self.GENERATED_PREFIXES)

    def _output(self, *arguments: str) -> str:
        return self._command(*arguments).stdout

    def _command(self, *arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
        result = self.runner(["git", *arguments], cwd=self.repo)
        if check and result.returncode != 0:
            detail = result.stderr.strip() or result.stdout.strip() or "git command failed"
            raise GitSafetyError(f"git {' '.join(arguments)}: {detail}")
        return result

    @staticmethod
    def _run(arguments: Sequence[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(arguments, cwd=cwd, text=True, capture_output=True, check=False)
