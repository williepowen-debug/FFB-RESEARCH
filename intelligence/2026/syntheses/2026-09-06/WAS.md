---
schema_version: 1
record_id: "ti-2026-was-20260906-001"
record_type: "team_intelligence"
title: "Washington Commanders intelligence synthesis — 2026-09-06"
team_ids: ["WAS"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-washington-commanders"]
supersedes: []
observation_ids: ["obs-2026-was-20260906t193157z-001", "obs-2026-was-20260906t193157z-002"]
run_ids: ["20260906T193157Z"]
---

# Washington Commanders intelligence synthesis — 2026-09-06

## Executive signal

Tunsil and Newton went to IR.

## Reconciled evidence

- `obs-2026-was-20260906t193157z-001`: Washington placed left tackle Laremy Tunsil on injured reserve on August 31.
- `obs-2026-was-20260906t193157z-002`: Washington placed defensive tackle Jer'Zhan Newton on injured reserve on August 31.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

was-off-001 faces a protection constraint. The existing was-def-001 measured pressure trigger remains open.

Baseline read: `teams/NFC/East/Washington-Commanders/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-was-20260822-001`.

- Reviewed existing `til-2026-was-20260822-001`: trigger remains unmet by this batch; retain Gamebook or film-based pressure chart, first-team edge snaps, and four-man-versus-blitz results.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| escalate | Tunsil and Newton went to IR. | `obs-2026-was-20260906t193157z-001`; `obs-2026-was-20260906t193157z-002` | Promote bounded current state to `wm-2026-w01-was-phi-001`; Opening left tackle, protection assignments and interior-DL rotation. |

The opening protection and interior-DL personnel assumptions need adjustment; no numerical efficiency or DST change is established.

## Conflicts and uncertainty

Opening left tackle, protection assignments and interior-DL rotation. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 2
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-was/run-report.csv).

## Sources

- [local-source-washington-commanders](https://www.commanders.com/news/commanders-place-tunsil-newton-on-ir-sign-moreau-tuttle) — published 2026-08-31T20:29:18.638Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-was-20260906t193157z-001`, `obs-2026-was-20260906t193157z-002`.
