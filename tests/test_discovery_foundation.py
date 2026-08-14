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

    def test_github_accepts_only_canonical_repository_path(self) -> None:
        self.assertIsNone(normalize_repository_url("https://github.com/owner/repo/issues/1"))
        self.assertIsNone(normalize_repository_url("https://github.com/owner/repo/tree/main"))

    def test_gitlab_ignores_dash_page_paths_but_rejects_issue_pages(self) -> None:
        coordinate = RepositoryCoordinate(
            host="gitlab.com", owner="group/subgroup", repository="project"
        )
        self.assertEqual(
            normalize_repository_url("https://gitlab.com/group/subgroup/project/-/tree/main"),
            coordinate,
        )
        self.assertEqual(
            normalize_repository_url("https://gitlab.com/group/subgroup/project/-/"),
            coordinate,
        )
        self.assertIsNone(
            normalize_repository_url("https://gitlab.com/group/subgroup/project/-/issues/1")
        )

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
    def test_rejects_invalid_state_schema_and_version(self) -> None:
        invalid_payloads = (
            {"version": 2, "seen_fingerprints": [], "updated_at": "2026-08-14T00:00:00+00:00"},
            {"version": 1, "seen_fingerprints": "abc", "updated_at": "2026-08-14T00:00:00+00:00"},
            {"version": 1, "seen_fingerprints": ["ok", 3], "updated_at": "2026-08-14T00:00:00+00:00"},
            {"version": 1, "seen_fingerprints": [], "updated_at": "2026-08-14T00:00:00"},
        )
        for payload in invalid_payloads:
            with self.subTest(payload=payload):
                with tempfile.TemporaryDirectory() as directory:
                    path = Path(directory) / "state.json"
                    path.write_text(json.dumps(payload), encoding="utf-8")
                    with self.assertRaises(ValueError):
                        load_state(path)

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


class CandidateTests(unittest.TestCase):
    def test_metadata_is_copied_and_to_dict_returns_deep_copy(self) -> None:
        metadata = {"labels": ["dsh"], "nested": {"score": 1}}
        candidate = Candidate(coordinate=None, name="repo", metadata=metadata)
        metadata["labels"].append("mutated")
        exported = candidate.to_dict()
        exported["metadata"]["nested"]["score"] = 99
        self.assertEqual(candidate.metadata, {"labels": ["dsh"], "nested": {"score": 1}})
        self.assertNotEqual(exported, candidate.to_dict())


class ConfigValidationTests(unittest.TestCase):
    def test_rejects_non_positive_or_non_finite_timeout(self) -> None:
        for value in ("0", "-1", "nan", "inf", "-inf"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    DiscoveryConfig.from_env({"DSH_DISCOVERY_TIMEOUT_SECONDS": value})


if __name__ == "__main__":
    unittest.main()
