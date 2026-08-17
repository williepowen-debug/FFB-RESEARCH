---
schema_version: 1
record_id: rf-2026-league-sos-watchlist-pass-001
record_type: research_finding
title: "2026 Schedule-Derived Watchlist Pass 001"
team_ids: []
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-17
last_verified: 2026-08-17
confidence: low
source_ids: ["athlon-2026-fantasy-sos", "fta-2026-playoff-sos", "ffb-2026-schedule"]
supersedes: []
---

# Finding: 2026 Schedule-Derived Watchlist Pass 001

## Scope

- Team/player: League-wide
- Area: Schedule-derived fantasy watchlist
- Season/week: 2026 season, preseason baseline
- Status: active
- Last verified: 2026-08-17

## Finding

The first actionable pass from early-season SOS creates 25 watchlist rows: 12 draft targets, 6 streamers, 2 buy-low watches, 1 sell-high watch, and 4 avoid-early-panic flags.

This is still a low-confidence schedule layer. It should be combined with role security, ADP, health, and scoring format before becoming a player recommendation.

## Fantasy implication

The watchlist gives draft prep and early-season management a practical queue:

- Draft tie-breakers: Eagles passing game, Cowboys passing game/backfield, Lions RBs, Texans WR/RB, Ravens WR, 49ers TE, Steelers D/ST, Lions D/ST.
- Streamers: Bengals TE, Browns TE, Seahawks TE, Dolphins D/ST, Raiders D/ST, Saints D/ST.
- Buy-low/patience: Dolphins WRs, Jaguars WRs, Bears WRs, Chargers passing game, Bills RBs, Chiefs RBs.
- Sell-high watch: Giants lead RB if the early schedule creates production that outruns the longer-term role/offense profile.

## Evidence

- `watchlists.csv` contains 25 rows.
- The labels are derived from `early-season-sos.csv`, `position-sos.csv`, `playoff-sos.csv`, and `schedule-wrinkles.csv`.
- The strongest multi-position early team schedule signal remains the Giants.
- The cleanest schedule-plus-team-quality early RB signal is the Lions backfield.
- The clearest draftable early D/ST signal is the Steelers, with Lions D/ST also supported.
- The clearest early box-score drag candidates are Jaguars WRs, Bears pass catchers, Dolphins WRs, Chargers passing game, Bills RBs, and Chiefs RBs.

## Sources

- `watchlists.csv`
- `early-season-sos.csv`
- `position-sos.csv`
- `playoff-sos.csv`
- `schedule-wrinkles.csv`
- `snapshots/2026-08-17-baseline-hot-start-sos.md`

## Assessment

- Confidence: low
- Reason: This pass is schedule-derived and does not yet include ADP, final depth charts, injury status, or actual 2026 defensive performance.
- Fact/inference boundary: The schedule ranks and watchlist rows are repository data. The action labels are fantasy inferences.
- What would invalidate this: ADP makes the target too expensive, role clarity breaks against the target, injuries change expected usage, or 2026 defensive performance invalidates the opponent-rank baseline.
- Next review: Add ADP/cost and role-confidence fields after draft market data is collected.

