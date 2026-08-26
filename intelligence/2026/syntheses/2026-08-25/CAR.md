---
schema_version: 1
record_id: ti-2026-car-20260825-001
record_type: team_intelligence
title: "Carolina Panthers intelligence synthesis — 2026-08-25"
team_ids: ["CAR"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-24
last_verified: 2026-08-25
confidence: high
source_ids: ["local-writer-darin-gantt"]
supersedes: []
observation_ids: ["obs-2026-car-20260825t223141z-001", "obs-2026-car-20260825t223141z-002"]
run_ids: ["20260825T223141Z"]
---

# Carolina Panthers intelligence synthesis — 2026-08-25

## Executive signal

Darren Waller completed his first Panthers practice on August 24, satisfying the first checkpoint
in Carolina's open Waller ledger review. His individual work and limited team exposure establish
progress through the ramp, but they do not establish a regular-season receiving role. The prior
checkpoint closes as a completed no-change review, while a narrower Week 1 usage review remains
open. No signal reaches the escalation or canonical-promotion threshold.

## Reconciled evidence

The official team notebook reports that Waller participated in individual drills and was mixed
into some team periods (`obs-2026-car-20260825t223141z-001`). It separately reports a plan for
more work in the August 26 joint practice and likely no preseason-finale appearance because he had
only one practice week (`obs-2026-car-20260825t223141z-002`). These are two claims from one
team-controlled origin, not independent confirmation. The first updates the August 22 observation
that Waller had not yet practiced; the second defines the next evaluation point.

## Hypothesis impact

- `car-2026-off-q04`: **first-practice trigger occurred; no conclusion change.** Waller advanced
  from return-to-play work into a real practice, but the source explicitly lacks a team-period
  target and supplies no route share, red-zone, third-down, or personnel-group evidence.
- `til-2026-car-20260822-003`: close as `no_change` / `resolved`. The named first-practice
  checkpoint was reviewed without enough evidence to alter the seasonal hypothesis.
- Continue review only for the August 26 joint-practice workload, final roster status, and early
  Week 1 route, target, red-zone, and third-down usage.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Waller completed his first practice but remained in a limited ramp with no documented team-period target. | `obs-2026-car-20260825t223141z-001`; `obs-2026-car-20260825t223141z-002` | Review measured joint-practice or Week 1 usage before changing `car-2026-off-q04`. |

Routing totals: zero `log`, one `review`, and zero `escalate` signals.

## Conflicts and uncertainty

There is no contradiction, but the evidence comes from one team-controlled notebook. Waller's
eventual roster position is likely but not decided by this source, and his route share, target
priority, red-zone involvement, third-down work, and blocking burden remain unknown.

## Excluded noise

Positive descriptions of Waller's conditioning and routes versus air were excluded from role
conclusions because they are qualitative and lack competitive or measured context.

## Run metrics

- Raw observations: 2
- Unique evidence clusters: 2
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing: 0 log, 1 review, 0 escalate
- Promotions: 0
- Synthesis elapsed time: approximately 8 minutes

## Sources

- Darin Gantt and Kassidy Hill, Carolina Panthers — [Training Camp Observations: Joint practice will determine workload in finale](https://www.panthers.com/news/training-camp-observations-joint-practice-will-determine-workload-in-finale) — published 2026-08-24T13:39:00-04:00; retrieved 2026-08-25T22:31:41Z; observations `obs-2026-car-20260825t223141z-001` and `obs-2026-car-20260825t223141z-002`.
