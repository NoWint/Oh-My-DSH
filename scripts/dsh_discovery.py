#!/usr/bin/env python3
"""Run the bounded DSH discovery pipeline safely."""
from __future__ import annotations
import argparse, fcntl, os, stat, sys
from datetime import datetime, timezone
from pathlib import Path
_REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(_REPOSITORY_ROOT) not in sys.path: sys.path.insert(0, str(_REPOSITORY_ROOT))
from scripts.dsh_discovery.catalog import CatalogEntry, update_readme
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


def run_discovery(repo: Path, env: dict[str, str], *, client=None, source_classes=None, validator=None, gitops=None) -> dict:
    config = DiscoveryConfig.from_env(env)
    client = client or HttpClient(timeout=config.request_timeout_seconds)
    credentials = SourceCredentials(github_token=config.github_token, gitlab_token=config.gitlab_token)
    classes = source_classes or (GitHubSource, GitLabSource, HackerNewsSource, LobstersSource, StackExchangeSource, RedditSource)
    results = [klass(client, credentials=credentials).discover() for klass in classes]
    hits = [hit.candidate for result in results for hit in result.hits]
    unique, _ = RepositoryValidator.deduplicate(hits)
    validator = validator or RepositoryValidator(client)
    validated = [validator.validate(candidate) for candidate in unique]
    entries = []
    for result in validated:
        metadata = result.candidate.metadata or {}
        if result.classification != EvidenceClass.VALIDATED: continue
        category, stars, english, chinese = metadata.get("category"), metadata.get("stars"), metadata.get("english_description"), metadata.get("chinese_description")
        if isinstance(category, str) and isinstance(stars, int) and stars >= 0 and isinstance(english, str) and isinstance(chinese, str) and english.strip() and chinese.strip():
            entries.append(CatalogEntry(result.candidate, result.classification.value, category, stars, english, chinese))
    readme = repo / "README.md"
    previous = Path.cwd()
    try:
        os.chdir(repo)
        readme_changed = update_readme(readme, entries, notice_date=datetime.now(timezone.utc).date().isoformat()) if entries else False
    finally: os.chdir(previous)
    pushed = False
    if readme_changed:
        pushed = (gitops or GitOps(repo)).commit_and_push("chore: update discovery catalog")
    return {"results": results, "readme_changed": readme_changed, "pushed": pushed, "validated": len(entries)}


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
                os.chdir(repo); save_report(Path("var/dsh-discovery-report.json"), DiscoveryReport(now, datetime.now(timezone.utc), "live", [{"source": r.source, "status": r.status.value, "hits": len(r.hits), "message": r.message} for r in outcome["results"]], {"readme_updated": outcome["readme_changed"], "pushed": outcome["pushed"], "state_updated": True, "report_written": True}))
            finally: os.chdir(previous)
            return 0
        finally: fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
if __name__ == "__main__": raise SystemExit(main())
