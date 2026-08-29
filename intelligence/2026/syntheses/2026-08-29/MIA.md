---
schema_version: 1
record_id: ti-2026-mia-20260829-001
record_type: team_intelligence
title: "Miami Dolphins intelligence synthesis — 2026-08-29"
team_ids: ["MIA"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-29
last_verified: 2026-08-29
confidence: high
source_ids: ["local-writer-barry-jackson"]
supersedes: ["ti-2026-mia-20260824-001"]
observation_ids: ["obs-2026-mia-20260829t143349z-001"]
run_ids: ["20260829T143349Z"]
---

# Miami Dolphins intelligence synthesis — 2026-08-29

## Executive signal

Miami traded Tutu Atwell to the Rams for running back Jarquez Hunter. The move removes one veteran
from an already unsettled receiver competition and adds another back behind De'Von Achane, but it
does not establish Hunter's offensive role.

## Reconciled evidence

One Miami Herald report, available through an attributed syndication copy, supplies the only
originating claim. No independent observation was assigned, and no conflict was found.

## Hypothesis impact

The transaction challenges the roster baseline in `rf-2026-mia-wide-receiver-veterans-001` and
`rf-2026-mia-wide-receiver-personnel-001`, which included Atwell in the veteran competition.
It also adds an unresolved backfield candidate, but one transaction does not change the established
Achane usage finding.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Atwell exits the receiver competition and Hunter joins Miami's backfield. | `obs-2026-mia-20260829t143349z-001` | Confirm final-roster placement, then update the receiver personnel baseline and chart Hunter's practice and Week 1 role. |

## Conflicts and uncertainty

The report does not establish Hunter's place relative to Jaylen Wright, Ollie Gordon II, or Carlos
Washington Jr. Final roster decisions and regular-season participation are still required.

## Excluded noise

The scouting description and college efficiency included in the report were excluded from the
role decision because they do not establish Miami usage.

## Run metrics

- Raw observations: 1
- Unique evidence clusters: 1
- Repeats removed: 0
- Routing: 0 log, 1 review, 0 escalate
- Promotions: 0
- Synthesis elapsed time: 4 minutes

## Sources

- Barry Jackson, Miami Herald, [Atwell-Hunter trade report](https://www.aol.com/articles/dolphins-trade-atwell-running-back-192133000.html), published 2026-08-27 at 19:21 UTC and retrieved 2026-08-29 at 14:38 UTC; `obs-2026-mia-20260829t143349z-001`.
