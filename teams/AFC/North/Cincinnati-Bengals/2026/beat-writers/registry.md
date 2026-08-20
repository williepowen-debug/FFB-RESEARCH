---
schema_version: 1
record_id: bw-2026-cin-registry-001
record_type: beat_writer_registry
title: "Cincinnati Bengals 2026 Source Registry"
team_ids: ["CIN"]
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
writer_ids: ["local-writer-ben-baby", "local-writer-kelsey-conway", "local-writer-paul-dehner-jr"]
---

# Cincinnati Bengals 2026 Source Registry

See [sources.csv](sources.csv), [endpoints.csv](endpoints.csv), and [README.md](README.md).

## Essential monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Cincinnati Bengals communications | Bengals | official | Roster, injuries, transactions, depth chart, conferences | Team analysis is not independent |
| NFL gamebooks and participation | NFL | official | Participation and game records | Preferred postgame record |
| Ben Baby | ESPN NFL Nation | reporting | Daily beat, injuries, roster, organization | ESPN verifies assignment |
| Kelsey Conway | Cincinnati Enquirer | reporting | Practice, roster, injuries and personnel | Paywalled; summarize and attribute |
| Paul Dehner Jr. | The Athletic | reporting | Beat reporting, contracts, roster and scheme | Separate reporting from analysis |

## Valuable monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Bengals Media Room | Bengals | official | Releases, depth chart, injuries, transactions, conferences | Consolidated official endpoint |
| Pro Football Reference | Sports Reference | data | Logs and snap counts | Secondary reference |

## Reliability history

Established 2026-08-20. No repo-local outcome history has yet been scored.

### Independent beat rotation

- Strongest coverage areas: availability, practice, roster construction, contracts and roles.
- Known limitations: paywalls and mixed reporting/analysis formats.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on current roles.
- Evidence for assessment: ESPN confirms Baby's Bengals assignment; current 2026 Enquirer and
  Athletic coverage confirms Conway and Dehner.

## Usage notes

Use official reports for availability and transactions. Treat camp-role conclusions as provisional
until corroborated by an independent observer or measured preseason/regular-season usage.
