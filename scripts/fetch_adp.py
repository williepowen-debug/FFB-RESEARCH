#!/usr/bin/env python3
"""Fetch ADP snapshots from public sources into league/rankings/adp/.

Sources:
- Fantasy Football Calculator public API (real mock/live drafts; format-specific).
- ESPN fantasy read API (default ranks and live ADP shown in ESPN draft lobbies).

Usage:
    python3 scripts/fetch_adp.py [--teams 12] [--scoring ppr] [--year 2026]

Writes date-stamped CSVs; never overwrites a previous day's snapshot silently.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.request
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "league/rankings/adp"

FFC_URL = "https://fantasyfootballcalculator.com/api/v1/adp/{scoring}?teams={teams}&year={year}"
ESPN_URL = (
    "https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}"
    "/segments/0/leaguedefaults/3?view=kona_player_info"
)
ESPN_FILTER = '{"players":{"limit":300,"sortAdp":{"sortAsc":true,"sortPriority":1}}}'

ESPN_POSITIONS = {1: "QB", 2: "RB", 3: "WR", 4: "TE", 5: "K", 16: "D/ST"}
ESPN_TEAMS = {
    0: "FA", 1: "ATL", 2: "BUF", 3: "CHI", 4: "CIN", 5: "CLE", 6: "DAL", 7: "DEN",
    8: "DET", 9: "GB", 10: "TEN", 11: "IND", 12: "KC", 13: "LV", 14: "LAR", 15: "MIA",
    16: "MIN", 17: "NE", 18: "NO", 19: "NYG", 20: "NYJ", 21: "PHI", 22: "ARI",
    23: "PIT", 24: "LAC", 25: "SF", 26: "SEA", 27: "TB", 28: "WSH", 29: "CAR",
    30: "JAX", 33: "BAL", 34: "HOU",
}


def fetch_json(url: str, headers: dict[str, str] | None = None) -> dict:
    base_headers = {"User-Agent": "curl/8.5.0", "Accept": "application/json"}
    request = urllib.request.Request(url, headers={**base_headers, **(headers or {})})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def write_ffc(teams: int, scoring: str, year: int, snapshot_date: str) -> Path:
    data = fetch_json(FFC_URL.format(scoring=scoring, teams=teams, year=year))
    meta = data.get("meta", {})
    out_path = OUT_DIR / f"{snapshot_date}-ffc-{teams}team-{scoring}.csv"
    with out_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "adp_rank", "name", "position", "team", "adp", "adp_formatted",
            "high", "low", "stdev", "times_drafted", "bye",
            "source", "scoring", "league_size", "total_drafts",
            "sample_start", "sample_end", "snapshot_date",
        ])
        for rank, player in enumerate(data.get("players", []), start=1):
            writer.writerow([
                rank, player.get("name"), player.get("position"), player.get("team"),
                player.get("adp"), player.get("adp_formatted"), player.get("high"),
                player.get("low"), player.get("stdev"), player.get("times_drafted"),
                player.get("bye"), "fantasyfootballcalculator", scoring, teams,
                meta.get("total_drafts"), meta.get("start_date"), meta.get("end_date"),
                snapshot_date,
            ])
    return out_path


def write_espn(year: int, snapshot_date: str) -> Path:
    data = fetch_json(ESPN_URL.format(year=year), headers={"x-fantasy-filter": ESPN_FILTER})
    out_path = OUT_DIR / f"{snapshot_date}-espn-adp.csv"
    with out_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "espn_adp_rank", "name", "position", "team", "espn_live_adp",
            "espn_ppr_rank", "espn_standard_rank", "espn_ppr_auction_value",
            "percent_owned", "espn_player_id", "source", "snapshot_date",
        ])
        rank = 0
        for entry in data.get("players", []):
            player = entry.get("player", {})
            ownership = player.get("ownership") or {}
            ranks = player.get("draftRanksByRankType") or {}
            adp = ownership.get("averageDraftPosition")
            if adp is None:
                continue
            rank += 1
            writer.writerow([
                rank, player.get("fullName"),
                ESPN_POSITIONS.get(player.get("defaultPositionId"), "?"),
                ESPN_TEAMS.get(player.get("proTeamId"), "?"),
                round(adp, 1),
                (ranks.get("PPR") or {}).get("rank"),
                (ranks.get("STANDARD") or {}).get("rank"),
                (ranks.get("PPR") or {}).get("auctionValue"),
                round(ownership.get("percentOwned", 0), 1),
                player.get("id"), "espn", snapshot_date,
            ])
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--teams", type=int, default=12)
    parser.add_argument("--scoring", default="ppr", choices=["ppr", "half-ppr", "standard", "2qb"])
    parser.add_argument("--year", type=int, default=2026)
    parser.add_argument("--date", default=date.today().isoformat(), help="snapshot date (YYYY-MM-DD)")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for label, writer_fn in (
        ("FFC", lambda: write_ffc(args.teams, args.scoring, args.year, args.date)),
        ("ESPN", lambda: write_espn(args.year, args.date)),
    ):
        try:
            path = writer_fn()
        except Exception as exc:  # noqa: BLE001 - report and continue with other source
            print(f"ERROR: {label} fetch failed: {exc}", file=sys.stderr)
            continue
        with path.open(encoding="utf-8") as handle:
            rows = sum(1 for _ in handle) - 1
        print(f"Wrote {rows} rows to {path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
