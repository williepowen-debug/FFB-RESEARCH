---
schema_version: 1
record_id: ti-2026-no-20260822-001
record_type: team_intelligence
title: "New Orleans Saints intelligence synthesis — 2026-08-22"
team_ids: ["NO"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-22
last_verified: 2026-08-22
confidence: medium
source_ids: ["local-source-nfl-gamebooks"]
supersedes: []
observation_ids: ["obs-2026-no-20260822t232931z-001", "obs-2026-no-20260822t232931z-002", "obs-2026-no-20260822t232931z-003", "obs-2026-no-20260822t232931z-004"]
run_ids: ["20260822T232931Z"]
---

# New Orleans Saints intelligence synthesis — 2026-08-22

## Executive signal

The available in-window official evidence contains four isolated reserve-unit plays and no snap,
route, personnel-grouping, starter, or participation report. Zach Wilson threw an interception and
was sacked; Spencer Rattler produced one explosive completion before a later 100-yard pick-six.
Those plays do not change Tyler Shough's QB1 baseline or resolve any of the three open Saints ledger
triggers. No signal reaches `review` or `escalate`.

## Reconciled evidence

- **Wilson reserve performance (two distinct play clusters):** Wilson was sacked by Wesley Bailey
  (`obs-2026-no-20260822t232931z-002`) and later intercepted by Al'zillion Hamilton
  (`obs-2026-no-20260822t232931z-001`). The NFL highlights establish the plays but not Wilson's
  total snaps, supporting cast, pressure rate, or position in the quarterback order.
- **Rattler reserve performance (two distinct play clusters):** Rattler completed a 32-yard pass to
  CJ Donaldson that reached the Rams' 10-yard line (`obs-2026-no-20260822t232931z-003`), then had a
  later pass intercepted and returned 100 yards by Alex Cook
  (`obs-2026-no-20260822t232931z-004`). Opposite outcomes in isolated plays are not a usable
  efficiency sample and contain no first-team competition evidence.

## Hypothesis impact

- `no-2026-off-q01`: **no change.** Wilson's and Rattler's reserve-game mistakes do not show either
  receiving meaningful first-team competition with Shough. Full drive and unit context was absent.
- `no-2026-off-q03`: **not addressed.** The batch contains no final-preseason routes, targets, or
  personnel groupings for Jordyn Tyson, Bryce Lance, or the other receivers.
- `no-2026-off-q04` and `no-2026-off-q05`: **not addressed.** A reception by CJ Donaldson supplies no
  healthy-backfield evidence for Travis Etienne or Alvin Kamara.
- `no-2026-off-q07`: **not addressed.** One sack of Wilson does not identify the blockers involved,
  the first-team line, Cesar Ruiz's status, or the next right-guard rotation.
- All other active Saints offensive hypotheses are unchanged because their stated triggers were not
  observed.

## Open-ledger trigger assessment

- `til-2026-no-20260821-001`: **Trigger not occurred.** No final-preseason receiver personnel,
  route, or target data was available.
- `til-2026-no-20260821-002`: **Trigger not occurred.** No official Ruiz status or first-team
  right-guard rotation was available.
- `til-2026-no-20260821-003`: **Trigger not occurred.** No healthy Etienne/Kamara backfield snaps,
  routes, two-minute work, or goal-line usage was available.

ARCH should leave all three ledger rows `deferred`/`open`.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| log | Wilson was sacked and threw an interception in reserve preseason work without complete drive or unit context. | `obs-2026-no-20260822t232931z-001`; `obs-2026-no-20260822t232931z-002` | Preserve as bounded QB2 evidence; compare complete participation and final-preseason quarterback order before revisiting `no-2026-off-q01`. |
| log | Rattler produced a 32-yard completion and later threw a 100-yard pick-six in reserve preseason work. | `obs-2026-no-20260822t232931z-003`; `obs-2026-no-20260822t232931z-004` | Preserve the mixed performance; require complete drive context and any first-team competition before changing the QB baseline. |

## Conflicts and uncertainty

No source conflict exists. The main limitation is missing role context: the official game center
exposed timestamped highlights but no downloadable gamebook, participation report, snap counts,
route participation, or postgame role explanation inside the frozen window. Score and isolated
plays therefore cannot support conclusions about the starting offense.

## Excluded noise

None. All four observations are retained as low-impact logs, but none independently changes a
fantasy-relevant conclusion.

## Run metrics

- Raw observations: 4
- Unique evidence clusters: 4
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing counts: 2 log, 0 review, 0 escalate
- False positives excluded: 0
- Affected hypotheses: 1 explicitly checked with no change; 4 open questions checked but not addressed
- Promotions: 0
- Synthesis elapsed time: 7 minutes

## Sources

- NFL game center, [Saints at Rams — 2026 preseason Week 2](https://www.nfl.com/games/saints-at-rams-2026-pre-2), individual highlights published between 2026-08-22T20:52:15.869Z and 2026-08-22T22:35:15.108Z, retrieved 2026-08-22T23:54:28Z — `obs-2026-no-20260822t232931z-001` through `obs-2026-no-20260822t232931z-004`.
