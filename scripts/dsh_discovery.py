#!/usr/bin/env python3
"""Run the bounded DSH discovery pipeline safely."""
from __future__ import annotations
import argparse, fcntl, os, stat, sys, time
from datetime import datetime, timezone
from pathlib import Path
_REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(_REPOSITORY_ROOT) not in sys.path: sys.path.insert(0, str(_REPOSITORY_ROOT))
from scripts.dsh_discovery.catalog import CatalogEntry, render_readme
from scripts.dsh_discovery.config import DiscoveryConfig
from scripts.dsh_discovery.gitops import GitOps
from scripts.dsh_discovery.report import DiscoveryReport, save_report
from scripts.dsh_discovery.sources import (GitHubSource, GitLabSource, HackerNewsSource, LobstersSource, RedditSource, SourceCredentials, StackExchangeSource, HttpClient)
from scripts.dsh_discovery.state import DiscoveryState, load_state, save_state
from scripts.dsh_discovery.validation import EvidenceClass, RepositoryValidator
from scripts.dsh_discovery.normalization import candidate_fingerprint


def _load_env(path: Path) -> dict[str, str]:
    mode = stat.S_IMODE(path.stat().st_mode)
    if not stat.S_ISREG(path.stat().st_mode) or mode != 0o600: raise ValueError("environment file must be a regular owner-only file with mode 0600")
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"): continue
        key, separator, value = line.partition("=")
        if not separator or not key.replace("_", "").isalnum(): raise ValueError("invalid environment file entry")
        values[key] = value
    return values


_CATALOG_CATEGORY = "## 🔧 Utility Toolkit / 实用工具集"


def _catalog_entry(result):
    if result.classification != EvidenceClass.VALIDATED:
        return None
    metadata = result.verified_metadata or {}
    stars = metadata.get("stars")
    description = metadata.get("description")
    if not isinstance(stars, int) or isinstance(stars, bool) or stars < 0 or not isinstance(description, str):
        return None
    english, separator, chinese = description.partition(" / ")
    if not separator or not english.strip() or not chinese.strip() or " / " in chinese:
        return None
    return CatalogEntry(result.candidate, result.classification.value, _CATALOG_CATEGORY, stars, english, chinese)


def run_discovery(repo: Path, env: dict[str, str], *, client=None, source_classes=None, validator=None, gitops=None, monotonic=time.monotonic) -> dict:
    config = DiscoveryConfig.from_env(env)
    client = client or HttpClient(timeout=config.request_timeout_seconds)
    credentials = SourceCredentials(github_token=config.github_token, gitlab_token=config.gitlab_token)
    classes = source_classes or (GitHubSource, GitLabSource, HackerNewsSource, LobstersSource, StackExchangeSource, RedditSource)
    results = [klass(client, credentials=credentials).discover() for klass in classes]
    hits = [hit.candidate for result in results for hit in result.hits]
    unique, _ = RepositoryValidator.deduplicate(hits)
    validator = validator or RepositoryValidator(client)
    deadline = monotonic() + config.validation_deadline_seconds
    validated = []
    validation_deadline_skipped = 0
    for index, candidate in enumerate(unique[:config.max_validation_candidates]):
        if monotonic() >= deadline:
            validation_deadline_skipped = len(unique[:config.max_validation_candidates]) - index
            break
        validated.append(validator.validate(candidate))
    validation_budget_skipped = max(0, len(unique) - config.max_validation_candidates)
    entries = [entry for result in validated if (entry := _catalog_entry(result)) is not None]
    readme_changed = False
    pushed = False
    if entries:
        readme = repo / "README.md"
        original = readme.read_text(encoding="utf-8")
        updated = render_readme(original, entries, notice_date=datetime.now(timezone.utc).date().isoformat())
        readme_changed = updated != original
        if readme_changed:
            publisher = gitops or GitOps(repo)
            publisher.prepare()
            try:
                readme.write_text(updated, encoding="utf-8")
                pushed = publisher.commit_and_push("chore: update discovery catalog")
            except Exception:
                readme.write_text(original, encoding="utf-8")
                raise
    return {"results": results, "readme_changed": readme_changed, "pushed": pushed, "validated": len(entries), "validation_budget_skipped": validation_budget_skipped, "validation_deadline_skipped": validation_deadline_skipped}


def main(argv: list[str] | None = None, *, environ: dict[str, str] | None = None, source_classes=None) -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--repo", type=Path, default=Path.cwd()); parser.add_argument("--dry-run", action="store_true"); parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv); env = dict(os.environ if environ is None else environ); repo = args.repo.resolve()
    if args.dry_run or args.fixtures: return 0
    env_path = Path(env.get("DSH_DISCOVERY_ENV_FILE", str(repo / ".env")))
    if env_path.exists(): env.update(_load_env(env_path))
    now = datetime.now(timezone.utc); lock_path = repo / "var/dsh-discovery.lock"; lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+") as lock:
        try: fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError: return 0
        try:
            outcome = run_discovery(repo, env, source_classes=source_classes)
            save_state(repo / "var/dsh-discovery-state.json", DiscoveryState(updated_at=now))
            previous = Path.cwd()
            try:
                os.chdir(repo); save_report(Path("var/dsh-discovery-report.json"), DiscoveryReport(now, datetime.now(timezone.utc), "live", [{"source": r.source, "status": r.status.value, "hits": len(r.hits), "message": r.message, "skipped_hits": getattr(r, "skipped_hits", 0)} for r in outcome["results"]], {"readme_updated": outcome["readme_changed"], "pushed": outcome["pushed"], "state_updated": True, "report_written": True, "validation_budget_skipped": outcome["validation_budget_skipped"], "validation_deadline_skipped": outcome["validation_deadline_skipped"]}))
            finally: os.chdir(previous)
            return 0
        finally: fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
if __name__ == "__main__": raise SystemExit(main())
