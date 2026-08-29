---
schema_version: 1
record_id: ti-2026-tb-20260829-001
record_type: team_intelligence
title: "Tampa Bay Buccaneers intelligence synthesis — 2026-08-29"
team_ids: ["TB"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-28
last_verified: 2026-08-29
confidence: high
source_ids: ["local-source-tampa-bay-buccaneers"]
supersedes: ["ti-2026-tb-20260824-001"]
observation_ids: ["obs-2026-tb-20260829t143349z-001", "obs-2026-tb-20260829t143349z-002"]
run_ids: ["20260829T143349Z"]
---

# Tampa Bay Buccaneers intelligence synthesis — 2026-08-29

## Executive signal

Eric Rivers Jr.'s six-catch finale and Jack Pyburn's two sacks are roster-cut evidence from a
reserve-context game. Neither performance establishes a fantasy role or changes Tampa Bay's
starting receiver or edge-rush hypotheses.

## Reconciled evidence

The official recap supplies two measured performance clusters from the same game: Rivers caught
six passes for 24 yards (`obs-2026-tb-20260829t143349z-001`), and Pyburn recorded four tackles and
two sacks (`obs-2026-tb-20260829t143349z-002`). The observations concern different units and do not
confirm each other.

## Hypothesis impact

- `tb-off-wr-001`: **no change.** Rivers' low-yardage reserve production supplies no first-team
  route, alignment, or target-order evidence.
- `tb-def-edge-001`: **no change.** Pyburn's production supports a roster case but lacks a pressure
  denominator, blitz context, and first-team role.

## Open-ledger trigger assessment

Tampa Bay has no open intelligence-ledger row. No prior trigger required disposition.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Rivers produced six short receptions in reserve finale work. | `obs-2026-tb-20260829t143349z-001` | Check final roster status; require first-team routes before revisiting `tb-off-wr-001`. |
| log | Pyburn recorded two sacks in the preseason finale. | `obs-2026-tb-20260829t143349z-002` | Check final roster and regular-season defensive role; do not infer starting pressure share. |

## Conflicts and uncertainty

No conflict exists. The official recap lacks snaps, routes, alignments, pressure denominators, and
opponent-unit context needed for role conclusions.

## Excluded noise

The 19-0 score and broad characterization of the offense as low-octane were excluded from player
and unit conclusions.

## Run metrics

- Raw observations: 2
- Unique evidence clusters: 2
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing: 2 log, 0 review, 0 escalate
- Promotions: 0
- Synthesis elapsed time: approximately 4 minutes

## Sources

- Brianna Dix, Tampa Bay Buccaneers — [Rapid Reaction: Jaguars 19, Buccaneers 0](https://www.buccaneers.com/news/bucs-lose-jacksonville-jaguars-preseason-week-3-2026-score-19-0) — published 2026-08-28T23:59:00-04:00; retrieved 2026-08-29T14:38:07Z; observations `obs-2026-tb-20260829t143349z-001` and `obs-2026-tb-20260829t143349z-002`.
