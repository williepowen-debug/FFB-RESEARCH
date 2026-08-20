---
schema_version: 1
record_id: bw-2026-det-registry-001
record_type: beat_writer_registry
title: "Detroit Lions 2026 Source Registry"
team_ids: ["DET"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-20
last_verified: 2026-08-20
confidence: high
source_ids: []
supersedes: []
writer_ids: ["local-writer-eric-woodyard", "local-writer-dave-birkett", "local-writer-colton-pouncy", "local-writer-justin-rogers", "local-writer-benjamin-raven"]
---

# Detroit Lions 2026 Source Registry

See [sources.csv](sources.csv), [endpoints.csv](endpoints.csv), and [README.md](README.md).

## Essential monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Detroit Lions communications | Lions | official | Roster, injuries, transactions, interviews | Team analysis is not independent |
| NFL gamebooks and participation | NFL | official | Participation and game records | Preferred postgame record |
| Eric Woodyard | ESPN NFL Nation | reporting | Daily beat, injuries, roster, organization | ESPN verifies assignment |
| Dave Birkett | Detroit Free Press | reporting | Practice, roster, transactions, organization | Paywalled; summarize |
| Colton Pouncy | The Athletic | reporting | Beat reporting, personnel, scheme | Paywalled; distinguish analysis |
| Justin Rogers | Detroit Football Network | reporting | Independent daily beat and practice reporting | Verify breaking items upstream |
| Benjamin Raven | MLive | reporting | Daily beat, camp, roster and player roles | Current MLive Lions beat assignment |

## Valuable monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Lions Collective | Independent collective | analysis | Cross-reporter discussion and context | Attribute speaker and date episode |
| Pro Football Reference | Sports Reference | data | Logs and snap counts | Secondary reference |

## Reliability history

Established 2026-08-20. No repo-local outcome history has yet been scored.

### Independent beat rotation

- Strongest coverage areas: camp roles, injuries, line combinations, personnel and organization.
- Known limitations: several sources are paywalled or podcast-heavy.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on verified roles.
- Evidence for assessment: ESPN confirms Woodyard; current 2026 bylines and the Lions Collective
  confirm the other listed assignments.

## Usage notes

Combine official status with two independent observers for consequential camp-role changes, then
test conclusions against regular-season snaps, routes, and touches.
