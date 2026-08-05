#!/usr/bin/env python3
"""Validate the canonical NFL schedule and team registry."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

SCHEDULE_COLUMNS = {
    "season", "week", "date_et", "kickoff_et", "away_team", "away_abbr",
    "home_team", "home_abbr", "venue", "venue_city", "neutral_site",
    "schedule_status", "source_url", "last_verified",
}
TEAM_COLUMNS = {
    "team_name", "abbr", "conference", "division", "city", "stadium",
    "stadium_city", "time_zone", "folder_path",
}
VALID_STATUSES = {"scheduled", "flex_pending", "date_time_tbd"}
TIME_RE = re.compile(r"^(?:0?[1-9]|1[0-2]):[0-5][0-9] (?:AM|PM)$")


def read_csv(path: Path) -> tuple[list[dict[str, str]], set[str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader), set(reader.fieldnames or [])


def validate_team_schedules(
    team_rows: list[dict[str, str]],
    game_rows: list[dict[str, str]],
    season: int,
    failures: list[str],
) -> None:
    expected: dict[str, dict[int, tuple[str, str, str, str, str]]] = {
        row["team_name"]: {
            week: ("—", "—", "BYE", "—", "bye") for week in range(1, 19)
        }
        for row in team_rows
    }
    for game in game_rows:
        week = int(game["week"])
        game_date = game["date_et"] or "TBD"
        kickoff = game["kickoff_et"] or "TBD"
        venue = game["venue"]
        status = game["schedule_status"]
        expected[game["away_team"]][week] = (
            game_date, kickoff, f"at {game['home_team']}", venue, status
        )
        expected[game["home_team"]][week] = (
            game_date, kickoff, f"vs. {game['away_team']}", venue, status
        )

    for team in team_rows:
        name = team["team_name"]
        path = Path(team["folder_path"]) / str(season) / "schedule.md"
        if not path.is_file():
            failures.append(f"{name}: missing team schedule {path}")
            continue
        actual: dict[int, tuple[str, str, str, str, str]] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            parts = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(parts) == 6 and parts[0].isdigit():
                actual[int(parts[0])] = tuple(parts[1:])  # type: ignore[assignment]
        for week in range(1, 19):
            if actual.get(week) != expected[name][week]:
                failures.append(
                    f"{name} week {week}: team view {actual.get(week)!r} "
                    f"!= canonical {expected[name][week]!r}"
                )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schedule", type=Path, default=Path("league/schedule/2026.csv"))
    parser.add_argument("--teams", type=Path, default=Path("league/teams.csv"))
    parser.add_argument("--season", type=int, default=2026)
    parser.add_argument(
        "--skip-team-files", action="store_true",
        help="validate only the machine-readable CSV files",
    )
    args = parser.parse_args()

    failures: list[str] = []
    for path in (args.schedule, args.teams):
        if not path.is_file():
            failures.append(f"missing file: {path}")
    if failures:
        print("\n".join(f"ERROR: {item}" for item in failures), file=sys.stderr)
        return 1

    team_rows, team_fields = read_csv(args.teams)
    game_rows, game_fields = read_csv(args.schedule)

    missing_team_fields = TEAM_COLUMNS - team_fields
    missing_game_fields = SCHEDULE_COLUMNS - game_fields
    if missing_team_fields:
        failures.append(f"team registry missing columns: {sorted(missing_team_fields)}")
    if missing_game_fields:
        failures.append(f"schedule missing columns: {sorted(missing_game_fields)}")
    if failures:
        print("\n".join(f"ERROR: {item}" for item in failures), file=sys.stderr)
        return 1

    if len(team_rows) != 32:
        failures.append(f"expected 32 teams, found {len(team_rows)}")

    teams_by_name = {row["team_name"]: row for row in team_rows}
    teams_by_abbr = {row["abbr"]: row for row in team_rows}
    if len(teams_by_name) != len(team_rows):
        failures.append("duplicate team_name in team registry")
    if len(teams_by_abbr) != len(team_rows):
        failures.append("duplicate abbr in team registry")

    expected_games = 272
    if len(game_rows) != expected_games:
        failures.append(f"expected {expected_games} games, found {len(game_rows)}")

    appearances: Counter[str] = Counter()
    weeks_by_team: dict[str, set[int]] = defaultdict(set)
    teams_by_week: dict[int, set[str]] = defaultdict(set)
    matchup_keys: set[tuple[int, frozenset[str]]] = set()

    for line_number, row in enumerate(game_rows, start=2):
        prefix = f"schedule row {line_number}"
        try:
            season = int(row["season"])
            week = int(row["week"])
        except ValueError:
            failures.append(f"{prefix}: season/week must be integers")
            continue

        if season != args.season:
            failures.append(f"{prefix}: season {season} != {args.season}")
        if not 1 <= week <= 18:
            failures.append(f"{prefix}: week {week} outside 1–18")

        away, home = row["away_team"], row["home_team"]
        if away == home:
            failures.append(f"{prefix}: team cannot play itself")
        for side, name, abbr in (
            ("away", away, row["away_abbr"]),
            ("home", home, row["home_abbr"]),
        ):
            team = teams_by_name.get(name)
            if team is None:
                failures.append(f"{prefix}: unknown {side} team {name!r}")
                continue
            if team["abbr"] != abbr:
                failures.append(
                    f"{prefix}: {name} abbreviation {abbr!r} != {team['abbr']!r}"
                )
            if name in teams_by_week[week]:
                failures.append(f"{prefix}: {name} appears twice in week {week}")
            teams_by_week[week].add(name)
            appearances[name] += 1
            weeks_by_team[name].add(week)

        key = (week, frozenset((away, home)))
        if key in matchup_keys:
            failures.append(f"{prefix}: duplicate matchup in week {week}: {away} / {home}")
        matchup_keys.add(key)

        status = row["schedule_status"]
        if status not in VALID_STATUSES:
            failures.append(f"{prefix}: invalid schedule_status {status!r}")

        game_date, kickoff = row["date_et"], row["kickoff_et"]
        if status == "date_time_tbd":
            if game_date or kickoff:
                failures.append(f"{prefix}: TBD game must have blank date/time")
        else:
            try:
                date.fromisoformat(game_date)
            except ValueError:
                failures.append(f"{prefix}: invalid ISO date {game_date!r}")
            if not TIME_RE.fullmatch(kickoff):
                failures.append(f"{prefix}: invalid Eastern kickoff {kickoff!r}")

        if row["neutral_site"] not in {"true", "false"}:
            failures.append(f"{prefix}: neutral_site must be true or false")
        try:
            date.fromisoformat(row["last_verified"])
        except ValueError:
            failures.append(f"{prefix}: invalid last_verified date")

    all_weeks = set(range(1, 19))
    for name in sorted(teams_by_name):
        if appearances[name] != 17:
            failures.append(f"{name}: expected 17 games, found {appearances[name]}")
        if len(weeks_by_team[name]) != 17:
            failures.append(
                f"{name}: expected games in 17 distinct weeks, found {len(weeks_by_team[name])}"
            )
        missing_weeks = all_weeks - weeks_by_team[name]
        if len(missing_weeks) != 1:
            failures.append(f"{name}: expected one bye, found weeks {sorted(missing_weeks)}")

    for week in range(1, 19):
        count = len(teams_by_week[week])
        if count % 2:
            failures.append(f"week {week}: odd number of participating teams ({count})")

    if not args.skip_team_files:
        validate_team_schedules(team_rows, game_rows, args.season, failures)

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        print(f"Validation failed with {len(failures)} error(s).", file=sys.stderr)
        return 1

    neutral_count = sum(row["neutral_site"] == "true" for row in game_rows)
    print(
        f"OK: {len(game_rows)} games, {len(team_rows)} teams, "
        f"17 games and one bye per team, {neutral_count} neutral-site games."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
