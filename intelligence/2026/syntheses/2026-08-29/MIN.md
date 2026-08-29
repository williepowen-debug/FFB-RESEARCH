---
schema_version: 1
record_id: ti-2026-min-20260829-001
record_type: team_intelligence
title: "Minnesota Vikings intelligence synthesis — 2026-08-29"
team_ids: ["MIN"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-28
last_verified: 2026-08-29
confidence: high
source_ids: ["local-source-minnesota-vikings"]
supersedes: ["ti-2026-min-20260824-001"]
observation_ids: ["obs-2026-min-20260829t143349z-001", "obs-2026-min-20260829t143349z-002"]
run_ids: ["20260829T143349Z"]
---

# Minnesota Vikings intelligence synthesis — 2026-08-29

## Executive signal

J.J. McCarthy's ankle injury limited his final preseason week and kept him out of Wednesday's
practice; Carson Wentz then started the finale for two series before Max Brosmer entered. This affects
reserve depth but does not challenge Kyler Murray's working QB1 baseline.

## Reconciled evidence

The official postgame account supplies two unique clusters from one origin: McCarthy's practice
availability and the Wentz/Brosmer game allocation. The latter is not independent confirmation of a
depth-chart order because starters were rested.

## Hypothesis impact

- `min-2026-off-q01`: **no change.** Murray's QB1 status is not challenged; the required official
  Week 1 depth-chart trigger remains outstanding.
- No active skill-position hypothesis is tested by the reserve-quarterback finale allocation.

Minnesota has no intelligence ledger, so no prior open trigger required disposition.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | McCarthy missed the key Wednesday practice with an ankle injury. | `obs-2026-min-20260829t143349z-001` | Monitor Week 1 practice status for reserve-depth implications. |
| log | Wentz started the finale and yielded to Brosmer after two series. | `obs-2026-min-20260829t143349z-002` | Check the final quarterback roster and official depth chart. |

## Conflicts and uncertainty

The source does not provide a recovery timetable for McCarthy. Finale usage cannot distinguish
roster evaluation from the final backup order.

## Excluded noise

None.

## Run metrics

- Raw observations: 2
- Unique evidence clusters: 2
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing: 2 log, 0 review, 0 escalate
- Promotions: 0 (not authorized)
- Synthesis elapsed time: approximately 4 minutes

## Sources

- Minnesota Vikings — [Vikings at Broncos Game Observations](https://www.vikings.com/news/broncos-2026-preseason-game-observations) — published 2026-08-28T23:20:00-05:00; retrieved 2026-08-29T14:37:45Z; observations `obs-2026-min-20260829t143349z-001` and `obs-2026-min-20260829t143349z-002`.
