---
schema_version: 1
record_id: "ti-2026-lar-20260906-002"
record_type: "team_intelligence"
title: "Los Angeles Rams Week 1 readiness \u2014 2026-09-06"
team_ids: ["LAR"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-los-angeles-rams", "local-writer-sarah-barshop"]
supersedes: []
observation_ids: ["obs-2026-lar-20260906t210715z-001", "obs-2026-lar-20260906t210715z-002"]
run_ids: ["20260906T210715Z"]
---

# Los Angeles Rams Week 1 readiness — 2026-09-06

## Executive signal

Nacua returned to practice; retain a separate final-status and workload checkpoint.

## Reconciled evidence

- `obs-2026-lar-20260906t210715z-001` — availability; update. Read the atomic claim in the [reader batch](../../runs/20260906T210715Z/reader-lar/observations.csv).
- `obs-2026-lar-20260906t210715z-002` — practice_participation; new. Read the atomic claim in the [reader batch](../../runs/20260906T210715Z/reader-lar/observations.csv).

Read against [the earlier September 6 synthesis](LAR.md). The overlapping window repairs missed access; it does not make repeated official statements independent evidence. New facts are retained once in the atomic batch.

## Hypothesis impact

lar-off-te-001 receives no measured personnel evidence. The dated Donald update does not resolve Garrett/Ferguson availability.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Supplemental readiness review | `obs-2026-lar-20260906t210715z-001`; `obs-2026-lar-20260906t210715z-002` | Promoted the bounded checkpoint to `wm-2026-w01-sf-lar-001`. Final designations and workload restrictions for Nacua, Donald, Garrett and Ferguson. |

## Conflicts and uncertainty

The public injury-report page exposes no current Week 1 rows in this retrieval. Empty rendering does not prove no injuries or no published report. No final designation, route restriction, or game snap share is inferred. Final designations and workload restrictions for Nacua, Donald, Garrett and Ferguson.

## Excluded noise

Index headlines alone, promotional material, travel logistics and practice photographs do not establish a cleared player or a measured role. SF transaction observations share one origin. See source reports for endpoint-specific limitations.

## Run metrics

- Raw observations: 2
- Unique originating articles: 2
- Prior originating clusters excluded: 0
- Independent confirmations claimed: 0
- Synthesis elapsed time: not separately instrumented.
- [Source report](../../runs/20260906T210715Z/reader-lar/run-report.csv).

## Sources

- [local-source-los-angeles-rams](https://www.therams.com/news/first-look-rams-take-on-49ers-in-australia-to-kick-off-2026-season) — published 2026-09-04T18:37:11.877Z; retrieved 2026-09-06T21:15:39+00:00; `obs-2026-lar-20260906t210715z-001`.
- [local-writer-sarah-barshop](https://www.espn.com/nfl/story/_/id/49826940/rams-plan-bring-entire-team-season-opener-including-donald) — published 2026-09-04T14:37:00-04:00; retrieved 2026-09-06T21:15:39+00:00; `obs-2026-lar-20260906t210715z-002`.
