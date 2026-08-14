# Task 2 Report

## Scope

Implemented the network source layer only. Foundation modules and tests were left untouched because they contain concurrent TASK1 changes.

## Source layer

- `HttpClient` uses stdlib `urllib`, a fixed user agent, finite timeout, and bounded retries for `429`, `403`, and `5xx` responses.
- Source adapters normalize results into `DiscoveryHit` and `SourceResult` values.
- Implemented GitHub repository search, GitLab public project search, Hacker News new/ask/show ID feeds, Lobsters RSS, Stack Exchange search, and OAuth-only Reddit handling.
- Reddit skips without `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET`; it does not scrape Reddit.
- Adapters enforce fixed page/request budgets and return source-level errors for malformed responses.
- Error messages contain exception types and generic source-unavailable text; response bodies and credentials are not logged.

## Tests

```sh
python3 -m unittest tests.test_sources -v
```

Result: 8 tests passed, covering normal JSON/XML responses, malformed responses, retryable rate limits, no-secret error messages, Reddit skip behavior, and request/page budgets.

The complete suite was also run. Six failures were present in concurrently modified TASK1 foundation tests; no foundation files were changed by this task.
