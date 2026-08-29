---
schema_version: 1
record_id: ti-2026-det-20260829-001
record_type: team_intelligence
title: "Detroit Lions intelligence synthesis — 2026-08-29"
team_ids: ["DET"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-27
last_verified: 2026-08-29
confidence: high
source_ids: ["local-source-detroit-lions"]
supersedes: ["ti-2026-det-20260822-001"]
observation_ids: ["obs-2026-det-20260829t143349z-001", "obs-2026-det-20260829t143349z-002"]
run_ids: ["20260829T143349Z"]
---

# Detroit Lions intelligence synthesis — 2026-08-29

## Executive signal

Isiah Pacheco missed most of camp with a sprained MCL, also has a back injury, and has no definitive
return date. The official update materially weakens the assumption that he will open the season as a
healthy workload challenger to Jahmyr Gibbs.

## Reconciled evidence

Two atomic observations arise from one direct Dan Campbell update: the MCL diagnosis and the newer
back/return uncertainty. They are related components of one availability cluster, not independent
confirmation. There are no conflicts.

## Hypothesis impact

- `det-off-001`: **supports Gibbs volume and requires immediate review.** Pacheco's uncertain
  availability reduces the known competition for early-down and short-yardage work, though it does
  not establish Gibbs' Week 1 goal-line or passing-down share.
- Open ledger row `til-2026-det-20260822-001`: **trigger not occurred.** This batch contains no edge
  snaps, alignments, or pressure evidence, so ARCH should leave the edge review open.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| escalate | Pacheco has a sprained MCL plus a back injury and no definitive return date. | `obs-2026-det-20260829t143349z-001`; `obs-2026-det-20260829t143349z-002` | Update the Gibbs/Pacheco availability baseline and obtain the Week 1 practice report and final backfield roster before rankings lock. |

## Conflicts and uncertainty

Campbell supplied no return timetable or Week 1 designation. The source does not establish whether
another back inherits Pacheco's expected short-yardage role.

## Excluded noise

None.

## Run metrics

- Raw observations: 2
- Unique evidence clusters: 1
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing: 0 log, 0 review, 1 escalate
- Promotions: 0 (not authorized)
- Synthesis elapsed time: approximately 5 minutes

## Sources

- Detroit Lions — [Camp Notes: Campbell reflects on Lions' 2026 training camp](https://www.detroitlions.com/news/camp-notes-campbell-reflects-on-lions-2026-training-camp-hutchinson-pacheco) — published 2026-08-27T16:50:00-04:00; retrieved 2026-08-29T14:37:45Z; observations `obs-2026-det-20260829t143349z-001` and `obs-2026-det-20260829t143349z-002`.
