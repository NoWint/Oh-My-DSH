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
            self.assertIn("截至 2026-08-14", contents)
            self.assertIn("Last updated: 2026-08-14", contents)
            self.assertIn("最后更新：2026-08-14", contents)
            self.assertLess(contents.index("[omdsh-dev/dsh-toolkit]"), contents.index("[acme/dsh-safe]"))

    def test_deduplicates_repeated_coordinate_within_one_update_batch(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            shutil.copyfile(Path(__file__).resolve().parents[1] / "README.md", path)
            first = CatalogEntry(Candidate(RepositoryCoordinate("github.com", "acme", "dsh-safe"), "dsh-safe"), "validated", "## 🔧 Utility Toolkit / 实用工具集", 1, "First explicit integration.", "第一个明确集成。")
            duplicate = CatalogEntry(Candidate(RepositoryCoordinate("github.com", "Acme", "DSH-SAFE"), "dsh-safe"), "validated", "## 🔧 Utility Toolkit / 实用工具集", 2, "Second explicit integration.", "第二个明确集成。")

            self.assertTrue(update_readme(path, (first, duplicate)))

            self.assertEqual(path.read_text(encoding="utf-8").count("https://github.com/acme/dsh-safe"), 1)

    def test_rejects_table_breaking_descriptions_and_invalid_notice_dates(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            shutil.copyfile(Path(__file__).resolve().parents[1] / "README.md", path)
            base = dict(candidate=Candidate(RepositoryCoordinate("github.com", "acme", "dsh-safe"), "dsh-safe"), classification="validated", category="## 🔧 Utility Toolkit / 实用工具集", stars=1, chinese_description="中文。")
            for description in ("has | delimiter", "line\nbreak", "line\rbreak", "control\x1fchar"):
                with self.subTest(description=repr(description)):
                    with self.assertRaises(CatalogStructureError):
                        update_readme(path, (CatalogEntry(english_description=description, **base),))
            for invalid_date in ("2026-8-14", "2026-02-30", "not-a-date"):
                with self.subTest(invalid_date=invalid_date):
                    with self.assertRaises(CatalogStructureError):
                        update_readme(path, (), notice_date=invalid_date)
    def test_rejects_non_integer_or_negative_stars_and_duplicate_notice_markers(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            shutil.copyfile(Path(__file__).resolve().parents[1] / "README.md", path)
            base = dict(candidate=Candidate(RepositoryCoordinate("github.com", "acme", "dsh-safe"), "dsh-safe"), classification="validated", category="## 🔧 Utility Toolkit / 实用工具集", english_description="English.", chinese_description="中文。")
            for stars in (True, False, -1, 1.5, "1", None):
                with self.subTest(stars=repr(stars)):
                    with self.assertRaises(CatalogStructureError):
                        update_readme(path, (CatalogEntry(stars=stars, **base),))
            contents = path.read_text(encoding="utf-8")
            path.write_text(contents + "\n*Last updated: 2026-08-14 · duplicate*\n", encoding="utf-8")
            with self.assertRaises(CatalogStructureError):
                update_readme(path, (), notice_date="2026-08-15")


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
