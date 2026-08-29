---
schema_version: 1
record_id: ti-2026-dal-20260829-001
record_type: team_intelligence
title: "Dallas Cowboys intelligence synthesis — 2026-08-29"
team_ids: ["DAL"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-28
last_verified: 2026-08-29
confidence: high
source_ids: ["local-source-dallas-cowboys"]
supersedes: ["ti-2026-dal-20260824-001"]
observation_ids: ["obs-2026-dal-20260829t143349z-001"]
run_ids: ["20260829T143349Z"]
---

# Dallas Cowboys intelligence synthesis — 2026-08-29

## Executive signal

Phil Mafah handled the largest workload in the preseason finale while Javonte Williams, Malik Davis,
and Jaydon Blue sat. This is roster-bubble usage, not evidence against Williams' established lead-back
baseline or proof of the reserve order.

## Reconciled evidence

One official, measured game cluster reports Mafah's start and 12 carries for 46 yards together with the
three veteran/priority backs being held out. There are no independent confirmations or conflicts.

## Hypothesis impact

- `dal-off-rb-001`: **no change.** Protecting Williams is consistent with his lead role, but the finale
  supplies no first-team early-down, passing-down, or goal-line split.

Dallas has no intelligence ledger, so no prior open trigger required disposition.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Mafah led the finale workload while Williams, Davis, and Blue sat. | `obs-2026-dal-20260829t143349z-001` | Check the final 53 and Week 1 high-value-touch split. |

## Conflicts and uncertainty

The source does not say every scratch was roster-safe, and backup-level preseason volume cannot settle
the regular-season backfield hierarchy.

## Excluded noise

The implied roster safety of all three inactive backs was excluded because the source framed it as
uncertain.

## Run metrics

- Raw observations: 1
- Unique evidence clusters: 1
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing: 1 log, 0 review, 0 escalate
- Promotions: 0 (not authorized)
- Synthesis elapsed time: approximately 4 minutes

## Sources

- Dallas Cowboys — [Updates: Mafah's bid to make final impression](https://www.dallascowboys.com/news/updates-offseason-2026) — update published 2026-08-28T22:43:00-05:00; retrieved 2026-08-29T14:37:45Z; observation `obs-2026-dal-20260829t143349z-001`.
