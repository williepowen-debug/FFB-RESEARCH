---
schema_version: 1
record_id: ti-2026-lv-20260825-001
record_type: team_intelligence
title: "Las Vegas Raiders intelligence synthesis — 2026-08-25"
team_ids: ["LV"]
player_ids: ["local-player-ashton-jeanty-2025"]
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-25
last_verified: 2026-08-25
confidence: high
source_ids: ["local-source-las-vegas-raiders"]
supersedes: ["ti-2026-lv-20260824-001"]
observation_ids: ["obs-2026-lv-20260826t011902z-001"]
run_ids: ["20260826T011902Z"]
---

# Las Vegas Raiders intelligence synthesis — 2026-08-25

## Executive signal

Klint Kubiak described Ashton Jeanty as “on the mend” after his August 23 practice exit but gave
no diagnosis or timetable. The comment is mildly reassuring and preserves Jeanty's lead-back
hypothesis, but it does not clear the open limitation checkpoint.

## Reconciled evidence

The official team report supplies the coach's exact characterization. Unregistered downstream
reports supplied more specific ankle language, so that diagnosis was excluded.

## Hypothesis impact

- `lv-off-rb-001`: **no directional change.** Jeanty's status remains the key immediate input;
  Mike Washington Jr.'s starter-unit usage remains the role check.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Jeanty is “on the mend,” with no diagnosis or return date. | `obs-2026-lv-20260826t011902z-001` | Monitor the next official practice report and Week 1 designation. |

## Conflicts and uncertainty

The source does not establish injury type, severity, or full-practice readiness.

## Excluded noise

Unregistered-source ankle-sprain labels and recovery estimates were excluded.

## Run metrics

- Raw observations: 1
- Unique evidence clusters: 1
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- Routing: 0 log, 1 review, 0 escalate
- Promotions: 1 factual checkpoint
- Synthesis elapsed time: approximately 4 minutes

## Sources

- Las Vegas Raiders — [Klint Kubiak: Ashton Jeanty is “on the mend”](https://www.raiders.com/news/klint-kubiak-ashton-jeanty-is-on-the-mend) — published 2026-08-25T12:17:00-07:00; retrieved 2026-08-26T01:25:51Z; observation `obs-2026-lv-20260826t011902z-001`.
