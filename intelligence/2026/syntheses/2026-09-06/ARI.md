---
schema_version: 1
record_id: "ti-2026-ari-20260906-001"
record_type: "team_intelligence"
title: "Arizona Cardinals intelligence synthesis — 2026-09-06"
team_ids: ["ARI"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-arizona-cardinals"]
supersedes: []
observation_ids: ["obs-2026-ari-20260906t193157z-001", "obs-2026-ari-20260906t193157z-002"]
run_ids: ["20260906T193157Z"]
---

# Arizona Cardinals intelligence synthesis — 2026-09-06

## Executive signal

Conner and Reiman moved onto reserve lists at cutdown.

## Reconciled evidence

- `obs-2026-ari-20260906t193157z-001`: Arizona placed James Conner on IR with a return designation; he must miss at least four games.
- `obs-2026-ari-20260906t193157z-002`: Arizona placed Tip Reiman on PUP at the initial-roster cutdown.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

ari-off-001 still depends on Love health. The Reiman official reserve transaction resolves the prior speculative availability checkpoint.

Baseline read: `teams/NFC/West/Arizona-Cardinals/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-ari-20260826-001`.

- Reviewed existing `til-2026-ari-20260821-002`: official reserve transaction resolves the Reiman availability question; weekly promotion is recorded separately.

- Reviewed existing `til-2026-ari-20260821-003`: trigger remains unmet by this batch; retain Return to practice, final depth chart, and Week 1 status.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| escalate | Conner and Reiman moved onto reserve lists at cutdown. | `obs-2026-ari-20260906t193157z-001`; `obs-2026-ari-20260906t193157z-002` | Promote bounded current state to `wm-2026-w01-ari-lac-001`; Love return and final status; Allgeier/Love/Knight deployment and TE routes. |

Remove both from immediate active-player plans; Love still requires his own health clearance and measured allocation.

## Conflicts and uncertainty

Love return and final status; Allgeier/Love/Knight deployment and TE routes. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 2
- Unique originating articles: 1
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-ari/run-report.csv).

## Sources

- [local-source-arizona-cardinals](https://www.azcardinals.com/news/cardinals-make-moves-to-get-to-initial-53-on-roster) — published 2026-08-30T22:11:00.17Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-ari-20260906t193157z-001`, `obs-2026-ari-20260906t193157z-002`.
