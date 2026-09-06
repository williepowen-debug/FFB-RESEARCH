---
schema_version: 1
record_id: "ti-2026-ind-20260906-001"
record_type: "team_intelligence"
title: "Indianapolis Colts intelligence synthesis — 2026-09-06"
team_ids: ["IND"]
player_ids: []
season: 2026
week: null
status: "active"
time_horizon: "seasonal"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-indianapolis-colts"]
supersedes: []
observation_ids: ["obs-2026-ind-20260906t193157z-001"]
run_ids: ["20260906T193157Z"]
---

# Indianapolis Colts intelligence synthesis — 2026-09-06

## Executive signal

Richardson is the announced backup behind Jones.

## Reconciled evidence

- `obs-2026-ind-20260906t193157z-001`: Indianapolis named Anthony Richardson Sr. its backup quarterback, ahead of Riley Leonard and behind Daniel Jones.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

ind-off-qb-001 remains about Jones readiness, not the now-settled QB2 order.

Baseline read: `teams/AFC/South/Indianapolis-Colts/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-ind-20260824-001`.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Richardson is the announced backup behind Jones. | `obs-2026-ind-20260906t193157z-001` | Log context; Jones availability and any explicit backup package. |

Useful contingency ordering; it does not change the starting quarterback or establish designed packages.

## Conflicts and uncertainty

Jones availability and any explicit backup package. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 1
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-ind/run-report.csv).

## Sources

- [local-source-indianapolis-colts](https://www.colts.com/news/anthony-richardson-sr-named-colts-backup-quarterback) — published 2026-09-03T15:26:48.596Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-ind-20260906t193157z-001`.
