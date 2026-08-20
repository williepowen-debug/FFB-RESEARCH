from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import validate_repository


class LinkValidationTests(unittest.TestCase):
    def test_rejects_broken_relative_link(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            path = root / "README.md"
            path.write_text("[missing](missing.md)\n", encoding="utf-8")
            failures: list[str] = []

            with patch.object(validate_repository, "REPO_ROOT", root):
                validate_repository.validate_links(failures)

        self.assertEqual(failures, ["README.md: broken relative link missing.md"])


class SupersessionValidationTests(unittest.TestCase):
    def test_rejects_unknown_self_and_cyclic_references(self) -> None:
        failures: list[str] = []
        validate_repository.validate_supersession_references(
            {
                "record-a": ["record-b", "missing-record"],
                "record-b": ["record-a"],
                "record-c": ["record-c"],
            },
            {
                "record-a": Path("a.md"),
                "record-b": Path("b.md"),
                "record-c": Path("c.md"),
            },
            failures,
        )

        self.assertIn("a.md: supersedes unknown record_ids ['missing-record']", failures)
        self.assertIn("c.md: record cannot supersede itself", failures)
        self.assertTrue(any(failure.startswith("supersession cycle:") for failure in failures))


if __name__ == "__main__":
    unittest.main()
