---
schema_version: 1
record_id: bw-2026-bal-registry-001
record_type: beat_writer_registry
title: "Baltimore Ravens 2026 Source Registry"
team_ids: ["BAL"]
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
writer_ids: ["local-writer-jeff-zrebiec", "local-writer-brian-wacker", "local-writer-jamison-hensley"]
---

# Baltimore Ravens 2026 Source Registry

See [sources.csv](sources.csv), [endpoints.csv](endpoints.csv), and [README.md](README.md).

## Essential monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Baltimore Ravens communications | Ravens | official | Roster, injuries, transactions, releases and transcripts | Team analysis is not independent |
| NFL gamebooks and participation | NFL | official | Participation and game records | Preferred postgame record |
| Jeff Zrebiec | The Athletic | reporting | Daily beat, roster, contracts, organization and practice | Paywalled; summarize and attribute |
| Brian Wacker | Baltimore Sun | reporting | Lead local beat, practice, roster and organization | Paywalled; distinguish analysis |
| Jamison Hensley | ESPN | reporting | Beat reporting, injuries, roster and team context | Current 2026 press access independently verified |

## Valuable monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Ravens Press Room | Ravens | official | Media guide, releases, game materials and transcripts | Consolidated official endpoint |
| Pro Football Reference | Sports Reference | data | Logs and snap counts | Secondary reference |

## Reliability history

Established 2026-08-20. No repo-local outcome history has yet been scored.

### Independent beat rotation

- Strongest coverage areas: practice, injuries, roster, contracts, coaching and organization.
- Known limitations: paywalls and mixed reporting/analysis notebooks.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on current roles and access.
- Evidence for assessment: 2026 official Ravens press-conference transcripts identify Zrebiec,
  Wacker, and Hensley as active participants; current outlet coverage confirms assignments.

## Usage notes

Use the official press room for source-of-record documents. Cross-check consequential role or
availability claims with independent reporting and later measured participation.
