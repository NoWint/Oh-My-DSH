"""Tests for the dependency-free discovery foundation."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from scripts.dsh_discovery.config import DiscoveryConfig
from scripts.dsh_discovery.models import Candidate, RepositoryCoordinate
from scripts.dsh_discovery.normalization import (
    candidate_fingerprint,
    is_dsh_relevant,
    normalize_repository_url,
    redact_token,
)
from scripts.dsh_discovery.state import DiscoveryState, load_state, save_state


class ConfigTests(unittest.TestCase):
    def test_from_env_uses_defaults_and_redacts_secrets(self) -> None:
        config = DiscoveryConfig.from_env(
            {
                "DSH_DISCOVERY_STATE_PATH": "var/discovery.json",
                "GITHUB_TOKEN": "ghp_abcdefghijklmnopqrstuvwxyz",
            }
        )

        self.assertEqual(config.state_path, Path("var/discovery.json"))
        self.assertEqual(config.github_token, "ghp_abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(config.gitlab_token, None)
        self.assertEqual(config.redacted_tokens()["github_token"], "ghp_…wxyz")


class NormalizationTests(unittest.TestCase):
    def test_normalizes_supported_github_and_gitlab_urls(self) -> None:
        self.assertEqual(
            normalize_repository_url("https://github.com/Owner/Repo.git/?tab=readme#top"),
            RepositoryCoordinate(host="github.com", owner="Owner", repository="Repo"),
        )
        self.assertEqual(
            normalize_repository_url("git@gitlab.com:group/subgroup/project.git"),
            RepositoryCoordinate(
                host="gitlab.com", owner="group/subgroup", repository="project"
            ),
        )

    def test_rejects_unsupported_or_incomplete_repository_urls(self) -> None:
        self.assertIsNone(normalize_repository_url("https://example.com/org/repo"))
        self.assertIsNone(normalize_repository_url("https://github.com/owner"))

    def test_redacts_short_and_long_tokens(self) -> None:
        self.assertEqual(redact_token(None), None)
        self.assertEqual(redact_token("abc"), "***")
        self.assertEqual(redact_token("abcdefghijklmnop"), "abcd…mnop")

    def test_requires_exact_or_strong_deepseek_harness_evidence(self) -> None:
        self.assertTrue(is_dsh_relevant(name="dsh-tool", description="A DSH plugin"))
        self.assertTrue(
            is_dsh_relevant(
                name="workflow-helper",
                description="Extension for DeepSeek Harness users",
            )
        )
        self.assertFalse(is_dsh_relevant(name="dsh", description="Data science helper"))
        self.assertFalse(is_dsh_relevant(name="dsh-backup", description="Daily shell helper"))

    def test_fingerprint_is_stable_for_equivalent_repository_forms(self) -> None:
        first = Candidate(
            coordinate=normalize_repository_url("https://github.com/Owner/Repo.git"),
            name="Repo",
            description="A plugin",
            source="github",
        )
        second = Candidate(
            coordinate=normalize_repository_url("git@github.com:Owner/Repo.git"),
            name="Changed name",
            description="Changed description",
            source="gitlab",
        )

        self.assertEqual(candidate_fingerprint(first), candidate_fingerprint(second))


class StateTests(unittest.TestCase):
    def test_round_trips_state_with_atomic_replace(self) -> None:
        state = DiscoveryState(
            seen_fingerprints={"abc123"},
            updated_at=datetime(2026, 8, 14, tzinfo=timezone.utc),
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            save_state(path, state)

            self.assertFalse(list(Path(directory).glob(".state.json.*.tmp")))
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["version"], 1)
            self.assertEqual(load_state(path), state)

    def test_missing_state_returns_empty_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(load_state(Path(directory) / "missing.json"), DiscoveryState())


if __name__ == "__main__":
    unittest.main()
