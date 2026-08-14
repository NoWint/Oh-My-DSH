from __future__ import annotations

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.dsh_discovery.models import Candidate, RepositoryCoordinate
from scripts.dsh_discovery.sources import DiscoveryHit, SourceResult, SourceStatus
from scripts.dsh_discovery.validation import EvidenceClass, ValidationResult


def _load_cli_module():
    path = Path(__file__).parents[1] / "scripts/dsh_discovery.py"
    spec = importlib.util.spec_from_file_location("dsh_discovery_pipeline", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def _candidate(number: int) -> Candidate:
    return Candidate(
        RepositoryCoordinate("github.com", "acme", f"dsh-plugin-{number}"),
        f"dsh-plugin-{number}",
        "Raw source description only.",
        "fake",
    )


class _FakeSource:
    candidates: tuple[Candidate, ...] = ()

    def __init__(self, client, credentials=None):
        pass

    def discover(self):
        return SourceResult(
            "fake",
            SourceStatus.OK,
            tuple(DiscoveryHit(candidate) for candidate in self.candidates),
        )


class _Validator:
    def __init__(self, results):
        self.results = dict(results)
        self.calls = []

    def validate(self, candidate, *, deadline=None, monotonic=None):
        self.calls.append(candidate)
        return self.results[candidate.coordinate.as_key()]


class DiscoveryPipelineTests(unittest.TestCase):
    def setUp(self):
        _FakeSource.candidates = ()
        self.module = _load_cli_module()

    def repository(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        repo = Path(directory.name)
        shutil.copyfile(Path(__file__).parents[1] / "README.md", repo / "README.md")
        return repo

    def test_validated_candidate_with_verified_bilingual_metadata_updates_readme(self):
        candidate = _candidate(1)
        _FakeSource.candidates = (candidate,)
        validator = _Validator({
            candidate.coordinate.as_key(): ValidationResult(
                candidate,
                EvidenceClass.VALIDATED,
                "explicit DSH integration evidence",
                verified_metadata={
                    "category": "## 🔧 Utility Toolkit / 实用工具集",
                    "stars": 42,
                    "description": "Verified DeepSeek Harness plugin. / 已验证的 DeepSeek Harness 插件。",
                },
            ),
        })

        class GitOps:
            def prepare(self):
                pass

            def commit_and_push(self, message):
                return True

        repo = self.repository()
        outcome = self.module.run_discovery(repo, {}, source_classes=(_FakeSource,), validator=validator, gitops=GitOps())

        self.assertTrue(outcome["readme_changed"])
        self.assertTrue(outcome["pushed"])
        self.assertIn("Verified DeepSeek Harness plugin. / 已验证的 DeepSeek Harness 插件。", (repo / "README.md").read_text(encoding="utf-8"))

    def test_catalogue_rejects_non_cjk_chinese_description_part(self):
        candidate = _candidate(1)
        _FakeSource.candidates = (candidate,)
        validator = _Validator({candidate.coordinate.as_key(): ValidationResult(candidate, EvidenceClass.VALIDATED, "verified", verified_metadata={"stars": 1, "description": "foo / bar"})})

        class RecordingGitOps:
            def prepare(self):
                pass

            def commit_and_push(self, message):
                return True

        repo = self.repository()
        outcome = self.module.run_discovery(repo, {}, source_classes=(_FakeSource,), validator=validator, gitops=RecordingGitOps())

        self.assertEqual(outcome["validated"], 0)
        self.assertFalse(outcome["readme_changed"])

    def test_inflight_validation_request_uses_only_remaining_deadline_budget(self):
        from scripts.dsh_discovery.sources import HttpClient

        candidate = _candidate(1)
        _FakeSource.candidates = (candidate,)
        now = [0.0]
        timeouts = []

        def slow_transport(request, timeout):
            timeouts.append(timeout)
            now[0] += timeout
            raise TimeoutError("slow response")

        outcome = self.module.run_discovery(
            self.repository(),
            {},
            source_classes=(_FakeSource,),
            client=HttpClient(transport=slow_transport, timeout=500, max_retries=2),
            monotonic=lambda: now[0],
        )

        self.assertEqual(timeouts, [120.0])
        self.assertEqual(now[0], 120.0)
        self.assertEqual(outcome["validation_deadline_skipped"], 0)

    def test_validation_budget_caps_global_candidates_and_records_skipped_count(self):
        candidates = tuple(_candidate(number) for number in range(25))
        _FakeSource.candidates = candidates
        validator = _Validator({
            candidate.coordinate.as_key(): ValidationResult(candidate, EvidenceClass.LEAD, "not catalogued")
            for candidate in candidates
        })

        outcome = self.module.run_discovery(self.repository(), {}, source_classes=(_FakeSource,), validator=validator)

        self.assertEqual(len(validator.calls), 20)
        self.assertEqual(outcome["validation_budget_skipped"], 5)
        self.assertEqual(outcome["validation_deadline_skipped"], 0)

    def test_validation_deadline_stops_global_validation_and_records_skipped_count(self):
        candidates = tuple(_candidate(number) for number in range(3))
        _FakeSource.candidates = candidates
        validator = _Validator({
            candidate.coordinate.as_key(): ValidationResult(candidate, EvidenceClass.LEAD, "not catalogued")
            for candidate in candidates
        })
        clock = iter((0.0, 0.0, 121.0))

        outcome = self.module.run_discovery(self.repository(), {}, source_classes=(_FakeSource,), validator=validator, monotonic=lambda: next(clock))

        self.assertEqual(len(validator.calls), 1)
        self.assertEqual(outcome["validation_budget_skipped"], 0)
        self.assertEqual(outcome["validation_deadline_skipped"], 2)

    def test_lobsters_rss_cap_records_skipped_items(self):
        from scripts.dsh_discovery.sources import FakeResponse, HttpClient, LobstersSource

        items = "".join(
            f"<item><title>DSH plugin {number}</title><description>DeepSeek Harness plugin</description><link>https://lobste.rs/s/{number}</link></item>"
            for number in range(25)
        )
        result = LobstersSource(HttpClient(transport=lambda request, timeout: FakeResponse(200, f"<rss><channel>{items}</channel></rss>".encode()), max_retries=0)).discover()

        self.assertEqual(len(result.hits), 20)
        self.assertEqual(result.skipped_hits, 5)

    def test_publication_preflight_refusal_leaves_readme_byte_identical(self):
        candidate = _candidate(1)
        _FakeSource.candidates = (candidate,)
        validator = _Validator({candidate.coordinate.as_key(): ValidationResult(candidate, EvidenceClass.VALIDATED, "verified", verified_metadata={"category": "## 🔧 Utility Toolkit / 实用工具集", "stars": 1, "description": "English. / 中文。"})})

        class RefusingGitOps:
            def prepare(self):
                raise RuntimeError("publication refused")

        repo = self.repository()
        before = (repo / "README.md").read_bytes()
        with self.assertRaisesRegex(RuntimeError, "publication refused"):
            self.module.run_discovery(repo, {}, source_classes=(_FakeSource,), validator=validator, gitops=RefusingGitOps())
        self.assertEqual((repo / "README.md").read_bytes(), before)

    def test_push_refusal_restores_readme_byte_identical(self):
        candidate = _candidate(1)
        _FakeSource.candidates = (candidate,)
        validator = _Validator({candidate.coordinate.as_key(): ValidationResult(candidate, EvidenceClass.VALIDATED, "verified", verified_metadata={"category": "## 🔧 Utility Toolkit / 实用工具集", "stars": 1, "description": "English. / 中文。"})})

        class RefusingGitOps:
            def prepare(self):
                pass

            def commit_and_push(self, message):
                raise RuntimeError("push refused")

        repo = self.repository()
        before = (repo / "README.md").read_bytes()
        with self.assertRaisesRegex(RuntimeError, "push refused"):
            self.module.run_discovery(repo, {}, source_classes=(_FakeSource,), validator=validator, gitops=RefusingGitOps())
        self.assertEqual((repo / "README.md").read_bytes(), before)

    def test_commit_and_push_false_restores_readme_byte_identical(self):
        candidate = _candidate(1)
        _FakeSource.candidates = (candidate,)
        validator = _Validator({candidate.coordinate.as_key(): ValidationResult(candidate, EvidenceClass.VALIDATED, "verified", verified_metadata={"stars": 1, "description": "English. / 中文。"})})

        class RefusingGitOps:
            def prepare(self):
                pass

            def commit_and_push(self, message):
                return False

        repo = self.repository()
        before = (repo / "README.md").read_bytes()
        outcome = self.module.run_discovery(repo, {}, source_classes=(_FakeSource,), validator=validator, gitops=RefusingGitOps())

        self.assertEqual((repo / "README.md").read_bytes(), before)
        self.assertFalse(outcome["readme_changed"])
        self.assertFalse(outcome["pushed"])


if __name__ == "__main__":
    unittest.main()
