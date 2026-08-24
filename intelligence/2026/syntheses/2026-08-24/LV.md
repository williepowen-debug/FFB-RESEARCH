---
schema_version: 1
record_id: ti-2026-lv-20260824-001
record_type: team_intelligence
title: "Las Vegas Raiders intelligence synthesis — 2026-08-24"
team_ids: ["LV"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-24
last_verified: 2026-08-24
confidence: medium
source_ids: ["local-source-las-vegas-raiders"]
supersedes: []
observation_ids: ["obs-2026-lv-20260824t151559z-001", "obs-2026-lv-20260824t151559z-002", "obs-2026-lv-20260824t151559z-003", "obs-2026-lv-20260824t151559z-004"]
run_ids: ["20260824T151559Z"]
---

# Las Vegas Raiders intelligence synthesis — 2026-08-24

## Executive signal

Mike Washington Jr. produced another efficient preseason rushing line, while Fernando Mendoza and
Aidan O'Connell split the game-level quarterback work. Neither result establishes a first-team
regular-season role.

## Reconciled evidence

The team recap is the sole originating report. It supplies explicit reserve-opponent context for
Mendoza's pressure and describes O'Connell's late comeback drive. Washington's 56 yards on nine
carries and Dylan Laube's 37 yards on six carries are separate bounded production clusters.

## Hypothesis impact

No change to `lv-off-qb-001`: Mendoza starting a preseason game without evidence that Kirk Cousins'
regular-season role was reopened does not disconfirm the baseline. Washington's production is
directionally relevant to `lv-off-rb-001`, but it occurred before the later Jeanty practice exit and
does not supply first-team early-down, passing-down, goal-line, or two-minute allocation.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Washington produced 56 yards on nine carries in a strong second preseason rushing sample. | obs-2026-lv-20260824t151559z-002 | Retain the existing Jeanty health and first-team usage trigger. |
| log | Mendoza started before O'Connell handled the late comeback. | obs-2026-lv-20260824t151559z-001; obs-2026-lv-20260824t151559z-004 | Review only if Cousins loses first-team practice or game work. |

## Conflicts and uncertainty

The assigned evidence lacks full snap, route, protection-unit, and healthy-first-team backfield
context. The recap's positive framing is team-controlled.

## Excluded noise

The comeback result, Laube touchdown, and isolated late-drive execution do not alter a current
fantasy conclusion.

## Run metrics

- Raw observations: 4
- Unique evidence clusters: 4
- Repeats removed: 0
- Synthesis elapsed time: 7 minutes

## Sources

- Las Vegas Raiders official recap, published 2026-08-20 at 9:31 PM PT and retrieved 2026-08-24;
  observations `obs-2026-lv-20260824t151559z-001` through `-004`.
