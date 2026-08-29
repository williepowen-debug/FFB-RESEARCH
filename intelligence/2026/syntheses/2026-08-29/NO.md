---
schema_version: 1
record_id: ti-2026-no-20260829-001
record_type: team_intelligence
title: "New Orleans Saints intelligence synthesis — 2026-08-29"
team_ids: ["NO"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-26
last_verified: 2026-08-29
confidence: high
source_ids: ["local-source-new-orleans-saints"]
supersedes: ["ti-2026-no-20260822-001"]
observation_ids: ["obs-2026-no-20260829t143349z-001", "obs-2026-no-20260829t143349z-002"]
run_ids: ["20260829T143349Z"]
---

# New Orleans Saints intelligence synthesis — 2026-08-29

## Executive signal

New Orleans rested most starters after 145 joint-practice snaps, so the final preseason game did
not resolve its receiver, offensive-line, or healthy-backfield triggers. Zamir White's arrival adds
another backfield variable, but there is no role, snap, route, or high-leverage usage evidence yet.

## Reconciled evidence

Two official team pages form separate clusters. Kellen Moore's rest decision
(`obs-2026-no-20260829t143349z-001`) establishes why representative first-unit finale evidence is
absent. A second recap documents White joining the running-back room
(`obs-2026-no-20260829t143349z-002`); it confirms presence with the team but not a role. Neither
claim has independent confirmation in this batch.

## Hypothesis impact

- `no-2026-off-q03`: **not addressed.** No final-preseason first-team receiver personnel, routes,
  or targets were observed.
- `no-2026-off-q04` and `no-2026-off-q05`: **review the expanded competition, no conclusion
  change.** White adds a possible workload claimant, but the evidence supplies no placement
  relative to Travis Etienne, Alvin Kamara, Kendre Miller, or other backs.
- `no-2026-off-q07`: **not addressed.** No official Cesar Ruiz status or first-team right-guard
  rotation was found.

## Open-ledger trigger assessment

- `til-2026-no-20260821-001`: **Trigger not occurred.** Starter rest prevented the named Bryce
  Lance personnel, route, and target test.
- `til-2026-no-20260821-002`: **Trigger not occurred.** No Ruiz status or first-team right-guard
  rotation appeared.
- `til-2026-no-20260821-003`: **Trigger not occurred.** No healthy first-team snaps, routes,
  two-minute work, or goal-line usage appeared; White's arrival expands but does not resolve it.

ARCH should leave all three rows `deferred` / `open`.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Resting most starters prevented the final-preseason role checkpoints from occurring. | `obs-2026-no-20260829t143349z-001` | Carry the receiver, line, and backfield triggers into Week 1. |
| review | Zamir White joined an already unsettled Saints backfield. | `obs-2026-no-20260829t143349z-002` | Verify final roster status and chart first-team early-down, route, two-minute, and goal-line usage before changing `no-2026-off-q04` or `no-2026-off-q05`. |

## Conflicts and uncertainty

There is no contradiction. White's acquisition originated before this window, and the in-window
evidence establishes only his arrival. The full backfield hierarchy and all three prior ledger
questions remain unresolved.

## Excluded noise

Positive teammate comments about White's personality and adaptability were excluded because they
do not establish role or performance.

## Run metrics

- Raw observations: 2
- Unique evidence clusters: 2
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing: 1 log, 1 review, 0 escalate
- Promotions: 0
- Synthesis elapsed time: approximately 6 minutes

## Sources

- John DeShazier, New Orleans Saints — [Saints starters will sit out preseason finale against Dallas](https://www.neworleanssaints.com/news/new-orleans-saints-starters-will-sit-out-preseason-finale-against-dallas-2026) — published 2026-08-26T22:41:00-05:00; retrieved 2026-08-29T14:38:07Z; observation `obs-2026-no-20260829t143349z-001`.
- New Orleans Saints — [Key takeaways from Training Camp media availability at Tulane](https://www.neworleanssaints.com/news/key-takeaways-from-saints-training-camp-media-availability-tulane-university-2026) — published 2026-08-26T22:12:00-05:00; retrieved 2026-08-29T14:38:07Z; observation `obs-2026-no-20260829t143349z-002`.
