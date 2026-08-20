from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.record_utils import FrontMatterError, parse_front_matter, render_catalog


class FrontMatterTests(unittest.TestCase):
    def test_parses_supported_scalar_types(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "record.md"
            path.write_text(
                "---\ncount: 2\nactive: true\nitems: [\"BUF\"]\nnothing: null\n---\nBody\n",
                encoding="utf-8",
            )

            metadata, body = parse_front_matter(path)

        self.assertEqual(
            metadata,
            {"count": 2, "active": True, "items": ["BUF"], "nothing": None},
        )
        self.assertEqual(body, "Body\n")

    def test_rejects_duplicate_keys(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "record.md"
            path.write_text("---\ntitle: First\ntitle: Second\n---\n", encoding="utf-8")

            with self.assertRaisesRegex(FrontMatterError, "duplicates key"):
                parse_front_matter(path)


class CatalogTests(unittest.TestCase):
    def test_catalog_is_sorted_by_record_id_then_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            league = root / "league"
            league.mkdir()
            for filename, record_id in (("z.md", "record-z"), ("a.md", "record-a")):
                (league / filename).write_text(
                    f"---\nrecord_id: {record_id}\nrecord_type: research_finding\n---\n",
                    encoding="utf-8",
                )

            entries = [json.loads(line) for line in render_catalog(root).splitlines()]

        self.assertEqual([entry["record_id"] for entry in entries], ["record-a", "record-z"])


if __name__ == "__main__":
    unittest.main()
