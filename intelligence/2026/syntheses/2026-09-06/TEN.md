---
schema_version: 1
record_id: "ti-2026-ten-20260906-001"
record_type: "team_intelligence"
title: "Tennessee Titans intelligence synthesis — 2026-09-06"
team_ids: ["TEN"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-tennessee-titans"]
supersedes: []
observation_ids: ["obs-2026-ten-20260906t193157z-001", "obs-2026-ten-20260906t193157z-002"]
run_ids: ["20260906T193157Z"]
---

# Tennessee Titans intelligence synthesis — 2026-09-06

## Executive signal

Carmona received the opening RG job while Tate missed the observed stretching period.

## Reconciled evidence

- `obs-2026-ten-20260906t193157z-001`: Saleh named Fernando Carmona the starting right guard for Week 1.
- `obs-2026-ten-20260906t193157z-002`: Carnell Tate was not seen in September 1 stretching; Saleh attributed the absence to stiffness.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

ten-2026-off-q03 remains conditional. The existing allocation ledger still lacks first-read, target and passing-down evidence.

Baseline read: `teams/AFC/South/Tennessee-Titans/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-ten-20260829-001`.

- Reviewed existing `til-2026-ten-20260829-001`: trigger remains unmet by this batch; retain Week 1 routes targets first reads attendance context and passing-down snaps.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Carmona received the opening RG job while Tate missed the observed stretching period. | `obs-2026-ten-20260906t193157z-001`; `obs-2026-ten-20260906t193157z-002` | Promote bounded current state to `wm-2026-w01-nyj-ten-001`; Tate participation and Week 1 routes; Carmona first-game protection. |

The guard role is clearer; Tate status needs verification before treating expected routes as available.

## Conflicts and uncertainty

Tate participation and Week 1 routes; Carmona first-game protection. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 2
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-ten/run-report.csv).

## Sources

- [local-source-tennessee-titans](https://www.tennesseetitans.com/news/quick-hits-after-tuesday-s-titans-practice-x7053) — published 2026-09-01T20:25:10.848Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-ten-20260906t193157z-001`, `obs-2026-ten-20260906t193157z-002`.
