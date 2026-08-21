from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import validate_repository


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


class SourceRegistryValidationTests(unittest.TestCase):
    def test_allows_legacy_registry_without_candidate_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            directory = root / "teams/NFC/North/Legacy-Team/2026/beat-writers"
            directory.mkdir(parents=True)
            (directory / "registry.md").write_text(
                "---\nwriter_ids: [\"writer-one\"]\n---\n",
                encoding="utf-8",
            )
            (directory / "sources.csv").write_text(
                "source_id,entity_type\nwriter-one,person\n",
                encoding="utf-8",
            )
            (directory / "endpoints.csv").write_text(
                "source_id,url\n",
                encoding="utf-8",
            )
            failures: list[str] = []
            with patch.object(validate_repository, "REPO_ROOT", root):
                validate_repository.validate_source_registries(failures)

        self.assertEqual(failures, [])

    def test_reconciles_writers_endpoints_and_candidate_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            directory = root / "teams/NFC/North/Test-Team/2026/beat-writers"
            directory.mkdir(parents=True)
            (directory / "registry.md").write_text(
                "---\nwriter_ids: [\"writer-one\", \"source-org\"]\n---\n",
                encoding="utf-8",
            )
            (directory / "sources.csv").write_text(
                "source_id,entity_type\nwriter-one,person\nsource-org,organization\nmissing-endpoint,organization\n",
                encoding="utf-8",
            )
            (directory / "endpoints.csv").write_text(
                "source_id,url\nwriter-one,https://example.com\nunknown,https://example.com\n",
                encoding="utf-8",
            )
            (directory / "candidates.csv").write_text(
                ",".join(validate_repository.CANDIDATE_HEADERS) + "\n"
                "candidate-one,Writer One,Outlet,person,initial,beat,,,include,essential,,writer-one,not-a-date\n",
                encoding="utf-8",
            )
            failures: list[str] = []
            with patch.object(validate_repository, "REPO_ROOT", root):
                validate_repository.validate_source_registries(failures)

        self.assertTrue(any("unknown source_ids" in failure for failure in failures))
        self.assertTrue(any("sources without endpoints" in failure for failure in failures))
        self.assertTrue(any("is not a person" in failure for failure in failures))
        self.assertTrue(any("included candidate requires" in failure for failure in failures))
        self.assertTrue(any("not an ISO date" in failure for failure in failures))


if __name__ == "__main__":
    unittest.main()
