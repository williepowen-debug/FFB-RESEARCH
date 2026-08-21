from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_intelligence import (
    ASSIGNMENT_HEADERS,
    LEDGER_HEADERS,
    OBSERVATION_HEADERS,
    PRIORITY_HEADERS,
    RUN_REPORT_HEADERS,
    validate_intelligence,
)


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
        assignments = run.parent / "assignments.csv"
        assignments.write_text(
            ",".join(ASSIGNMENT_HEADERS) + "\n"
            "20260821T180000Z,reader-one,2026,TST,local-writer-one,beat_reporting,"
            "2026-08-21T16:00:00Z,2026-08-21T18:00:00Z,"
            "intelligence/2026/runs/20260821T180000Z/reader-one,frozen,Test assignment\n",
            encoding="utf-8",
        )
        observations = run / "observations.csv"
        observations.write_text(
            ",".join(OBSERVATION_HEADERS) + "\n"
            "obs-2026-tst-20260821t180000z-001,TST,,local-writer-one,https://example.com/report,"
            "https://example.com/report,2026-08-21T17:00:00Z,2026-08-21T18:00:00Z,role,"
            "firsthand_observation,Player took every first-team rep,new,,tst-rb-first-team,high,high,"
            "high,reader-one,\n",
            encoding="utf-8",
        )
        (run / "run-report.csv").write_text(
            ",".join(RUN_REPORT_HEADERS) + "\n"
            "20260821T180000Z,reader-one,TST,2026-08-21T16:00:00Z,2026-08-21T18:00:00Z,"
            "20,10,local-writer-one,checked,1,1,0,0,1,0,false,"
            "obs-2026-tst-20260821t180000z-001,0,,Spot check passed\n",
            encoding="utf-8",
        )

        synthesis = root / "intelligence/2026/syntheses/2026-08-21/TST.md"
        synthesis.parent.mkdir(parents=True)
        synthesis.write_text(
            "---\nrecord_id: ti-2026-tst-20260821-001\nrecord_type: team_intelligence\n"
            "team_ids: [\"TST\"]\n"
            "observation_ids: [\"obs-2026-tst-20260821t180000z-001\"]\n---\n",
            encoding="utf-8",
        )

        target = root / "teams/NFC/North/Test-Team/2026/offense/hypotheses.csv"
        target.parent.mkdir(parents=True)
        target.write_text("question_id\ntst-off-001\n", encoding="utf-8")
        ledger = root / "teams/NFC/North/Test-Team/2026/intelligence-ledger.csv"
        ledger.write_text(
            ",".join(LEDGER_HEADERS) + "\n"
            "til-2026-tst-20260821-001,2026-08-21,TST,ti-2026-tst-20260821-001,"
            "obs-2026-tst-20260821t180000z-001,review,role,Test Player,supports,tst-off-001,"
            "teams/NFC/North/Test-Team/2026/offense/hypotheses.csv,deferred,Next game,open,,,,"
            "Awaiting role confirmation\n",
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

    def test_rejects_bad_report_outcome_and_ledger_lifecycle(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.build_fixture(root)
            report = root / "intelligence/2026/runs/20260821T180000Z/reader-one/run-report.csv"
            report.write_text(
                report.read_text(encoding="utf-8").replace(",checked,", ",checked_no_new_material,"),
                encoding="utf-8",
            )
            ledger = root / "teams/NFC/North/Test-Team/2026/intelligence-ledger.csv"
            ledger.write_text(
                ledger.read_text(encoding="utf-8").replace(",deferred,Next game,open,", ",promoted,Next game,open,"),
                encoding="utf-8",
            )
            failures = validate_intelligence(root)

        self.assertTrue(any("invalid access_outcome" in failure for failure in failures))
        self.assertTrue(any("promoted/no_change ledger item must be resolved" in failure for failure in failures))

    def test_rejects_publication_outside_window_and_unknown_target(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            observations, _, _ = self.build_fixture(root)
            observations.write_text(
                observations.read_text(encoding="utf-8").replace(
                    "2026-08-21T17:00:00Z", "2026-08-21T19:00:00Z"
                ),
                encoding="utf-8",
            )
            ledger = root / "teams/NFC/North/Test-Team/2026/intelligence-ledger.csv"
            ledger.write_text(
                ledger.read_text(encoding="utf-8").replace("tst-off-001", "tst-off-999"),
                encoding="utf-8",
            )
            failures = validate_intelligence(root)

        self.assertTrue(any("published_at falls outside" in failure for failure in failures))
        self.assertTrue(any("target_ids not found" in failure for failure in failures))


if __name__ == "__main__":
    unittest.main()
