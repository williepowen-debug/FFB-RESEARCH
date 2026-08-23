---
schema_version: 1
record_id: ti-2026-lar-20260822-001
record_type: team_intelligence
title: "Los Angeles Rams intelligence synthesis — 2026-08-22"
team_ids: ["LAR"]
player_ids: []
season: 2026
week: null
status: draft
time_horizon: seasonal
valid_as_of: 2026-08-22
last_verified: 2026-08-22
confidence: medium
source_ids: ["local-source-nfl-gamebooks"]
supersedes: []
observation_ids: ["obs-2026-lar-20260822t232931z-001", "obs-2026-lar-20260822t232931z-002", "obs-2026-lar-20260822t232931z-003", "obs-2026-lar-20260822t232931z-004"]
run_ids: ["20260822T232931Z"]
---

# Los Angeles Rams intelligence synthesis — 2026-08-22

## Executive signal

Stetson Bennett scored twice as a runner and Jarquez Hunter recorded a short reception and a
12-yard rushing touchdown, but all four observations are isolated backup or depth plays without
snap, route, personnel, or first-team context. They do not challenge Matthew Stafford's status,
resolve the Williams-Corum split, or test the Rams' first-team tight-end and defensive hypotheses.
No signal reaches `review` or `escalate`.

## Reconciled evidence

- **Bennett rushing scores (two distinct scoring plays):** Bennett scored on a pylon dive
  (`obs-2026-lar-20260822t232931z-001`) and on a separate eight-yard run
  (`obs-2026-lar-20260822t232931z-002`). The official highlights establish the plays but do not
  suggest first-team work or competition with Stafford.
- **Hunter reserve production (two distinct plays):** Hunter converted a five-yard reception into
  a first down (`obs-2026-lar-20260822t232931z-003`) and later scored on a 12-yard run
  (`obs-2026-lar-20260822t232931z-004`). No snap share, routes, quarterback unit, down-distance
  portfolio, or comparison with Kyren Williams and Blake Corum was available.

## Hypothesis impact

- `lar-off-qb-001`: **no change.** Bennett's rushing production came without evidence of first-team
  work and does not challenge Stafford's uncontested QB1 status.
- `lar-off-rb-001`: **no change.** Hunter's reserve production does not test the stated Williams
  versus Corum first-team carry, route, drive, or red-zone conditions.
- `lar-off-te-001` and `lar-off-wr3-001`: **not addressed.** No first-team personnel-grouping or
  route-participation evidence was available.
- `lar-def-rush-001`, `lar-def-cb-001`, `lar-def-idp-001`, and `lar-def-script-001`: **not
  addressed.** The batch does not provide first-team defensive participation, alignment, or
  pressure-rate evidence.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Bennett scored two rushing touchdowns in backup preseason work. | `obs-2026-lar-20260822t232931z-001`; `obs-2026-lar-20260822t232931z-002` | Preserve as quarterback-depth evidence; do not revisit `lar-off-qb-001` without first-team reps or a Stafford availability change. |
| log | Hunter produced one short reception and one 12-yard rushing touchdown without role-defining context. | `obs-2026-lar-20260822t232931z-003`; `obs-2026-lar-20260822t232931z-004` | Obtain complete snaps, routes, and unit context; keep the Williams-Corum hypothesis unchanged. |

## Conflicts and uncertainty

No source conflict exists. The official game center supplied timestamped highlights but no
downloadable gamebook, participation report, snap counts, routes, or first-team personnel data.
The 34-0 score and depth production cannot be projected onto the Rams' regular-season starters.

## Excluded noise

None. All four observations are retained as low-impact depth logs.

## Run metrics

- Raw observations: 4
- Unique evidence clusters: 4
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing counts: 2 log, 0 review, 0 escalate
- False positives excluded: 0
- Affected hypotheses: 2 explicitly checked with no change; 6 checked but not addressed
- Promotions: 0
- Synthesis elapsed time: 6 minutes

## Sources

- NFL game center, [Saints at Rams — 2026 preseason Week 2](https://www.nfl.com/games/saints-at-rams-2026-pre-2), individual highlights published between 2026-08-22T21:06:13.910Z and 2026-08-22T23:15:31.768Z, retrieved 2026-08-22T23:54:28Z — `obs-2026-lar-20260822t232931z-001` through `obs-2026-lar-20260822t232931z-004`.
