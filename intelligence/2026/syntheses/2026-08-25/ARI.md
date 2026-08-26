---
schema_version: 1
record_id: ti-2026-ari-20260825-001
record_type: team_intelligence
title: "Arizona Cardinals intelligence synthesis — 2026-08-25"
team_ids: ["ARI"]
player_ids: ["local-player-jeremiyah-love-2026", "local-player-josh-sweat-2018"]
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-24
last_verified: 2026-08-25
confidence: high
source_ids: ["local-source-arizona-cardinals"]
supersedes: ["ti-2026-ari-20260824-001"]
observation_ids: ["obs-2026-ari-20260826t011902z-001", "obs-2026-ari-20260826t011902z-002"]
run_ids: ["20260826T011902Z"]
---

# Arizona Cardinals intelligence synthesis — 2026-08-25

## Executive signal

Arizona activated Josh Sweat from PUP and waived/injured Trey Benson with a knee injury on August
24. Sweat's transaction closes the open activation checkpoint without proving pass-rush quality.
Benson's removal materially narrows the running-back room, but Jeremiyah Love's health and the
opening workload remain unresolved.

## Reconciled evidence

Both claims come from Arizona's official transaction ledger. They are distinct roster events from
one team-controlled source, not independent confirmation. The ledger supplies transaction dates
but no publication times or recovery timetables.

## Hypothesis impact

- `ari-def-003`: **supports availability, not performance.** Sweat is now eligible to practice and
  play, closing the previous PUP trigger.
- `ari-off-001`: **supports a clearer opportunity path.** Benson is no longer part of the immediate
  roster competition, but Love still must clear his ankle issue and earn high-value work.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Sweat activated from PUP. | `obs-2026-ari-20260826t011902z-001` | Promote the availability fact and review Week 1 participation. |
| escalate | Benson waived/injured, narrowing the running-back room. | `obs-2026-ari-20260826t011902z-002` | Update the backfield baseline and draft-facing monitoring. |

## Conflicts and uncertainty

The transaction page gives no Sweat practice workload and no Benson recovery timetable. Love's
ankle status and the Allgeier/Conner/Love order remain open.

## Excluded noise

No admissible Jeremiyah Love update was found. Unregistered aggregation was excluded.

## Run metrics

- Raw observations: 2
- Unique evidence clusters: 2
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing: 0 log, 1 review, 1 escalate
- Promotions: 2
- Synthesis elapsed time: approximately 6 minutes

## Sources

- Arizona Cardinals — [2026 transactions](https://www.azcardinals.com/team/transactions/2026) — dated 2026-08-24; retrieved 2026-08-26T01:25:51Z; observations `obs-2026-ari-20260826t011902z-001` and `obs-2026-ari-20260826t011902z-002`.
