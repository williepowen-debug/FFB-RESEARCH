---
schema_version: 1
record_id: "ti-2026-pit-20260906-001"
record_type: "team_intelligence"
title: "Pittsburgh Steelers intelligence synthesis — 2026-09-06"
team_ids: ["PIT"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-pittsburgh-steelers"]
supersedes: []
observation_ids: ["obs-2026-pit-20260906t193157z-001", "obs-2026-pit-20260906t193157z-002"]
run_ids: ["20260906T193157Z"]
---

# Pittsburgh Steelers intelligence synthesis — 2026-09-06

## Executive signal

The cutdown trades remove Kaleb Johnson from the projected committee and send Broderick Jones to Dallas.

## Reconciled evidence

- `obs-2026-pit-20260906t193157z-001`: Pittsburgh agreed to trade tackle Broderick Jones to Dallas with draft-pick compensation, pending a physical.
- `obs-2026-pit-20260906t193157z-002`: Pittsburgh agreed to trade running back Kaleb Johnson to Green Bay for a 2028 sixth-round pick, pending a physical.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

pit-2026-off-q06 must drop the three-way Warren/Dowdle/Johnson premise.

Baseline read: `teams/AFC/North/Pittsburgh-Steelers/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-pit-20260829-001`.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | The cutdown trades remove Kaleb Johnson from the projected committee and send Broderick Jones to Dallas. | `obs-2026-pit-20260906t193157z-001`; `obs-2026-pit-20260906t193157z-002` | Promote bounded current state to `wm-2026-w01-atl-pit-001`; Warren/Dowdle early-down, passing-down and goal-line split; starting protection group. |

Reframe Pittsburgh RB allocation around Warren and Dowdle without naming a bell cow; monitor tackle cover.

Canonical promotion: `rf-2026-pit-backfield-committee-002` at `teams/AFC/North/Pittsburgh-Steelers/2026/offense/backfield-committee-002.md`. Replaced and archived the disproved immediate backfield premise; workload percentages remain unmeasured.

Canonical promotion: `pit-2026-off-q06` at `teams/AFC/North/Pittsburgh-Steelers/2026/offense/hypotheses.csv`. Removed Johnson from the live committee candidates without assigning the vacated work.

Canonical promotion: `to-2026-pit-overview-001` at `teams/AFC/North/Pittsburgh-Steelers/2026/overview.md`. Aligned the overview with the revised backfield finding.

## Conflicts and uncertainty

Warren/Dowdle early-down, passing-down and goal-line split; starting protection group. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 2
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-pit/run-report.csv).

## Sources

- [local-source-pittsburgh-steelers](https://www.steelers.com/news/steelers-make-two-trades-as-part-of-final-roster-moves) — published 2026-08-30T22:27:00Z; retrieved 2026-09-06T19:52:06+00:00; `obs-2026-pit-20260906t193157z-001`, `obs-2026-pit-20260906t193157z-002`.
