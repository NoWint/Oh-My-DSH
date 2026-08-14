from __future__ import annotations

import json
import os
import unittest
from unittest.mock import patch

from scripts.dsh_discovery.sources import (
    FakeResponse,
    GitHubSource,
    HackerNewsSource,
    LobstersSource,
    RedditSource,
    SourceStatus,
    SourceCredentials,
    StackExchangeSource,
    GitLabSource,
    HttpClient,
)


class FakeTransport:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def __call__(self, request, timeout):
        self.calls.append((request, timeout))
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


class SourceTests(unittest.TestCase):
    def test_github_parses_normal_json(self):
        transport = FakeTransport([FakeResponse(200, {"items": [{"full_name": "acme/dsh-plugin", "name": "dsh-plugin", "description": "DeepSeek harness plugin", "html_url": "https://github.com/acme/dsh-plugin", "topics": ["dsh"]}]})])
        result = GitHubSource(HttpClient(transport=transport, max_retries=0), pages=1).discover()
        self.assertEqual(result.status, SourceStatus.OK)
        self.assertEqual(result.hits[0].candidate.coordinate.owner, "acme")
        self.assertEqual(result.hits[0].candidate.source, "github")

    def test_gitlab_malformed_json_is_source_error(self):
        transport = FakeTransport([FakeResponse(200, "not-json")])
        result = GitLabSource(HttpClient(transport=transport, max_retries=0), pages=1).discover()
        self.assertEqual(result.status, SourceStatus.ERROR)
        self.assertEqual(result.hits, ())

    def test_hacker_news_rate_limit_retries_once_without_secret_logging(self):
        transport = FakeTransport([FakeResponse(429, {"error": "token-secret-value"}), FakeResponse(200, [101]), FakeResponse(200, {"title": "DeepSeek Harness DSH plugin", "text": "release", "url": "https://example.test"}), FakeResponse(200, []), FakeResponse(200, [])])
        client = HttpClient(transport=transport, max_retries=1)
        result = HackerNewsSource(client).discover()
        self.assertEqual(result.status, SourceStatus.OK)
        self.assertEqual(len(transport.calls), 5)
        self.assertNotIn("token-secret-value", result.message)

    def test_lobsters_parses_rss(self):
        rss = b'<rss><channel><item><title>DSH plugin</title><description>DeepSeek harness</description><link>https://lobste.rs/s/abc</link><guid>abc</guid></item></channel></rss>'
        result = LobstersSource(HttpClient(transport=FakeTransport([FakeResponse(200, rss)]), max_retries=0)).discover()
        self.assertEqual(result.status, SourceStatus.OK)
        self.assertEqual(result.hits[0].candidate.name, "DSH plugin")

    def test_stack_exchange_parses_json(self):
        payload = {"items": [{"title": "DeepSeek harness", "link": "https://stackoverflow.com/q/1", "question_id": 1, "body_markdown": "plugin"}]}
        result = StackExchangeSource(HttpClient(transport=FakeTransport([FakeResponse(200, payload)]), max_retries=0), pages=1).discover()
        self.assertEqual(result.status, SourceStatus.OK)
        self.assertEqual(result.hits[0].candidate.source, "stackexchange")

    def test_reddit_skips_without_official_oauth_config(self):
        with patch.dict(os.environ, {}, clear=True):
            result = RedditSource(HttpClient(transport=FakeTransport([]))).discover()
        self.assertEqual(result.status, SourceStatus.SKIPPED)
        self.assertIn("OAuth", result.message)

    def test_budgets_limit_requests_and_pages(self):
        transport = FakeTransport([FakeResponse(200, {"items": []})] * 10)
        result = StackExchangeSource(HttpClient(transport=transport, max_retries=0), pages=2).discover()
        self.assertEqual(result.status, SourceStatus.OK)
        self.assertEqual(len(transport.calls), 2)

    def test_http_client_rejects_non_positive_or_non_finite_timeout(self):
        for timeout in (0, -1, float("nan"), float("inf"), float("-inf")):
            with self.subTest(timeout=timeout):
                with self.assertRaises(ValueError):
                    HttpClient(timeout=timeout)

    def test_http_client_retries_only_retryable_statuses(self):
        transport = FakeTransport([FakeResponse(403, {"error": "secret"}, {"X-RateLimit-Remaining": "0"})] * 4)
        result = GitHubSource(HttpClient(transport=transport, max_retries=2)).discover()
        self.assertEqual(result.status, SourceStatus.ERROR)
        self.assertEqual(len(transport.calls), 2)
        self.assertNotIn("secret", result.message)

    def test_source_budget_caps_retries_as_physical_attempts(self):
        transport = FakeTransport([FakeResponse(429, {}, {"Retry-After": "1"})] * 4)
        delays = []
        result = GitHubSource(
            HttpClient(transport=transport, max_retries=2, sleep=delays.append),
            pages=2,
        ).discover()
        self.assertEqual(result.status, SourceStatus.ERROR)
        self.assertEqual(len(transport.calls), 2)
        self.assertEqual(delays, [1.0])

    def test_403_retries_only_with_rate_limit_evidence(self):
        plain = FakeTransport([FakeResponse(403, {})])
        result = GitHubSource(HttpClient(transport=plain, max_retries=2), pages=1).discover()
        self.assertEqual(result.status, SourceStatus.ERROR)
        self.assertEqual(len(plain.calls), 1)

        limited = FakeTransport([FakeResponse(403, {}, {"X-RateLimit-Remaining": "0"}), FakeResponse(200, {"items": []})])
        result = GitHubSource(HttpClient(transport=limited, max_retries=1), pages=1).discover()
        self.assertEqual(result.status, SourceStatus.OK)
        self.assertEqual(len(limited.calls), 2)

    def test_all_sources_filter_irrelevant_hits_and_hn_fetches_metadata(self):
        github = GitHubSource(HttpClient(transport=FakeTransport([FakeResponse(200, {"items": [{"name": "dsh-plugin", "description": "DeepSeek harness plugin", "html_url": "https://github.com/a/dsh-plugin"}, {"name": "dsh", "description": "data helper", "html_url": "https://github.com/a/dsh"}]})]), max_retries=0), pages=1)
        self.assertEqual([hit.candidate.name for hit in github.discover().hits], ["dsh-plugin"])

        hn_transport = FakeTransport([FakeResponse(200, [1]), FakeResponse(200, {"title": "DeepSeek Harness DSH plugin", "text": "release", "url": "https://example.test"}), FakeResponse(200, []), FakeResponse(200, [])])
        result = HackerNewsSource(HttpClient(transport=hn_transport, max_retries=0)).discover()
        self.assertEqual([hit.candidate.name for hit in result.hits], ["DeepSeek Harness DSH plugin"])
        self.assertEqual(len(hn_transport.calls), 4)

    def test_credentials_are_injected_without_environment_lookup(self):
        transport = FakeTransport([FakeResponse(200, {"items": []})])
        source = GitHubSource(
            HttpClient(transport=transport, max_retries=0), pages=1,
            credentials=SourceCredentials(github_token="injected-token"),
        )
        with patch.dict(os.environ, {"GITHUB_TOKEN": "environment-token"}, clear=True):
            source.discover()
        self.assertEqual(transport.calls[0][0].get_header("Authorization"), "Bearer injected-token")

    def test_query_budget_is_removed_in_favor_of_explicit_request_budget(self):
        self.assertFalse(hasattr(GitHubSource, "query_budget"))
