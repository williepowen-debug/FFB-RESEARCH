---
schema_version: 1
record_id: "ti-2026-det-20260906-001"
record_type: "team_intelligence"
title: "Detroit Lions intelligence synthesis — 2026-09-06"
team_ids: ["DET"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-detroit-lions"]
supersedes: []
observation_ids: ["obs-2026-det-20260906t193157z-001"]
run_ids: ["20260906T193157Z"]
---

# Detroit Lions intelligence synthesis — 2026-09-06

## Executive signal

Pacheco IR replaces the earlier uncertain-opening-status premise.

## Reconciled evidence

- `obs-2026-det-20260906t193157z-001`: Detroit placed Isiah Pacheco on IR; he will miss at least four games and the GM supplied no return date.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

det-off-001 receives directional support without measured volume proof. The existing edge-rotation ledger has no new snap evidence.

Baseline read: `teams/NFC/North/Detroit-Lions/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-det-20260829-001`.

- Reviewed existing `til-2026-det-20260822-001`: trigger remains unmet by this batch; retain Edge snaps, third-down rush packages, alignments, and pressures alongside Hutchinson.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| escalate | Pacheco IR replaces the earlier uncertain-opening-status premise. | `obs-2026-det-20260906t193157z-001` | Promote bounded current state to `wm-2026-w01-no-det-001`; Remaining-back goal-line and passing-down roles; later Pacheco return transaction. |

Pacheco is unavailable in Week 1; Gibbs has less known competition, but remaining complementary work must still be charted.

## Conflicts and uncertainty

Remaining-back goal-line and passing-down roles; later Pacheco return transaction. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. The inspected Woodyard article repeats the official IR event and was not admitted as independent evidence.

## Run metrics

- Raw observations: 1
- Unique originating articles: 1
- Repeats removed: 1
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-det/run-report.csv).

## Sources

- [local-source-detroit-lions](https://www.detroitlions.com/news/10-takeaways-from-brad-holmes-and-ray-agnew-gill-howard-oneill-goff) — published 2026-09-02T17:36:37.192Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-det-20260906t193157z-001`.
