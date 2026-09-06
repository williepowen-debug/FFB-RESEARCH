---
schema_version: 1
record_id: "ti-2026-bal-20260906-001"
record_type: "team_intelligence"
title: "Baltimore Ravens intelligence synthesis — 2026-09-06"
team_ids: ["BAL"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-baltimore-ravens"]
supersedes: []
observation_ids: ["obs-2026-bal-20260906t193157z-001"]
run_ids: ["20260906T193157Z"]
---

# Baltimore Ravens intelligence synthesis — 2026-09-06

## Executive signal

Flowers returned to practice, clearing an attendance checkpoint.

## Reconciled evidence

- `obs-2026-bal-20260906t193157z-001`: Zay Flowers returned to practice September 3 after missing roughly two weeks.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

bal-2026-off-q03 remains the target baseline; the new report supports availability rather than target-share measurement.

Baseline read: `teams/AFC/North/Baltimore-Ravens/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-bal-20260824-001`.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Flowers returned to practice, clearing an attendance checkpoint. | `obs-2026-bal-20260906t193157z-001` | Promote bounded current state to `wm-2026-w01-bal-ind-001`; Flowers final Week 1 report and route participation. |

Preserve the Flowers target-lead premise while checking workload and designation; attendance alone does not prove unrestricted routes.

## Conflicts and uncertainty

Flowers final Week 1 report and route participation. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 1
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-bal/run-report.csv).

## Sources

- [local-source-baltimore-ravens](https://www.baltimoreravens.com/news/zay-flowers-returns-ravens-practice-wide-receiver-injury) — published 2026-09-03T17:03:22.348Z; retrieved 2026-09-06T19:52:06+00:00; `obs-2026-bal-20260906t193157z-001`.
