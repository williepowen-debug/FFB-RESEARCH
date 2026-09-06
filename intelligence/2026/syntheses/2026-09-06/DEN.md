---
schema_version: 1
record_id: "ti-2026-den-20260906-001"
record_type: "team_intelligence"
title: "Denver Broncos intelligence synthesis — 2026-09-06"
team_ids: ["DEN"]
player_ids: []
season: 2026
week: null
status: "active"
time_horizon: "seasonal"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-denver-broncos"]
supersedes: []
observation_ids: ["obs-2026-den-20260906t193157z-001"]
run_ids: ["20260906T193157Z"]
---

# Denver Broncos intelligence synthesis — 2026-09-06

## Executive signal

Denver kept Badie over McLaughlin with special teams cited.

## Reconciled evidence

- `obs-2026-den-20260906t193157z-001`: Denver waived Jaleel McLaughlin and retained Tyler Badie, with Payton citing special-teams considerations.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

den-off-rb-001, den-off-qb-001 and den-off-wr-001 retain their existing open evidence triggers.

Baseline read: `teams/AFC/West/Denver-Broncos/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-den-20260822-001`.

- Reviewed existing `til-2026-den-20260822-001`: trigger remains unmet by this batch; retain Next practice and game availability plus designed movement, scramble behavior, and full first-team operation.

- Reviewed existing `til-2026-den-20260822-002`: trigger remains unmet by this batch; retain First-team routes, targets, alignments, and first-read charting relative to Sutton, Mims, and Engram.

- Reviewed existing `til-2026-den-20260822-003`: trigger remains unmet by this batch; retain First-team early-down, passing-down, two-minute, and goal-line work for Dobbins, Harvey, and Coleman.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Denver kept Badie over McLaughlin with special teams cited. | `obs-2026-den-20260906t193157z-001` | Log context; Healthy-back split, Nix functional mobility and receiver distribution. |

A depth transaction does not settle the Dobbins/Harvey/Coleman usage contest.

## Conflicts and uncertainty

Healthy-back split, Nix functional mobility and receiver distribution. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 1
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-den/run-report.csv).

## Sources

- [local-source-denver-broncos](https://www.denverbroncos.com/news/we-re-pleased-with-what-transpired-in-the-last-24-hours-hc-sean-payton-offers-insight-into-roster-moves-after-broncos-set-initial-53-man-roster-practice-squad) — published 2026-09-01T00:35:44.457Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-den-20260906t193157z-001`.
