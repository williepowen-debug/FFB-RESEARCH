from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ScheduleCliTests(unittest.TestCase):
    def test_rejects_team_playing_itself(self) -> None:
        source = REPO_ROOT / "league" / "schedule" / "2026.csv"
        with source.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            fieldnames = reader.fieldnames
        self.assertIsNotNone(fieldnames)
        rows[0]["home_team"] = rows[0]["away_team"]
        rows[0]["home_abbr"] = rows[0]["away_abbr"]

        with tempfile.TemporaryDirectory() as temporary_directory:
            schedule = Path(temporary_directory) / "schedule.csv"
            with schedule.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "validate_schedule.py"),
                    "--schedule",
                    str(schedule),
                    "--teams",
                    str(REPO_ROOT / "league" / "teams.csv"),
                    "--skip-team-files",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("team cannot play itself", result.stderr)


if __name__ == "__main__":
    unittest.main()
