---
schema_version: 1
record_id: ti-2026-phi-20260829-001
record_type: team_intelligence
title: "Philadelphia Eagles intelligence synthesis — 2026-08-29"
team_ids: ["PHI"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-27
last_verified: 2026-08-29
confidence: high
source_ids: ["local-source-philadelphia-eagles"]
supersedes: ["ti-2026-phi-20260826-001"]
observation_ids: ["obs-2026-phi-20260829t143349z-001"]
run_ids: ["20260829T143349Z"]
---

# Philadelphia Eagles intelligence synthesis — 2026-08-29

## Executive signal

Philadelphia exchanged two depth receivers, signing Tahj Washington and waiving Brandon Hayes. The
move does not alter the Smith/Lemon/Wicks/Brown fantasy questions without route or depth-chart evidence.

## Reconciled evidence

One official transaction cluster records both corresponding moves. There are no repeats,
confirmations, or conflicts.

## Hypothesis impact

- `phi-off-002` and `phi-off-003`: **no change.** Neither Washington nor Hayes had established
  first-team evidence in the active hypotheses.
- Prior ledger rows `til-2026-phi-20260825-001` and `til-2026-phi-20260826-001` are resolved; their
  final-depth-chart and Week 1 Lemon usage triggers did not occur in this batch.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Philadelphia signed Washington and waived Hayes. | `obs-2026-phi-20260829t143349z-001` | Reconcile the final receiver roster; no hypothesis edit now. |

## Conflicts and uncertainty

The official log exposes a calendar date but no item-level publication time. No role information
accompanied the move.

## Excluded noise

None.

## Run metrics

- Raw observations: 1
- Unique evidence clusters: 1
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing: 1 log, 0 review, 0 escalate
- Promotions: 0 (not authorized)
- Synthesis elapsed time: approximately 3 minutes

## Sources

- Philadelphia Eagles — [Transactions](https://www.philadelphiaeagles.com/team/transactions/) — dated 2026-08-27; retrieved 2026-08-29T14:37:45Z; observation `obs-2026-phi-20260829t143349z-001`.
