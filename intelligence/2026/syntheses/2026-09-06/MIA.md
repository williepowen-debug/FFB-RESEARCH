---
schema_version: 1
record_id: ti-2026-mia-20260906-001
record_type: team_intelligence
title: "Miami Dolphins intelligence synthesis — 2026-09-06"
team_ids: ["MIA"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-09-06
last_verified: 2026-09-06
confidence: high
source_ids: ["local-source-miami-dolphins"]
supersedes: []
observation_ids: ["obs-2026-mia-20260906t193157z-001", "obs-2026-mia-20260906t193157z-002"]
run_ids: ["20260906T193157Z"]
---

# Miami Dolphins intelligence synthesis — 2026-09-06

## Executive signal

The receiver roster gate is resolved: Atwell is absent, Bell is included among seven initial-roster receivers, and Hunter is a practice-squad running back. This invalidates live Atwell opening-role projections without identifying a new target leader.

## Reconciled evidence

- `obs-2026-mia-20260906t193157z-001`: Miami signed running back Jarquez Hunter to its practice squad on August 31. Relationship: update of `obs-2026-mia-20260829t143349z-001`.
- `obs-2026-mia-20260906t193157z-002`: Miami kept seven initial-roster receivers: Tolbert, Washington, Douglas, Bell, Coleman, Miller and Henning; Tutu Atwell is absent. Relationship: update of `obs-2026-mia-20260829t143349z-001`.

## Hypothesis impact

Promote the roster checkpoint to `rf-2026-mia-wide-receiver-personnel-001` and linked receiver analyses. Invalidate `mia-2026-off-q09` and `mia-2026-off-q43`; narrow `mia-2026-off-q45` from reserve-status progression to measured offensive work. Preserve the prior analysis as explicitly dated history.

The prior open ledger row was reviewed. Its roster trigger has occurred and is promoted/resolved; the narrower unobserved Week 1 test continues in a new deferred row. No deployment inference is treated as resolved.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Receiver membership and Hunter position/roster correction | obs-2026-mia-20260906t193157z-001; obs-2026-mia-20260906t193157z-002 | Promote the roster correction; Chart Week 1 game-day receivers and first-unit routes; verify Bell participation and any Hunter elevation before assigning workload. |

## Conflicts and uncertainty

Initial membership is established. Receiver route shares, Bell full-contact readiness and game-day status, and Hunter elevation or workload are not. The two articles establish separate roster facts from one official ecosystem, not independent support for a usage prediction. Jackson access was incomplete (X 403 and a selected Herald article cache miss); no independent current beat body was admitted.

There are no conflicting admitted reports. Historical premises are retained as dated evidence; changed roster facts govern the active baseline.

## Excluded noise

No separate noise observations were admitted. Roster inclusion is not a route-share measurement, and repeated official confirmation is not independent corroboration.

## Run metrics

- Raw observations: 2.
- Unique evidence clusters: 2.
- Repeats removed: 0.
- Relationships: 2 updates; conflicts: 0.
- Routing: log 0; review 1; escalate 0.
- Synthesis elapsed time: not separately instrumented; included in the combined three-team reconciliation.
- Coverage: official items above; current beat retrieval incomplete. No claim of exhaustive archive coverage.

## Sources

- local-source-miami-dolphins — [supporting item](https://www.miamidolphins.com/news/dolphins-sign-nine-players-to-the-practice-squad); published `2026-08-31T19:09:10.322Z`; retrieved `2026-09-06T19:52:06+00:00`; `obs-2026-mia-20260906t193157z-001`.
- local-source-miami-dolphins — [supporting item](https://www.miamidolphins.com/news/miami-dolphins-set-initial-53-man-roster-for-2026); published `2026-08-30T22:35:30.556Z`; retrieved `2026-09-06T19:52:06+00:00`; `obs-2026-mia-20260906t193157z-002`.
