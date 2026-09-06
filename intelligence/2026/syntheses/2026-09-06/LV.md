---
schema_version: 1
record_id: "ti-2026-lv-20260906-001"
record_type: "team_intelligence"
title: "Las Vegas Raiders intelligence synthesis — 2026-09-06"
team_ids: ["LV"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-06"
last_verified: "2026-09-06"
confidence: "medium"
source_ids: ["local-source-las-vegas-raiders"]
supersedes: []
observation_ids: ["obs-2026-lv-20260906t193157z-001", "obs-2026-lv-20260906t193157z-002"]
run_ids: ["20260906T193157Z"]
---

# Las Vegas Raiders intelligence synthesis — 2026-09-06

## Executive signal

Cousins is the announced Week 1 starter; Jeanty availability remains unsettled.

## Reconciled evidence

- `obs-2026-lv-20260906t193157z-001`: Klint Kubiak named Kirk Cousins the Raiders starting quarterback for Week 1.
- `obs-2026-lv-20260906t193157z-002`: Ashton Jeanty had not practiced since the final preseason week; the GM briefing supplied no return date.

The official outlet supplies the originating evidence. Shared briefings are not independent corroboration. Statements about planned practice remain plans; the dated snapshots do not establish later game clearance.

## Hypothesis impact

lv-off-qb-001 is confirmed for the opener; lv-off-rb-001 retains its availability checkpoint.

Baseline read: `teams/AFC/West/Las-Vegas-Raiders/2026/offense/hypotheses.csv` and prior synthesis `ti-2026-lv-20260825-001`.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| escalate | Cousins is the announced Week 1 starter; Jeanty availability remains unsettled. | `obs-2026-lv-20260906t193157z-001`; `obs-2026-lv-20260906t193157z-002` | Promote bounded current state to `wm-2026-w01-mia-lv-001`; Jeanty official report; Cousins early-game performance and Bowers routes. |

Start quarterback preparation from Cousins; keep a backfield contingency without assigning Washington a verified lead workload.

Canonical promotion: `lv-off-qb-001` at `teams/AFC/West/Las-Vegas-Raiders/2026/offense/hypotheses.csv`. Confirmed the opening starter from Kubiak's announcement.

Canonical promotion: `rf-2026-lv-quarterback-transition-001` at `teams/AFC/West/Las-Vegas-Raiders/2026/offense/quarterback-transition.md`. Updated camp projection to the announced opening starter.

## Conflicts and uncertainty

Jeanty official report; Cousins early-game performance and Bowers routes. No independent beat confirmation is claimed. See source-level access limits in the reader report.

## Excluded noise

Out-of-window search results, profile biographies, generic praise and promotional material do not establish current roles. No extra role conclusion is drawn from roster inclusion.

## Run metrics

- Raw observations: 2
- Unique originating articles: 2
- Repeats removed: 0
- Independent confirmations: 0
- Synthesis elapsed time: not separately instrumented.
- Reader coverage: [`run-report.csv`](../../runs/20260906T193157Z/reader-lv/run-report.csv).

## Sources

- [local-source-las-vegas-raiders](https://www.raiders.com/news/kirk-cousins-named-raiders-starting-quarterback) — published 2026-09-02T16:30:53.406Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-lv-20260906t193157z-001`.
- [local-source-las-vegas-raiders](https://www.raiders.com/news/4-takeaways-john-spytek-and-brian-stark-raiders-53-man-roster) — published 2026-09-02T00:14:04.705Z; retrieved 2026-09-06T19:52:07+00:00; `obs-2026-lv-20260906t193157z-002`.
