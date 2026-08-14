"""Environment-backed configuration for discovery jobs."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from .normalization import redact_token


@dataclass(frozen=True)
class DiscoveryConfig:
    state_path: Path = Path("var/dsh-discovery-state.json")
    github_token: str | None = None
    gitlab_token: str | None = None
    request_timeout_seconds: float = 20.0

    @classmethod
    def from_env(cls, environ: Mapping[str, str] | None = None) -> "DiscoveryConfig":
        env = os.environ if environ is None else environ
        timeout = float(env.get("DSH_DISCOVERY_TIMEOUT_SECONDS", "20"))
        return cls(
            state_path=Path(env.get("DSH_DISCOVERY_STATE_PATH", "var/dsh-discovery-state.json")),
            github_token=env.get("GITHUB_TOKEN") or None,
            gitlab_token=env.get("GITLAB_TOKEN") or None,
            request_timeout_seconds=timeout,
        )

    def redacted_tokens(self) -> dict[str, str | None]:
        return {
            "github_token": redact_token(self.github_token),
            "gitlab_token": redact_token(self.gitlab_token),
        }
