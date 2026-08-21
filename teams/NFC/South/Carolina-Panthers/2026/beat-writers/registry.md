---
schema_version: 1
record_id: bw-2026-car-registry-001
record_type: beat_writer_registry
title: "Carolina Panthers 2026 Source Registry"
team_ids: ["CAR"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-21
last_verified: 2026-08-21
confidence: high
source_ids: []
supersedes: []
writer_ids: ["local-writer-mike-kaye", "local-writer-joe-person", "local-writer-alex-zietlow", "local-writer-scott-fowler", "local-writer-sheena-quick", "local-writer-vashti-hurt", "local-writer-darin-gantt", "local-writer-kassidy-hill", "local-writer-john-ellis", "local-writer-julian-council"]
---

# Carolina Panthers 2026 Source Registry

This registry covers every defined fantasy-relevant information lane. See [sources.csv](sources.csv), [endpoints.csv](endpoints.csv), the [candidate audit](candidates.csv), and the [monitoring guide](README.md).

The central 2026 role change is Mike Kaye's August move from the Charlotte Observer to ESPN's Panthers beat. Alex Zietlow remains the Observer's primary beat voice, with columnist Scott Fowler adding enterprise and organizational context. David Newton is retained only in the audit as the former ESPN reporter.

## Essential monitoring

| Source | Function | Primary value | Handling note |
|---|---|---|---|
| Carolina Panthers communications | Official | Injuries, transactions, roster, press conferences | Source of record; team analysis is not independent |
| Mike Kaye (ESPN) | Reporting | Daily beat, camp observations, personnel usage | New ESPN assignment in August 2026; do not use older Observer affiliation |
| Joe Person (The Athletic) | Reporting | Sourced beat reporting and organizational context | Paywall; separate reporting from analysis |
| Alex Zietlow (Charlotte Observer) | Reporting | Daily camp and locker-room reporting | Paywall; primary current Observer beat voice |
| Sheena Quick | Reporting | Credentialed observations, interviews, player context | Independent multimedia work; verify outlet on each item |
| Vashti Hurt (Carolina Blitz) | Reporting | Credentialed pressers, interviews, independent local coverage | Multi-sport outlet; use the Panthers-specific original item |
| Darin Gantt and Kassidy Hill | Official | Daily team notebooks, transactions, interviews | Team-employed; pair consequential claims with independent reporting |

## Valuable monitoring

| Source | Function | Primary value | Handling note |
|---|---|---|---|
| Scott Fowler | Commentary/reporting | Enterprise, ownership, coaching, major role stories | Columnist; distinguish reported facts from opinion |
| John Ellis | Film analysis | Scheme, quarterback and position-role interpretation | Analysis must be tied to observable film |
| Julian Council | Team analysis | Daily roster, role, and listener-question synthesis | High cadence; distinguish original analysis from summarized reporting |
| NFL gamebooks | Official record | Participation and game records | Use specific gamebook or transaction |
| Pro Football Reference | Data | Historical stats and snap counts | Snap counts are unofficial reference data |
| Over the Cap | Contract data | Cap and contract mechanics | Cross-check unusual figures |

## Reliability history

This is the initial 2026 registry. Priority indicates monitoring value, not a blanket accuracy grade. No repo-local confirmed-hit or correction history exists yet. Add dated outcomes before changing reliability assessments.

Role drift is explicit: Mike Kaye replaced David Newton as ESPN's Panthers reporter in August 2026. Future changes should update status and replacement fields rather than silently deleting history.

## Usage notes

For material fantasy conclusions, pair an official or measured source with independent reporting. Direct practice observations establish reps and availability; film analysis explains possible meaning; regular-season usage tests the conclusion. Treat camp praise without role evidence as provisional.
