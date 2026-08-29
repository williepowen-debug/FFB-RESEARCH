---
schema_version: 1
record_id: ti-2026-lac-20260829-001
record_type: team_intelligence
title: "Los Angeles Chargers intelligence synthesis — 2026-08-29"
team_ids: ["LAC"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-29
last_verified: 2026-08-29
confidence: high
source_ids: ["local-source-los-angeles-chargers"]
supersedes: []
observation_ids: ["obs-2026-lac-20260829t143349z-001"]
run_ids: ["20260829T143349Z"]
---

# Los Angeles Chargers intelligence synthesis — 2026-08-29

## Executive signal

Justin Herbert connected with Quentin Johnston for a 65-yard touchdown in the preseason finale.
The play demonstrates a live vertical connection with the starting quarterback, but one target
does not establish Johnston's route or target concentration.

## Reconciled evidence

One official postgame report supplies the play result and coach/player reaction. No independent
origin, confirmation, update, or conflict was assigned.

## Hypothesis impact

The play directionally supports Johnston's perimeter and touchdown upside in
`rf-2026-lac-skill-usage-001` and provides one positive downfield result for
`rf-2026-lac-herbert-protection-001`. It does not change either finding without full first-unit
routes, targets, protection outcomes, and personnel context.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Herbert and Johnston connected for a 65-yard preseason touchdown. | `obs-2026-lac-20260829t143349z-001` | Chart Week 1 route share, targets, depth of target, and protection before changing Johnston or Herbert expectations. |

## Conflicts and uncertainty

The report does not supply Johnston's total routes or targets, the coverage, or Herbert's full
dropback and pressure sample.

## Excluded noise

Postgame praise and the isolated highlight were not treated as evidence of a stable target share.

## Run metrics

- Raw observations: 1
- Unique evidence clusters: 1
- Repeats removed: 0
- Routing: 1 log, 0 review, 0 escalate
- Promotions: 0
- Synthesis elapsed time: 3 minutes

## Sources

- Los Angeles Chargers, [5 Takeaways After Preseason Play](https://www.chargers.com/news/justin-herbert-53-man-roster-deadline), published 2026-08-28 at 10:30 AM ET and retrieved 2026-08-29 at 14:38 UTC; `obs-2026-lac-20260829t143349z-001`.
