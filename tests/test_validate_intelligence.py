from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_intelligence import OBSERVATION_HEADERS, PRIORITY_HEADERS, validate_intelligence


class IntelligenceValidationTests(unittest.TestCase):
    def build_fixture(self, root: Path) -> tuple[Path, Path, Path]:
        league = root / "league"
        league.mkdir()
        (league / "teams.csv").write_text(
            "team_name,abbr,conference,division,city,stadium,stadium_city,time_zone,folder_path\n"
            "Test Team,TST,NFC,North,Test,Test Stadium,Test City,America/New_York,teams/NFC/North/Test-Team\n",
            encoding="utf-8",
        )
        registry = root / "teams/NFC/North/Test-Team/2026/beat-writers"
        registry.mkdir(parents=True)
        (registry / "sources.csv").write_text("source_id\nlocal-writer-one\n", encoding="utf-8")

        run = root / "intelligence/2026/runs/20260821T180000Z/reader-one"
        run.mkdir(parents=True)
        observations = run / "observations.csv"
        observations.write_text(
            ",".join(OBSERVATION_HEADERS) + "\n"
            "obs-2026-tst-20260821t180000z-001,TST,,local-writer-one,https://example.com/report,"
            "https://example.com/report,2026-08-21T17:00:00Z,2026-08-21T18:00:00Z,role,"
            "firsthand_observation,Player took every first-team rep,new,,tst-rb-first-team,high,high,"
            "high,reader-one,\n",
            encoding="utf-8",
        )

        synthesis = root / "intelligence/2026/syntheses/2026-08-21/TST.md"
        synthesis.parent.mkdir(parents=True)
        synthesis.write_text(
            "---\nrecord_id: ti-2026-tst-20260821-001\nrecord_type: team_intelligence\n"
            "observation_ids: [\"obs-2026-tst-20260821t180000z-001\"]\n---\n",
            encoding="utf-8",
        )

        priority = root / "intelligence/2026/priority/2026-08-21/priority-board.csv"
        priority.parent.mkdir(parents=True)
        priority.write_text(
            ",".join(PRIORITY_HEADERS) + "\n"
            "sig-2026-tst-20260821-001,TST,,obs-2026-tst-20260821t180000z-001,"
            "ti-2026-tst-20260821-001,review,role,First-team role changed,Potential workload increase,"
            "Seek independent confirmation,high,open,2026-08-21T18:10:00Z,2026-08-21T18:10:00Z\n",
            encoding="utf-8",
        )
        return observations, synthesis, priority

    def test_accepts_traceable_pipeline(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.build_fixture(root)
            failures = validate_intelligence(root)

        self.assertEqual(failures, [])

    def test_rejects_unregistered_source_and_broken_priority_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            observations, _, priority = self.build_fixture(root)
            observations.write_text(
                observations.read_text(encoding="utf-8").replace("local-writer-one", "unknown-source"),
                encoding="utf-8",
            )
            priority.write_text(
                priority.read_text(encoding="utf-8").replace(
                    "obs-2026-tst-20260821t180000z-001,ti-2026",
                    "obs-2026-tst-20260821t180000z-999,ti-2026",
                ),
                encoding="utf-8",
            )
            failures = validate_intelligence(root)

        self.assertTrue(any("source_id is not registered" in failure for failure in failures))
        self.assertTrue(any("unknown observation_ids" in failure for failure in failures))


if __name__ == "__main__":
    unittest.main()
