---
schema_version: 1
record_id: ti-2026-ten-20260829-001
record_type: team_intelligence
title: "Tennessee Titans intelligence synthesis — 2026-08-29"
team_ids: ["TEN"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-29
last_verified: 2026-08-29
confidence: medium
source_ids: ["local-source-tennessee-titans"]
supersedes: ["ti-2026-ten-20260824-001"]
observation_ids: ["obs-2026-ten-20260829t143349z-001", "obs-2026-ten-20260829t143349z-002", "obs-2026-ten-20260829t143349z-003"]
run_ids: ["20260829T143349Z"]
---

# Tennessee Titans intelligence synthesis — 2026-08-29

## Executive signal

Across 15 practices open to the media, Wan'Dale Robinson led Tennessee with 53 charted receptions,
Tyjae Spears had 40, and Calvin Ridley had 14. The large directional gap supports Robinson's
offseason momentum and Spears' receiving path while challenging any assumption that Ridley was
the dominant camp target, but the data omit routes, targets, team level, and absences.

## Reconciled evidence

All three observations come from one team-employed reporter's self-described unofficial charting
of 7-on-7 and team periods. They are separate player totals from one evidence origin, not three
independent confirmations. No contradiction was assigned.

## Hypothesis impact

The evidence supports the Robinson and Spears opportunity cases in
`rf-2026-ten-backfield-receiver-allocation-001` and challenges the possibility that Ridley entered
the season as an unquestioned target leader. Because practice attendance, route denominators,
first-team splits, and target opportunities are missing, it does not establish a fantasy ranking.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Open-practice catch totals favor Robinson and Spears and show a much lower Ridley total. | `obs-2026-ten-20260829t143349z-001`; `obs-2026-ten-20260829t143349z-002`; `obs-2026-ten-20260829t143349z-003` | Reconcile attendance and first-team context, then chart Week 1 routes, targets, first reads, and backfield passing-down snaps before changing projections. |

## Conflicts and uncertainty

The source warned that the counts were unofficial. The totals do not disclose routes run, targets,
drops, absences, quarterback distribution, or first-team versus reserve work, so raw reception
rank cannot be treated as target share.

## Excluded noise

The source's quarterback completion totals and defensive interception list were outside the three
assigned observations and were not routed.

## Run metrics

- Raw observations: 3
- Unique evidence clusters: 3 player totals from 1 originating chart
- Repeats removed: 0
- Routing: 0 log, 1 review, 0 escalate
- Promotions: 0
- Synthesis elapsed time: 5 minutes

## Sources

- Tennessee Titans / Jim Wyatt, [Training Camp Numbers](https://www.tennesseetitans.com/news/training-camp-numbers-titans-statistical-leaders-qbs-receptions-ints-in-the-15-practices-open-to-the-media-in-2026), published 2026-08-28 at 10:32 AM CT and retrieved 2026-08-29 at 14:38 UTC; `obs-2026-ten-20260829t143349z-001` through `-003`.
