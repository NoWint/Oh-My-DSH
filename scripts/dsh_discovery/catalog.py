"""Strict, bounded updates to the established bilingual README catalog."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
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
_FOOTER_EN = re.compile(r"(\*Last updated: )\d{4}-\d{2}-\d{2}")
_FOOTER_CN = re.compile(r"(\*最后更新：)\d{4}-\d{2}-\d{2}")
_CONTROL = re.compile(r"[|\x00-\x1f\x7f]")


def render_readme(original: str, entries: Iterable[CatalogEntry], *, notice_date: str | None = None) -> str:
    """Produce a catalog update without mutating the README on disk."""
    lines = original.splitlines(keepends=True)
    categories = _table_boundaries(lines)
    changed = False
    existing_coordinates = _catalog_coordinates(original)
    for entry in entries:
        _validate_entry(entry, categories)
        assert entry.candidate.coordinate is not None
        coordinate_key = entry.candidate.coordinate.as_key()
        if coordinate_key in existing_coordinates:
            continue
        insert_at = categories[entry.category]
        lines.insert(insert_at, _format_row(entry))
        existing_coordinates.add(coordinate_key)
        categories = _table_boundaries(lines)
        changed = True
    updated = "".join(lines)
    if notice_date is not None:
        _validate_notice_date(notice_date)
        notice_patterns = (_NOTICE_EN, _NOTICE_CN, _FOOTER_EN, _FOOTER_CN)
        if any(len(pattern.findall(updated)) != 1 for pattern in notice_patterns):
            raise CatalogStructureError("automation notice structure drift")
        noticed = updated
        for pattern in notice_patterns:
            noticed = pattern.sub(r"\g<1>" + notice_date, noticed, count=1)
        changed = changed or noticed != updated
        updated = noticed
    return updated


def update_readme(path: Path, entries: Iterable[CatalogEntry], *, notice_date: str | None = None) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = render_readme(original, entries, notice_date=notice_date)
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


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
    if not isinstance(entry.stars, int) or isinstance(entry.stars, bool) or entry.stars < 0:
        raise CatalogStructureError("stars must be a non-negative integer")
    if not entry.english_description.strip() or not entry.chinese_description.strip():
        raise CatalogStructureError("explicit bilingual descriptions are required")
    if " / " in entry.english_description or " / " in entry.chinese_description:
        raise CatalogStructureError("descriptions must be supplied as separate languages")
    if _CONTROL.search(entry.english_description) or _CONTROL.search(entry.chinese_description):
        raise CatalogStructureError("descriptions contain table-breaking characters")


def _validate_notice_date(value: str) -> None:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise CatalogStructureError("notice date must be ISO YYYY-MM-DD")
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise CatalogStructureError("notice date must be ISO YYYY-MM-DD") from exc


def _catalog_coordinates(contents: str) -> set[str]:
    coordinates: set[str] = set()
    for url in re.findall(r"https?://[^)\s]+", contents):
        coordinate = normalize_repository_url(url)
        if coordinate is not None:
            coordinates.add(coordinate.as_key())
    return coordinates


def _format_row(entry: CatalogEntry) -> str:
    coordinate = entry.candidate.coordinate
    assert coordinate is not None
    url = f"https://{coordinate.host}/{coordinate.owner}/{coordinate.repository}"
    return (
        f"| ⭐ {entry.stars} | [{coordinate.owner}/{coordinate.repository}]({url}) | "
        f"{entry.english_description.strip()} / {entry.chinese_description.strip()} |\n"
    )
