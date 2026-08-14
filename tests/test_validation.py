from __future__ import annotations

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
    def github_result(self, metadata, readme=None):
        responses = [FakeResponse(200, metadata)]
        if readme is not None:
            responses.append(FakeResponse(200, readme))
        candidate = Candidate(RepositoryCoordinate("github.com", "acme", "dsh-plugin"), "untrusted DSH plugin", "untrusted evidence")
        return RepositoryValidator(HttpClient(transport=FakeTransport(responses), max_retries=0)).validate(candidate)

    def test_validates_only_public_canonical_github_repository_with_affirmative_readme_integration(self):
        result = self.github_result(
            {"full_name": "acme/dsh-plugin", "archived": False, "fork": False, "private": False, "visibility": "public", "description": "Useful tool", "topics": ["tools"]},
            {"content": "# Plugin\n\nThis repository provides a DeepSeek Harness plugin integration."},
        )
        self.assertEqual(result.classification, EvidenceClass.VALIDATED)
        self.assertEqual(result.evidence, ("README",))

    def test_rejects_missing_or_malformed_public_status(self):
        base = {"full_name": "acme/dsh-plugin", "archived": False, "fork": False, "description": "DeepSeek Harness plugin integration", "topics": []}
        for patch in ({}, {"private": False}, {"private": "false", "visibility": "public"}, {"private": False, "visibility": "internal"}):
            with self.subTest(patch=patch):
                result = self.github_result(base | patch)
                self.assertEqual(result.classification, EvidenceClass.REJECTED)
                self.assertIn("public status", result.reason)

    def test_rejects_archived_fork_mirror_inaccessible_and_wrong_canonical_identity(self):
        base = {"full_name": "acme/dsh-plugin", "archived": False, "fork": False, "private": False, "visibility": "public", "topics": []}
        cases = (({"archived": True}, "archived"), ({"fork": True}, "fork"), ({"mirror_url": "https://x"}, "mirror"), ({"full_name": "other/repo"}, "identity"))
        for patch, reason in cases:
            with self.subTest(reason=reason):
                result = self.github_result(base | patch)
                self.assertEqual(result.classification, EvidenceClass.REJECTED)
                self.assertIn(reason, result.reason)
        inaccessible = RepositoryValidator(HttpClient(transport=FakeTransport([FakeResponse(404, {})]), max_retries=0)).validate(Candidate(RepositoryCoordinate("github.com", "acme", "dsh-plugin"), "repo"))
        self.assertEqual(inaccessible.classification, EvidenceClass.REJECTED)

    def test_candidate_fields_and_mere_or_negative_mentions_are_not_evidence(self):
        base = {"full_name": "acme/dsh-plugin", "archived": False, "fork": False, "private": False, "visibility": "public", "topics": []}
        for readme in (
            {"content": "A generic repository."},
            {"content": "DeepSeek Harness is not supported by this repository."},
            {"content": "Mentions a DeepSeek Harness plugin in a comparison."},
        ):
            with self.subTest(readme=readme):
                result = self.github_result(base, readme)
                self.assertEqual(result.classification, EvidenceClass.LEAD)

    def test_malformed_metadata_readme_topics_and_base64_reject_without_raising(self):
        candidate = Candidate(RepositoryCoordinate("github.com", "acme", "dsh-plugin"), "repo")
        malformed = (b"not-json", [], {"full_name": "acme/dsh-plugin", "private": False, "visibility": "public", "archived": False, "fork": False, "topics": "dsh"})
        for body in malformed:
            with self.subTest(body=body):
                result = RepositoryValidator(HttpClient(transport=FakeTransport([FakeResponse(200, body)]), max_retries=0)).validate(candidate)
                self.assertEqual(result.classification, EvidenceClass.REJECTED)
        metadata = {"full_name": "acme/dsh-plugin", "archived": False, "fork": False, "private": False, "visibility": "public", "topics": []}
        result = RepositoryValidator(HttpClient(transport=FakeTransport([FakeResponse(200, metadata), FakeResponse(200, {"encoding": "base64", "content": "%%%"})]), max_retries=0)).validate(candidate)
        self.assertEqual(result.classification, EvidenceClass.REJECTED)

    def test_gitlab_requires_public_status_canonical_identity_and_affirmative_metadata_evidence(self):
        candidate = Candidate(RepositoryCoordinate("gitlab.com", "group", "plugin"), "untrusted", "DeepSeek Harness plugin")
        payload = {"path_with_namespace": "group/plugin", "archived": False, "forked_from_project": None, "mirror": False, "visibility": "public", "description": "DeepSeek Harness plugin integration"}
        result = RepositoryValidator(HttpClient(transport=FakeTransport([FakeResponse(200, payload)]), max_retries=0)).validate(candidate)
        self.assertEqual(result.classification, EvidenceClass.PROBABLE)
        for patch in ({"visibility": None}, {"path_with_namespace": "other/plugin"}, {"description": "DeepSeek Harness is not supported"}):
            with self.subTest(patch=patch):
                rejected = RepositoryValidator(HttpClient(transport=FakeTransport([FakeResponse(200, payload | patch)]), max_retries=0)).validate(candidate)
                self.assertEqual(rejected.classification, EvidenceClass.REJECTED)

    def test_deduplicates_candidates_by_canonical_coordinate(self):
        first = Candidate(RepositoryCoordinate("github.com", "Acme", "Plugin"), "Plugin", source="github")
        duplicate = Candidate(RepositoryCoordinate("github.com", "acme", "plugin"), "Changed", source="gitlab")
        kept, duplicates = RepositoryValidator.deduplicate((first, duplicate))
        self.assertEqual(kept, (first,))
        self.assertEqual(duplicates, (duplicate,))


if __name__ == "__main__":
    unittest.main()
