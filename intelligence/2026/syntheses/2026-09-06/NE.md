---
schema_version: 1
record_id: "ti-2026-ne-20260906-001"
record_type: "team_intelligence"
title: "New England Patriots intelligence synthesis — 2026-09-06"
team_ids: ["NE"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-new-england-patriots"]
supersedes: []
observation_ids: ["obs-2026-ne-20260906t193157z-001", "obs-2026-ne-20260906t193157z-002"]
run_ids: ["20260906T193157Z"]
---

# New England Patriots intelligence synthesis — 2026-09-06

## Executive signal

Landry is unavailable to open the season; Henderson still required assessment in the September 5 coach briefing.

## Reconciled evidence

- `obs-2026-ne-20260906t193157z-001`: Harold Landry will begin on reserve/PUP and miss at least four games.
- `obs-2026-ne-20260906t193157z-002`: On September 5 Vrabel said Henderson would be assessed at practice; the game-day backfield remained undecided.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

ne-2026-off-q06 and q07 remain conditional on both backs being available; Landry affects edge depth.

Baseline read: `teams/AFC/East/New-England-Patriots/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-ne-20260829-001`.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Landry is unavailable to open the season; Henderson still required assessment in the September 5 coach briefing. | `obs-2026-ne-20260906t193157z-001`; `obs-2026-ne-20260906t193157z-002` | Promote bounded current state to `wm-2026-w01-ne-sea-001`; Official Henderson participation and final designation before the September 9 opener. |

Prepare a Stevenson-heavy contingency if Henderson cannot play; no automatic workload upgrade while status remains unresolved.

## Conflicts and uncertainty

Official Henderson participation and final designation before the September 9 opener. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 2
- Unique originating articles: 2
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-ne/run-report.csv).

## Sources

- [local-source-new-england-patriots](https://www.patriots.com/news/analysis-breaking-down-the-patriots-initial-53-man-roster-for-the-2026-season) — published 2026-08-30T23:24:00Z; retrieved 2026-09-06T19:52:06+00:00; `obs-2026-ne-20260906t193157z-001`.
- [local-source-new-england-patriots](https://www.patriots.com/news/transcript-head-coach-mike-vrabel-press-conference-9-5-x4643) — published 2026-09-05T10:00:00Z; retrieved 2026-09-06T19:54:26+00:00; `obs-2026-ne-20260906t193157z-002`.
