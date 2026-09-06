---
schema_version: 1
record_id: "ti-2026-lar-20260906-001"
record_type: "team_intelligence"
title: "Los Angeles Rams intelligence synthesis — 2026-09-06"
team_ids: ["LAR"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-los-angeles-rams"]
supersedes: []
observation_ids: ["obs-2026-lar-20260906t193157z-001", "obs-2026-lar-20260906t193157z-002", "obs-2026-lar-20260906t193157z-003"]
run_ids: ["20260906T193157Z"]
---

# Los Angeles Rams intelligence synthesis — 2026-09-06

## Executive signal

Donald, Garrett and Ferguson had separate ramp or practice limitations in the August 31 report.

## Reconciled evidence

- `obs-2026-lar-20260906t193157z-001`: McVay said Aaron Donald's missed Monday practice was planned; his Week 1 participation remained undecided.
- `obs-2026-lar-20260906t193157z-002`: Myles Garrett remained out of individual and team drills on August 31, with McVay targeting Australia.
- `obs-2026-lar-20260906t193157z-003`: Terrance Ferguson worked with trainers rather than practicing August 31; McVay attributed the caution to soreness.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

lar-off-te-001 remains a personnel hypothesis; Ferguson absence can affect TE allocation without proving a new package rate.

Baseline read: `teams/NFC/West/Los-Angeles-Rams/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-lar-20260822-001`.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Donald, Garrett and Ferguson had separate ramp or practice limitations in the August 31 report. | `obs-2026-lar-20260906t193157z-001`; `obs-2026-lar-20260906t193157z-002`; `obs-2026-lar-20260906t193157z-003` | Promote bounded current state to `wm-2026-w01-sf-lar-001`; Final Week 1 designations and expected workloads for all three. |

Treat the Australia personnel projection as conditional; a travel or recovery plan is not game clearance.

## Conflicts and uncertainty

Final Week 1 designations and expected workloads for all three. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 3
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-lar/run-report.csv).

## Sources

- [local-source-los-angeles-rams](https://www.therams.com/news/injury-updates-aaron-donald-not-practicing-monday-part-of-the-plan-all-along-myles-garrett-making-really-good-progress-and-updates-on-terrance-ferguson-grant-stuard-keagen-trost-and-justin-dedich) — published 2026-09-01T02:03:22.449Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-lar-20260906t193157z-001`, `obs-2026-lar-20260906t193157z-002`, `obs-2026-lar-20260906t193157z-003`.
