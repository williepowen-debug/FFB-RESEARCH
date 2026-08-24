---
schema_version: 1
record_id: ti-2026-pit-20260824-001
record_type: team_intelligence
title: "Pittsburgh Steelers intelligence synthesis — 2026-08-24"
team_ids: ["PIT"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-24
last_verified: 2026-08-24
confidence: medium
source_ids: ["local-source-pittsburgh-steelers"]
supersedes: []
observation_ids: ["obs-2026-pit-20260824t151559z-001", "obs-2026-pit-20260824t151559z-002", "obs-2026-pit-20260824t151559z-003", "obs-2026-pit-20260824t151559z-004"]
run_ids: ["20260824T151559Z"]
---

# Pittsburgh Steelers intelligence synthesis — 2026-08-24

## Executive signal

Pittsburgh held out Aaron Rodgers and Mason Rudolph, split reserve quarterback work by half, and
continued offensive-line rotation. The shutout and Kaleb Johnson's team-leading rushing line do
not resolve a regular-season role question.

## Reconciled evidence

One official recap supplies all four observations. Howard's two interceptions and Allar's uneven
second half occurred behind shuffled line combinations. Johnson's 10 carries and two receptions
lack a healthy first-team committee comparison.

## Hypothesis impact

No game-based change to `pit-2026-off-q02`, because Rodgers was deliberately held out. Johnson's
bounded usage is relevant to `pit-2026-off-q06`, but without Warren and Dowdle allocation it does
not identify a lead back. The reported line shuffling leaves `pit-2026-off-q08` open rather than
confirming instability.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Johnson led Pittsburgh with 10 carries and added two receptions in incomplete committee context. | obs-2026-pit-20260824t151559z-004 | Compare healthy first-team early-down, passing-down, and goal-line work. |
| log | Howard and Allar divided the reserve quarterback work while Rodgers and Rudolph rested. | obs-2026-pit-20260824t151559z-001; obs-2026-pit-20260824t151559z-002; obs-2026-pit-20260824t151559z-003 | No action beyond roster evaluation. |

## Conflicts and uncertainty

The recap does not supply full snap counts, stable offensive-line combinations, or comparable
first-team backfield usage.

## Excluded noise

The 17-0 result, isolated deep completion, and turnover totals were not treated as season-long
offensive evidence.

## Run metrics

- Raw observations: 4
- Unique evidence clusters: 4
- Repeats removed: 0
- Synthesis elapsed time: 6 minutes

## Sources

- Pittsburgh Steelers official recap, published 2026-08-21 at 10:15 PM ET and retrieved
  2026-08-24; observations `obs-2026-pit-20260824t151559z-001` through `-004`.
