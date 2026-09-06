---
schema_version: 1
record_id: "ti-2026-dal-20260906-001"
record_type: "team_intelligence"
title: "Dallas Cowboys intelligence synthesis — 2026-09-06"
team_ids: ["DAL"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-dallas-cowboys"]
supersedes: []
observation_ids: ["obs-2026-dal-20260906t193157z-001"]
run_ids: ["20260906T193157Z"]
---

# Dallas Cowboys intelligence synthesis — 2026-09-06

## Executive signal

The newly acquired Jones will compete with Steele at right tackle.

## Reconciled evidence

- `obs-2026-dal-20260906t193157z-001`: Dallas reported Schottenheimer will have Broderick Jones compete with Terence Steele at right tackle; no winner was announced.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

dal-off-ol-001 retains left-tackle risk and gains a separate right-tackle competition checkpoint.

Baseline read: `teams/NFC/East/Dallas-Cowboys/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-dal-20260829-001`.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | The newly acquired Jones will compete with Steele at right tackle. | `obs-2026-dal-20260906t193157z-001` | Promote bounded current state to `wm-2026-w01-dal-nyg-001`; Named opening tackle and pressure/protection sample. |

Treat right tackle as unsettled; a trade and coach competition statement do not establish improved protection.

## Conflicts and uncertainty

Named opening tackle and pressure/protection sample. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 1
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-dal/run-report.csv).

## Sources

- [local-source-dallas-cowboys](https://www.dallascowboys.com/news/mailbag-can-jones-compete-at-right-tackle) — published 2026-09-01T14:41:06.226Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-dal-20260906t193157z-001`.
