"""Strict, bounded updates to the established bilingual README catalog."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .models import Candidate
from .normalization import normalize_repository_url


class CatalogStructureError(ValueError):
    pass


@dataclass(frozen=True)
class CatalogEntry:
    candidate: Candidate
    classification: str
    category: str
    stars: int
    english_description: str
    chinese_description: str


_TABLE_HEADER = "| Stars | Repo | Description / 描述 |"
_NOTICE_EN = re.compile(r"(> \*\*Data source:\*\*.*?as of )\d{4}-\d{2}-\d{2}")
_NOTICE_CN = re.compile(r"(> \*\*数据来源：\*\*.*?截至 )\d{4}-\d{2}-\d{2}")


def update_readme(path: Path, entries: Iterable[CatalogEntry], *, notice_date: str | None = None) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    categories = _table_boundaries(lines)
    changed = False
    for entry in entries:
        _validate_entry(entry, categories)
        if _contains_coordinate(original, entry.candidate):
            continue
        insert_at = categories[entry.category]
        lines.insert(insert_at, _format_row(entry))
        categories = _table_boundaries(lines)
        changed = True
    updated = "".join(lines)
    if notice_date is not None:
        if not _NOTICE_EN.search(updated) or not _NOTICE_CN.search(updated):
            raise CatalogStructureError("automation notice structure drift")
        noticed = _NOTICE_EN.sub(r"\g<1>" + notice_date, updated, count=1)
        noticed = _NOTICE_CN.sub(r"\g<1>" + notice_date, noticed, count=1)
        changed = changed or noticed != updated
        updated = noticed
    if changed:
        path.write_text(updated, encoding="utf-8")
    return changed


def _table_boundaries(lines: list[str]) -> dict[str, int]:
    boundaries: dict[str, int] = {}
    heading: str | None = None
    for index, line in enumerate(lines):
        if line.startswith("## "):
            heading = line.rstrip("\n")
        elif line.rstrip("\n") == _TABLE_HEADER:
            if heading is None or index + 1 >= len(lines) or not lines[index + 1].startswith("|---"):
                raise CatalogStructureError("catalog table structure drift")
            end = index + 2
            while end < len(lines) and lines[end].startswith("|"):
                end += 1
            boundaries[heading] = end
    if not boundaries:
        raise CatalogStructureError("no catalog tables found")
    return boundaries


def _validate_entry(entry: CatalogEntry, categories: dict[str, int]) -> None:
    if entry.classification != "validated":
        raise CatalogStructureError("only validated candidates may be catalogued")
    if entry.candidate.coordinate is None:
        raise CatalogStructureError("candidate must have a canonical repository URL")
    if entry.category not in categories:
        raise CatalogStructureError("unknown category")
    if not entry.english_description.strip() or not entry.chinese_description.strip():
        raise CatalogStructureError("explicit bilingual descriptions are required")
    if " / " in entry.english_description or " / " in entry.chinese_description:
        raise CatalogStructureError("descriptions must be supplied as separate languages")


def _contains_coordinate(contents: str, candidate: Candidate) -> bool:
    assert candidate.coordinate is not None
    expected = candidate.coordinate.as_key()
    for url in re.findall(r"https?://[^)\s]+", contents):
        coordinate = normalize_repository_url(url)
        if coordinate is not None and coordinate.as_key() == expected:
            return True
    return False


def _format_row(entry: CatalogEntry) -> str:
    coordinate = entry.candidate.coordinate
    assert coordinate is not None
    url = f"https://{coordinate.host}/{coordinate.owner}/{coordinate.repository}"
    return (
        f"| ⭐ {entry.stars} | [{coordinate.owner}/{coordinate.repository}]({url}) | "
        f"{entry.english_description.strip()} / {entry.chinese_description.strip()} |\n"
    )
