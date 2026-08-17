---
schema_version: 1
record_id: rf-2026-league-sos-changelog-001
record_type: research_finding
title: "Strength Of Schedule Changelog"
team_ids: []
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-17
last_verified: 2026-08-17
confidence: low
source_ids: ["nfl-ops-2026-sos", "sporting-news-2026-sos", "athlon-2026-fantasy-sos", "fta-2026-playoff-sos", "ffb-2026-schedule"]
supersedes: []
---

# Finding: Strength Of Schedule Changelog

## Scope

- Team/player: League-wide
- Area: 2026 strength-of-schedule research versioning
- Season/week: 2026 season, preseason baseline
- Status: active
- Last verified: 2026-08-17

## Finding

The strength-of-schedule workspace now separates current data tables from dated interpretation snapshots, so future changes can update the CSVs while preserving the dated research take that drove draft, waiver, trade, or ranking decisions.

## Fantasy implication

Schedule-based player targeting can change materially as 2026 roles, injuries, and defensive performance data update. The changelog preserves why a schedule edge was considered actionable at the time, reducing the risk of stale or silently overwritten conclusions.

## Evidence

## 2026-08-17

- Created the strength-of-schedule workspace under `league/schedule/`.
- Added source registry rows for NFL Ops, Sporting News/Sharp, Athlon, Fantasy Team Advice, and the internal canonical schedule.
- Filled `overall-sos.csv` with:
  - 32-team prior-year opponent win percentage ranks from NFL Ops.
  - 32-team market/projection SOS ranks from Sharp Football Analysis as summarized by Sporting News.
- Filled `position-sos.csv` with Athlon top/bottom position-level fantasy SOS groups for QB, RB, WR, TE, and DST.
- Filled `playoff-sos.csv` with Fantasy Team Advice overall Weeks 14-17 playoff SOS extremes.
- Filled `schedule-wrinkles.csv` with all 2026 bye weeks and all neutral-site/international games from `league/schedule/2026.csv`.
- Added `early-season-sos.csv` for first-five-played-games hot-start/cold-start targeting.
- Added baseline snapshot: `snapshots/2026-08-17-baseline-hot-start-sos.md`.
- Added `watchlists.csv` to translate schedule signals into actionable draft, streaming, sell-high, buy-low, and patience labels.
- Added snapshot: `snapshots/2026-08-17-watchlist-pass-001.md`.
- Added `adp-research.csv` with a first 27-row market-cost pass for schedule watchlist players.
- Added ADP/ranking sources: FantasyPros ADP, FantasyPros rankings, BeatADP, Fantasy Team Advice player rankings, FantasySP, Footballguys, and NFL.com RB values.
- Added snapshot: `snapshots/2026-08-17-adp-pass-001.md`.

Interpretation impact:

- The first hot-start target flags are baseline, schedule-derived signals only.
- Giants, Eagles, Cowboys, Bengals, Browns, Lions, Texans, Ravens, 49ers, Seahawks, Dolphins DST, Raiders DST, Steelers DST, Saints DST, and Lions DST emerged as early schedule beneficiaries by at least one fantasy position.
- Cardinals and Cowboys Week 14 byes were flagged as playoff-format friction.
- The 49ers showed a full-season versus playoff-window contradiction: favorable market SOS, but difficult FTA Weeks 14-17 playoff SOS.
- Watchlist interpretation remains low confidence until role, health, and ADP inputs are attached.
- First ADP pass suggests schedule signals are already fully priced for Jahmyr Gibbs, CeeDee Lamb, Nico Collins, Lamar Jackson, and James Cook, while Jalen Hurts, Dak Prescott, C.J. Stroud, George Kittle, and selected mid-round WR/RB options may be more useful cost-adjusted schedule targets.

## Sources

- `sources.csv`
- `overall-sos.csv`
- `position-sos.csv`
- `early-season-sos.csv`
- `playoff-sos.csv`
- `schedule-wrinkles.csv`

## Assessment

- Confidence: low
- Reason: This is a versioning and interpretation-control record, not a direct player projection. It is supported by the repository structure and the current source registry.
- Fact/inference boundary: The file additions and CSV rows are factual repository state. The fantasy implication is an inference about how schedule research should be consumed.
- What would invalidate this: A future schema or repository convention creates a better first-class record type for schedule model versions.
- Next review: After the next major SOS data refresh or before converting schedule takes into player/team records.
