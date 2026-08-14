from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.dsh_discovery.models import Candidate, RepositoryCoordinate
from scripts.dsh_discovery.catalog import CatalogEntry, CatalogStructureError, update_readme


class ReadmeUpdaterTests(unittest.TestCase):
    def test_inserts_only_validated_candidate_in_existing_category_table_and_updates_notice(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            fixture = Path(__file__).resolve().parents[1] / "README.md"
            shutil.copyfile(fixture, path)
            entry = CatalogEntry(
                candidate=Candidate(RepositoryCoordinate("github.com", "acme", "dsh-safe"), "dsh-safe"),
                classification="validated",
                category="## 🔧 Utility Toolkit / 实用工具集",
                stars=12,
                english_description="Safe utility integration for DeepSeek Harness.",
                chinese_description="用于 DeepSeek Harness 的安全实用工具集成。",
            )

            changed = update_readme(path, (entry,), notice_date="2026-08-14")

            contents = path.read_text(encoding="utf-8")
            self.assertTrue(changed)
            self.assertIn("[acme/dsh-safe](https://github.com/acme/dsh-safe)", contents)
            self.assertIn("Safe utility integration for DeepSeek Harness. / 用于 DeepSeek Harness 的安全实用工具集成。", contents)
            self.assertIn("as of 2026-08-14", contents)
            self.assertLess(contents.index("[omdsh-dev/dsh-toolkit]"), contents.index("[acme/dsh-safe]"))

    def test_rejects_unvalidated_missing_description_unknown_category_and_existing_url(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            shutil.copyfile(Path(__file__).resolve().parents[1] / "README.md", path)
            base = dict(candidate=Candidate(RepositoryCoordinate("github.com", "acme", "dsh-safe"), "dsh-safe"), category="## 🔧 Utility Toolkit / 实用工具集", stars=1, english_description="English.", chinese_description="中文。")
            with self.assertRaises(CatalogStructureError):
                update_readme(path, (CatalogEntry(classification="lead", **base),))
            with self.assertRaises(CatalogStructureError):
                update_readme(path, (CatalogEntry(classification="validated", category="## Unknown", **{key: value for key, value in base.items() if key != "category"}),))
            with self.assertRaises(CatalogStructureError):
                update_readme(path, (CatalogEntry(classification="validated", english_description="", **{key: value for key, value in base.items() if key != "english_description"}),))
            duplicate = CatalogEntry(candidate=Candidate(RepositoryCoordinate("github.com", "omdsh-dev", "dsh-toolkit"), "dsh-toolkit"), classification="validated", category="## 🔧 Utility Toolkit / 实用工具集", stars=10, english_description="English.", chinese_description="中文。")
            self.assertFalse(update_readme(path, (duplicate,)))


if __name__ == "__main__":
    unittest.main()
