---
schema_version: 1
record_id: "ti-2026-buf-20260906-001"
record_type: "team_intelligence"
title: "Buffalo Bills intelligence synthesis — 2026-09-06"
team_ids: ["BUF"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-buffalo-bills"]
supersedes: []
observation_ids: ["obs-2026-buf-20260906t193157z-001", "obs-2026-buf-20260906t193157z-002"]
run_ids: ["20260906T193157Z"]
---

# Buffalo Bills intelligence synthesis — 2026-09-06

## Executive signal

Buffalo has a confirmed interior-DL absence and an unresolved linebacker practice checkpoint.

## Reconciled evidence

- `obs-2026-buf-20260906t193157z-001`: Buffalo placed Zane Durant on IR; Beane said the neck stinger will cost him at least the first four games.
- `obs-2026-buf-20260906t193157z-002`: Terrel Bernard missed September 1 practice; Beane remained hopeful for Week 1 without declaring him available.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

Defensive personnel availability changes; the Cook and receiving workload hypotheses receive no new usage evidence.

Baseline read: `teams/AFC/East/Buffalo-Bills/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-buf-20260824-001`.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Buffalo has a confirmed interior-DL absence and an unresolved linebacker practice checkpoint. | `obs-2026-buf-20260906t193157z-001`; `obs-2026-buf-20260906t193157z-002` | Promote bounded current state to `wm-2026-w01-buf-hou-001`; First Week 1 practice report and Bernard game status. |

Recheck Buffalo defensive availability before assessing Houston efficiency; do not infer a unit-wide downgrade from two names.

## Conflicts and uncertainty

First Week 1 practice report and Bernard game status. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 2
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-buf/run-report.csv).

## Sources

- [local-source-buffalo-bills](https://www.buffalobills.com/news/bills-gm-brandon-beane-provides-team-injury-updates-prior-to-week-1-of-2026-season) — published 2026-09-01T21:52:30.295Z; retrieved 2026-09-06T19:52:06+00:00; `obs-2026-buf-20260906t193157z-001`, `obs-2026-buf-20260906t193157z-002`.
