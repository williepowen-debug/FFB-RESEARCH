---
schema_version: 1
record_id: ti-2026-sf-20260829-001
record_type: team_intelligence
title: "San Francisco 49ers intelligence synthesis — 2026-08-29"
team_ids: ["SF"]
player_ids: ["local-player-george-kittle-2017"]
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-28
last_verified: 2026-08-29
confidence: high
source_ids: ["local-source-san-francisco-49ers"]
supersedes: ["ti-2026-sf-20260825-001"]
observation_ids: ["obs-2026-sf-20260829t143349z-001", "obs-2026-sf-20260829t143349z-002", "obs-2026-sf-20260829t143349z-003"]
run_ids: ["20260829T143349Z"]
---

# San Francisco 49ers intelligence synthesis — 2026-08-29

## Executive signal

George Kittle's ramp has not yet produced a clear Week 1 readiness signal: Kyle Shanahan said
Kittle was taking a step back and included him among players requiring evaluation before travel to
Australia. That official, immediate checkpoint materially raises Week 1 uncertainty. Carver Willis
is pushing for the starting left guard job, while Shanahan indicated a three-back rotation is
unlikely without a compelling reason.

## Reconciled evidence

All three observations come from one official postgame quote compilation and represent distinct
coach statements. Willis' unresolved left-guard competition (`obs-2026-sf-20260829t143349z-001`),
Kittle's readiness checkpoint (`obs-2026-sf-20260829t143349z-002`), and the unlikely three-back
rotation (`obs-2026-sf-20260829t143349z-003`) are separate clusters with no independent
confirmation.

## Hypothesis impact

- `sf-off-kittle-001`: **challenges readiness.** The expected progression into competitive
  first-team routes is not established, and the coach's "taking a step back" wording heightens the
  risk that Kittle enters Week 1 with an uncertain route rate or availability.
- `sf-off-ol-001`: **challenges the Robert Jones baseline.** Willis has made enough of a push that
  coaches had not decided the starting left guard after the finale.
- `sf-off-cmc-001`: **contextual support for concentration, not player allocation.** Shanahan's
  reluctance to use three backs argues against an automatic three-way rotation but does not identify
  the two likely backs or assign high-value touches.
- `sf-off-wr-001` and `sf-off-rookie-001`: **not addressed.** No Mike Evans return or De'Zhaun
  Stribling route evidence appeared.

## Open-ledger trigger assessment

- `til-2026-sf-20260821-001`: **Trigger not occurred.** No Stribling route participation, snaps by
  quarterback unit, or red-zone usage was supplied.
- The promoted Evans checkpoint remains untested: no next-practice participation appeared in this
  batch.

ARCH should leave the Stribling row `deferred` / `open` and retain Evans' next-practice follow-up.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Willis is pushing for the starting left guard job and the competition remained undecided after the finale. | `obs-2026-sf-20260829t143349z-001` | Check the opening lineup and protection assignments before updating `sf-off-ol-001`. |
| escalate | Kittle was described as taking a step back and still required a Week 1 readiness evaluation before Australia. | `obs-2026-sf-20260829t143349z-002` | Monitor every pre-travel practice and official Week 1 status; adjust rankings and lineup contingencies if competitive first-team work does not occur. |
| log | Shanahan indicated a three-running-back rotation was unlikely absent a compelling reason. | `obs-2026-sf-20260829t143349z-003` | Identify the actual two-back allocation and high-value work before changing `sf-off-cmc-001`. |

## Conflicts and uncertainty

No source conflict exists, but the phrase "taking a step back" is not an injury diagnosis or game
designation. Kittle's competitive participation, route rate, and travel/game status remain unknown.
The left-guard winner and actual two-back hierarchy are also unresolved.

## Excluded noise

Generic praise of preseason performers and unrelated postgame evaluations were excluded. The
coach's favorable comments about individual reserve backs were not used to identify the eventual
rotation.

## Run metrics

- Raw observations: 3
- Unique evidence clusters: 3
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing: 1 log, 1 review, 1 escalate
- Promotions: 0
- Synthesis elapsed time: approximately 7 minutes

## Sources

- San Francisco 49ers — [What the 49ers and Raiders Had to Say After Preseason Week 3](https://www.49ers.com/news/what-the-49ers-and-raiders-had-to-say-after-preseason-week-3) — published 2026-08-28T16:29:00-07:00; retrieved 2026-08-29T14:38:07Z; observations `obs-2026-sf-20260829t143349z-001`, `obs-2026-sf-20260829t143349z-002`, and `obs-2026-sf-20260829t143349z-003`.
