"""Safe, narrow Git operations for discovery publication."""

from __future__ import annotations

import subprocess
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
        dirty = self._dirty_paths()
        uncontrolled = [path for path in dirty if not self._is_controlled(path)]
        if uncontrolled:
            raise GitSafetyError("uncontrolled changes in worktree: " + ", ".join(uncontrolled))
        self._command("fetch", "origin", "main")
        result = self._command("merge-base", "--is-ancestor", "origin/main", "HEAD", check=False)
        if result.returncode != 0:
            raise GitSafetyError("local branch is behind origin/main; refusing non-fast-forward update")

    def commit_and_push(self, message: str) -> bool:
        self.prepare()
        dirty = self._dirty_paths()
        publishable = sorted(path for path in dirty if path in self.PUBLISHABLE)
        if not publishable:
            return False
        self._command("add", "--", *publishable)
        staged = self._output("diff", "--cached", "--name-only").splitlines()
        if not staged or any(path not in self.PUBLISHABLE for path in staged):
            raise GitSafetyError("staged files are outside the discovery publication whitelist")
        self._command("commit", "-m", message)
        self._command("push", "origin", "HEAD:main")
        return True

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
