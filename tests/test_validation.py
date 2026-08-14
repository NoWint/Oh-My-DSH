from __future__ import annotations

import json
import unittest

from scripts.dsh_discovery.models import Candidate, RepositoryCoordinate
from scripts.dsh_discovery.sources import FakeResponse, HttpClient
from scripts.dsh_discovery.validation import EvidenceClass, RepositoryValidator


class FakeTransport:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def __call__(self, request, timeout):
        self.calls.append(request.full_url)
        return self.responses.pop(0)


class RepositoryValidationTests(unittest.TestCase):
    def test_validates_public_github_repository_with_explicit_integration_evidence(self):
        transport = FakeTransport([
            FakeResponse(200, {
                "full_name": "acme/dsh-plugin", "archived": False, "fork": False,
                "private": False, "description": "Useful tool", "topics": ["tools"],
                "html_url": "https://github.com/acme/dsh-plugin",
            }),
            FakeResponse(200, {"content": "# dsh-plugin\n\nInstall as a DeepSeek Harness plugin."}),
        ])
        candidate = Candidate(RepositoryCoordinate("github.com", "acme", "dsh-plugin"), "dsh-plugin")

        result = RepositoryValidator(HttpClient(transport=transport, max_retries=0)).validate(candidate)

        self.assertEqual(result.classification, EvidenceClass.VALIDATED)
        self.assertEqual(result.candidate.coordinate.as_key(), "github.com/acme/dsh-plugin")
        self.assertTrue(result.evidence)

    def test_rejects_archived_fork_mirror_and_inaccessible_repositories(self):
        cases = (
            ({"archived": True, "fork": False, "private": False}, "archived"),
            ({"archived": False, "fork": True, "private": False}, "fork"),
            ({"archived": False, "fork": False, "private": False, "mirror_url": "https://x"}, "mirror"),
        )
        for metadata, reason in cases:
            with self.subTest(reason=reason):
                candidate = Candidate(RepositoryCoordinate("github.com", "acme", "repo"), "repo")
                result = RepositoryValidator(HttpClient(transport=FakeTransport([FakeResponse(200, metadata)]), max_retries=0)).validate(candidate)
                self.assertEqual(result.classification, EvidenceClass.REJECTED)
                self.assertIn(reason, result.reason)
        inaccessible = RepositoryValidator(HttpClient(transport=FakeTransport([FakeResponse(404, {})]), max_retries=0)).validate(
            Candidate(RepositoryCoordinate("github.com", "acme", "repo"), "repo")
        )
        self.assertEqual(inaccessible.classification, EvidenceClass.REJECTED)
        self.assertIn("inaccessible", inaccessible.reason)

    def test_classifies_metadata_without_explicit_integration_as_lead(self):
        transport = FakeTransport([FakeResponse(200, {
            "archived": False, "fork": False, "private": False,
            "description": "A generic collection of utilities", "topics": ["utilities"],
        })])
        candidate = Candidate(RepositoryCoordinate("github.com", "acme", "repo"), "repo")

        result = RepositoryValidator(HttpClient(transport=transport, max_retries=0)).validate(candidate)

        self.assertEqual(result.classification, EvidenceClass.LEAD)
        self.assertIn("no explicit", result.reason)

    def test_deduplicates_candidates_by_canonical_coordinate(self):
        first = Candidate(RepositoryCoordinate("github.com", "Acme", "Plugin"), "Plugin", source="github")
        duplicate = Candidate(RepositoryCoordinate("github.com", "acme", "plugin"), "Changed", source="gitlab")

        kept, duplicates = RepositoryValidator.deduplicate((first, duplicate))

        self.assertEqual(kept, (first,))
        self.assertEqual(duplicates, (duplicate,))


if __name__ == "__main__":
    unittest.main()
