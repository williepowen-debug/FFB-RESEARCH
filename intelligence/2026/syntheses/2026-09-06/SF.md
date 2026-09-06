---
schema_version: 1
record_id: "ti-2026-sf-20260906-001"
record_type: "team_intelligence"
title: "San Francisco 49ers intelligence synthesis — 2026-09-06"
team_ids: ["SF"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-san-francisco-49ers"]
supersedes: []
observation_ids: ["obs-2026-sf-20260906t193157z-001", "obs-2026-sf-20260906t193157z-002", "obs-2026-sf-20260906t193157z-003"]
run_ids: ["20260906T193157Z"]
---

# San Francisco 49ers intelligence synthesis — 2026-09-06

## Executive signal

The club planned managed Kittle/Bosa work while left guard remained unsettled.

## Reconciled evidence

- `obs-2026-sf-20260906t193157z-001`: Shanahan planned managed practice work for George Kittle before departure, including progression toward team work.
- `obs-2026-sf-20260906t193157z-002`: Shanahan planned managed practice work for Nick Bosa before departure; the plan did not itself confirm Week 1 clearance.
- `obs-2026-sf-20260906t193157z-003`: Shanahan said left guard remained unsettled and planned to evaluate newly acquired Jarrett Patterson in the group.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

sf-off-kittle-001 remains conditional; sf-off-ol-001 and Stribling route hypotheses retain existing open triggers.

Baseline read: `teams/NFC/West/San-Francisco-49ers/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-sf-20260829-001`.

- Reviewed existing `til-2026-sf-20260821-001`: trigger remains unmet by this batch; retain Preseason route participation, snaps by quarterback unit, and red-zone usage.

- Reviewed existing `til-2026-sf-20260829-001`: trigger remains unmet by this batch; retain Opening left-guard lineup and protection assignments.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | The club planned managed Kittle/Bosa work while left guard remained unsettled. | `obs-2026-sf-20260906t193157z-001`; `obs-2026-sf-20260906t193157z-002`; `obs-2026-sf-20260906t193157z-003` | Promote bounded current state to `wm-2026-w01-sf-lar-001`; Completed team work, final game designations and named opening left guard. |

The plan updates the earlier Kittle concern but does not prove completed competitive work or a full route rate.

## Conflicts and uncertainty

Completed team work, final game designations and named opening left guard. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 3
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-sf/run-report.csv).

## Sources

- [local-source-san-francisco-49ers](https://www.49ers.com/news/5-takeaways-from-john-lynch-and-kyle-shanahan-ahead-of-australia) — published 2026-09-01T02:32:16.575Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-sf-20260906t193157z-001`, `obs-2026-sf-20260906t193157z-002`, `obs-2026-sf-20260906t193157z-003`.
