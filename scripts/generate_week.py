#!/usr/bin/env python3
"""Generate one weekly research workspace from the canonical schedule."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def matchup_markdown(
    game: dict[str, str], teams: dict[str, dict[str, str]]
) -> str:
    away = teams[game["away_team"]]
    home = teams[game["home_team"]]
    date_label = game["date_et"] or "TBD"
    time_label = game["kickoff_et"] or "TBD"
    away_link = f"../../../../{away['folder_path']}/2026/"
    home_link = f"../../../../{home['folder_path']}/2026/"
    return f"""# {game['away_team']} at {game['home_team']} — Week {game['week']}

- Date (ET): {date_label}
- Kickoff (ET): {time_label}
- Venue: {game['venue']} — {game['venue_city']}
- Schedule status: {game['schedule_status']}
- Neutral site: {game['neutral_site']}
- Team research: [{game['away_team']}]({away_link}) · [{game['home_team']}]({home_link})
- Schedule source: [NFL]({game['source_url']})
- Last schedule verification: {game['last_verified']}

## Injuries and personnel

_TBD_

## Matchup

_TBD_

## Fantasy implications

_TBD_

## Evidence

_TBD_

## Watch items and invalidation

_TBD_
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("week", type=int, choices=range(1, 19), metavar="WEEK")
    parser.add_argument("--season", type=int, default=2026)
    parser.add_argument("--schedule", type=Path, default=Path("league/schedule/2026.csv"))
    parser.add_argument("--teams", type=Path, default=Path("league/teams.csv"))
    parser.add_argument("--output-root", type=Path, default=Path("weekly"))
    parser.add_argument("--force", action="store_true", help="overwrite generated files")
    parser.add_argument("--dry-run", action="store_true", help="show planned output only")
    args = parser.parse_args()

    games = [
        row for row in load_rows(args.schedule)
        if int(row["season"]) == args.season and int(row["week"]) == args.week
    ]
    if not games:
        parser.error(f"no games found for season {args.season}, week {args.week}")

    team_rows = load_rows(args.teams)
    teams = {row["team_name"]: row for row in team_rows}
    target = args.output_root / str(args.season) / f"week-{args.week:02d}"
    games_dir = target / "games"
    filenames = [
        f"{game['away_abbr']}-at-{game['home_abbr']}.md"
        for game in games
    ]
    planned = [target / "README.md", *(games_dir / name for name in filenames)]

    existing = [path for path in planned if path.exists()]
    if existing and not args.force:
        names = "\n".join(f"  {path}" for path in existing)
        parser.error(f"generated files already exist; use --force to replace:\n{names}")

    if args.dry_run:
        print(f"Would generate {len(planned)} files under {target}:")
        for path in planned:
            print(path)
        return 0

    games_dir.mkdir(parents=True, exist_ok=True)
    games = sorted(games, key=lambda row: (
        row["date_et"] or "9999-99-99",
        row["kickoff_et"] or "TBD",
        row["away_abbr"],
    ))

    active = {game["away_team"] for game in games} | {
        game["home_team"] for game in games
    }
    byes = sorted(set(teams) - active)
    bye_label = ", ".join(byes) if byes else "None"

    table_rows = []
    for game in games:
        filename = f"{game['away_abbr']}-at-{game['home_abbr']}.md"
        path = games_dir / filename
        path.write_text(matchup_markdown(game, teams), encoding="utf-8")
        table_rows.append(
            f"| {game['date_et'] or 'TBD'} | {game['kickoff_et'] or 'TBD'} | "
            f"[{game['away_team']} at {game['home_team']}](games/{filename}) | "
            f"{game['schedule_status']} |"
        )

    index = f"""# {args.season} Week {args.week:02d}

- Bye teams: {bye_label}
- Generated from: [canonical schedule](../../../league/schedule/{args.season}.csv)
- Regenerate: `python scripts/generate_week.py {args.week} --force`

| Date (ET) | Kickoff (ET) | Matchup | Status |
|---|---|---|---|
{chr(10).join(table_rows)}

Fast-changing injuries, weather, roles, projections, and decisions belong in this weekly workspace. Durable player or scheme findings belong in the canonical player/team records.
"""
    (target / "README.md").write_text(index, encoding="utf-8")
    print(f"Generated {len(planned)} files under {target}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
