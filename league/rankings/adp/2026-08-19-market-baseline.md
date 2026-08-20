---
schema_version: 1
record_id: rf-2026-league-adp-baseline-001
record_type: research_finding
title: "ADP market baseline 2026-08-19 — Gridiron Guru's Only draft prep"
team_ids: []
player_ids: []
season: 2026
week: null
status: superseded
time_horizon: seasonal
valid_as_of: 2026-08-19
last_verified: 2026-08-19
confidence: medium
source_ids: ["ffc-2026-adp-api", "espn-2026-fantasy-api"]
supersedes: []
---

> **Superseded 2026-08-20 by `rf-2026-league-adp-baseline-002`**
> ([2026-08-20-availability-windows.md](2026-08-20-availability-windows.md)). The data below
> stands; two conclusions in "Fantasy implication" did not survive the availability
> arithmetic and are corrected there.

# Finding: The market prices the first QB near pick 33; slot 10's window is exactly the dual-threat RB tier

## Scope

- Area: league-wide draft market prices ahead of the 2026-08-21 Gridiron Guru's
  Only draft (12-team PPR, slot 10; see
  [league record](../../scoring-formats/gridiron-gurus-only-2026.md))
- Data: `2026-08-19-ffc-12team-ppr.csv` (266 players, 6,885 real 12-team PPR
  drafts, 2026-08-12 to 2026-08-19) and `2026-08-19-espn-adp.csv` (300 players,
  ESPN default ranks plus live ADP)

## Finding

Neutral-market drafters take the first quarterback (Josh Allen) at overall 22–33
and the second tier (Jackson, Maye, Burrow, Daniels, Hurts) between roughly 39 and
60. In a league scoring 6-point passing touchdowns plus completions, that pricing
leaves the QB position systematically cheap relative to league-specific value.
Separately, the picks 8–18 window in current 12-team PPR drafts is dominated by
the dual-threat RB tier and elite WRs, matching the expected board at slot 10.

## Evidence

FFC 12-team PPR (6,885 drafts, week ending 2026-08-19):

- Picks 8–18 by ADP: Jonathan Taylor 7.4, Drake London 10.1, De'Von Achane 10.2,
  CeeDee Lamb 10.7, Justin Jefferson 11.8, James Cook 12.3, Chase Brown 13.7,
  Rashee Rice 14.8, Ashton Jeanty 15.3, Derrick Henry 17.6, A.J. Brown 17.7.
- Achane range 5–16 (stdev 1.9); Cook 5–22; Chase Brown 6–22.
- QBs: Allen 32.5 (range 10–48), Maye 50.5, Burrow 56.0, Jackson 56.8,
  Prescott 65.8, Daniels 72.9, Stafford 77.9.

ESPN (live ADP vs. default lobby rank):

- Allen 22.1 live vs. rank 36; Jackson 38.8 vs. 58; Maye 47.4 vs. 60;
  Daniels 50.8 vs. 56; Hurts 52.3 vs. 62; Burrow 60.0 vs. 81.
- ESPN drafters already bump QBs 15–20 spots above the default list even in
  generic scoring; the lobby list itself badly lags the market.
- Top of board: ESPN has Gibbs (1.5) over Bijan Robinson (2.6); FFC reverses them.

## Fantasy implication

For slot 10 (picks 10, 15, 34, 39, 58, 63, ...):

- **Pick 10 will offer the exact tier discussed**: one of Achane / Lamb /
  Jefferson / London is essentially guaranteed; Cook and Chase Brown are the
  fallback tier at 15.
- **The QB plan can likely wait past 15**: with tier-2 QBs priced 39–60 on the
  platforms, taking elite skill players at both 10 and 15 and the first QB at 34
  (targeting whichever of Jackson/Maye/Burrow slides) is well-supported by market
  ranges. Allen at 15 remains a justified reach in this league's scoring if the
  room is drafting off neutral instincts.
- **Room-behavior caveat**: ESPN applies league scoring to its *projected points*
  sort. Any league-mate sorting by projections in a 6-point-TD league will see
  QBs at the top of the list. Do not assume the QB discount survives contact with
  the room; be ready to take the QB at 15 if two or more go before pick 30.
- **QB2 window**: Prescott/Daniels/Stafford tier at 58/63 fits the required
  2-QB roster build at near-zero opportunity cost.

## Assessment

- Confidence: medium
- Reason: sample sizes are large and current, but neither source reflects this
  league's custom scoring, and room behavior on draft night is a one-shot event.
- Fact/inference boundary: all ADP figures are sourced facts from the snapshot
  CSVs; the availability projections at specific picks are inference from ranges.
- What would invalidate this: a market shift before 2026-08-21 (injury news), or
  a draft room that prices QBs aggressively from the start.
- Next review: refresh snapshots the morning of 2026-08-21 with
  `python3 scripts/fetch_adp.py` and re-check the QB tier pricing.

## Sources

- Fantasy Football Calculator public ADP API —
  [12-team PPR, year 2026](https://fantasyfootballcalculator.com/api/v1/adp/ppr?teams=12&year=2026)
  — fetched 2026-08-19; sample of 6,885 drafts, 2026-08-12 to 2026-08-19.
- ESPN fantasy read API —
  [2026 leaguedefaults kona_player_info view](https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2026/segments/0/leaguedefaults/3?view=kona_player_info)
  — fetched 2026-08-19.
