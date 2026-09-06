---
schema_version: 1
record_id: "ti-2026-sf-20260906-002"
record_type: "team_intelligence"
title: "San Francisco 49ers Week 1 readiness \u2014 2026-09-06"
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
observation_ids: ["obs-2026-sf-20260906t210715z-001", "obs-2026-sf-20260906t210715z-002"]
run_ids: ["20260906T210715Z"]
---

# San Francisco 49ers Week 1 readiness — 2026-09-06

## Executive signal

The roster transaction changes the available tight-end group without establishing Kittle clearance.

## Reconciled evidence

- `obs-2026-sf-20260906t210715z-001` — transaction; new. Read the atomic claim in the [reader batch](../../runs/20260906T210715Z/reader-sf/observations.csv).
- `obs-2026-sf-20260906t210715z-002` — transaction; new. Read the atomic claim in the [reader batch](../../runs/20260906T210715Z/reader-sf/observations.csv).

Read against [the earlier September 6 synthesis](SF.md). The overlapping window repairs missed access; it does not make repeated official statements independent evidence. New facts are retained once in the atomic batch.

## Hypothesis impact

sf-off-kittle-001 remains conditional. Existing open til-2026-sf-20260821-001 and til-2026-sf-20260829-001 remain open: neither Stribling usage nor the opening left guard was resolved.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Supplemental readiness review | `obs-2026-sf-20260906t210715z-001`; `obs-2026-sf-20260906t210715z-002` | Promoted the bounded checkpoint to `wm-2026-w01-sf-lar-001`. Kittle/Bosa completed team work and final status; opening left guard; Stribling routes. |

## Conflicts and uncertainty

The public injury-report page exposes no current Week 1 rows in this retrieval. Empty rendering does not prove no injuries or no published report. No final designation, route restriction, or game snap share is inferred. Kittle/Bosa completed team work and final status; opening left guard; Stribling routes.

## Excluded noise

Index headlines alone, promotional material, travel logistics and practice photographs do not establish a cleared player or a measured role. SF transaction observations share one origin. See source reports for endpoint-specific limitations.

## Run metrics

- Raw observations: 2
- Unique originating articles: 1
- Prior originating clusters excluded: 0
- Independent confirmations claimed: 0
- Synthesis elapsed time: not separately instrumented.
- [Source report](../../runs/20260906T210715Z/reader-sf/run-report.csv).

## Sources

- [local-source-san-francisco-49ers](https://www.49ers.com/news/49ers-promote-ls-jon-weeks-to-active-roster-waive-te-brayden-willis) — published 2026-09-05T22:00:23.793Z; retrieved 2026-09-06T21:15:39+00:00; `obs-2026-sf-20260906t210715z-001`.
- [local-source-san-francisco-49ers](https://www.49ers.com/news/49ers-promote-ls-jon-weeks-to-active-roster-waive-te-brayden-willis) — published 2026-09-05T22:00:23.793Z; retrieved 2026-09-06T21:15:39+00:00; `obs-2026-sf-20260906t210715z-002`.
