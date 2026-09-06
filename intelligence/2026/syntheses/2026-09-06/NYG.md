---
schema_version: 1
record_id: ti-2026-nyg-20260906-001
record_type: team_intelligence
title: "New York Giants intelligence synthesis — 2026-09-06"
team_ids: ["NYG"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-09-06
last_verified: 2026-09-06
confidence: high
source_ids: ["local-source-new-york-giants"]
supersedes: []
observation_ids: ["obs-2026-nyg-20260906t193157z-001", "obs-2026-nyg-20260906t193157z-002"]
run_ids: ["20260906T193157Z"]
---

# New York Giants intelligence synthesis — 2026-09-06

## Executive signal

Zvada's job and roster place are confirmed. Promote him as the current rostered kicker and close the old competition/roster gate; retain routine Week 1 active-status verification.

## Reconciled evidence

- `obs-2026-nyg-20260906t193157z-001`: Schoen reaffirmed that Dominic Zvada had won the Giants kicking competition. Relationship: confirm of `obs-2026-nyg-20260829t143349z-002`.
- `obs-2026-nyg-20260906t193157z-002`: The Giants roster announcement includes Dominic Zvada and reports Ben Sauls waived with an injury settlement. Relationship: confirm of `obs-2026-nyg-20260829t143349z-002`.

## Hypothesis impact

Update `to-2026-nyg-overview-001` special teams. This resolves the roster portion of `til-2026-nyg-20260829-001`; it does not project kick volume or establish game-day active status.

The prior open ledger row was reviewed. Its roster trigger has occurred and is promoted/resolved; the narrower unobserved Week 1 test continues in a new deferred row. No deployment inference is treated as resolved.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Zvada kicking job and roster confirmation | obs-2026-nyg-20260906t193157z-001; obs-2026-nyg-20260906t193157z-002 | Promote the roster correction; Verify the Week 1 active list and any intervening specialist transaction before using Zvada in a lineup. |

## Conflicts and uncertainty

Both official items reflect the same kicker decision and roster follow-through. They are one consolidated kicker signal, not independent performance confirmation. Game-day active status and scoring opportunity remain unverified. Raanan's bio endpoint was readable, but no current original beat article was admitted.

There are no conflicting admitted reports. Historical premises are retained as dated evidence; changed roster facts govern the active baseline.

## Excluded noise

No separate noise observations were admitted. Roster inclusion is not a route-share measurement, and repeated official confirmation is not independent corroboration.

## Run metrics

- Raw observations: 2.
- Unique evidence clusters: 1.
- Repeats removed: 0; NYG official follow-through is grouped into one decision signal.
- Relationships: 2 confirmations; conflicts: 0.
- Routing: log 0; review 1; escalate 0.
- Synthesis elapsed time: not separately instrumented; included in the combined three-team reconciliation.
- Coverage: official items above; current beat retrieval incomplete. No claim of exhaustive archive coverage.

## Sources

- local-source-new-york-giants — [supporting item](https://www.giants.com/news/presser-points-gm-joe-schoen-previews-season-2026-john-harbaugh-deonte-banks-dominic-zvada); published `2026-09-02T18:15:00Z`; retrieved `2026-09-06T19:52:07+00:00`; `obs-2026-nyg-20260906t193157z-001`.
- local-source-new-york-giants — [supporting item](https://www.giants.com/news/roster-update-giants-announce-initial-53-man-roster-for-2026-nfl-season-week-1-john-harbaugh); published `2026-09-06T13:36:00Z`; retrieved `2026-09-06T19:54:26+00:00`; `obs-2026-nyg-20260906t193157z-002`.
