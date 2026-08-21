---
schema_version: 1
record_id: bw-2026-phi-registry-001
record_type: beat_writer_registry
title: "Philadelphia Eagles 2026 Source Registry"
team_ids: ["PHI"]
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
writer_ids: ["local-writer-tim-mcmanus", "local-writer-olivia-reiner", "local-writer-jeff-neiburg", "local-writer-dave-zangaro", "local-writer-reuben-frank", "local-writer-eliot-shorr-parks", "local-writer-brandon-lee-gowton", "local-writer-john-mcmullen", "local-writer-zach-berman"]
---

# Philadelphia Eagles 2026 Source Registry

See [sources.csv](sources.csv), [endpoints.csv](endpoints.csv), [candidates.csv](candidates.csv), and the
[monitoring guide](README.md).

## Essential monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Philadelphia Eagles communications | Eagles | official | Roster, injuries, transactions, gamebooks, transcripts | Team analysis is not independent |
| NFL gamebooks and participation | NFL | official | Participation, starters, statistics, play-by-play | Preferred postgame record |
| Tim McManus | ESPN NFL Nation | reporting | Daily beat, injuries, roster, organization | ESPN verifies the current Eagles assignment |
| Olivia Reiner | Philadelphia Inquirer | reporting | Camp, practice, roles, roster | Paywalled; summarize and attribute |
| Jeff Neiburg | Philadelphia Inquirer | reporting | Practice, personnel, roster and draft | Separate observations from projections |
| Dave Zangaro | NBC Sports Philadelphia | reporting | Daily beat, practice, roster and snap analysis | Verify consequential role claims with usage |
| Reuben Frank | NBC Sports Philadelphia | reporting | Daily camp observations, history and role context | Shared outlet with Zangaro is not separate corroboration |
| Eliot Shorr-Parks | 94WIP | reporting | Credentialed camp observations and daily local radio | Opinion-forward; verify evaluations |

## Valuable monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Eagles Media Center | Eagles | official | Weekly releases, gamebooks, rosters and injury reports | Best consolidated official endpoint |
| Philadelphia Inquirer Eagles coverage | Inquirer | reporting | Multi-reporter camp and game coverage | Preserve individual byline |
| Brandon Lee Gowton | Bleeding Green Nation | team analysis | Credentialed camp notes, roster and podcast | Separate firsthand observation from reaction |
| John McMullen | Sports Illustrated / JAKIB | reporting | Credentialed camp reporting and interviews | Verify breaking claims at primary source |
| Zach Berman | PHLY | reporting | Organization, roster and institutional context | Subscription work; lower daily cadence |
| Over the Cap | Over the Cap | contract data | Contracts and roster mechanics | Third-party interpretation |
| Pro Football Reference | Sports Reference | data | Game logs and snap counts | Secondary reference |

## Coverage audit

All eight required lanes are covered. The reopened omission pass added Frank, Shorr-Parks, Gowton,
McMullen, Berman, and Over the Cap. Shared Philadelphia outlets and podcasts must not be counted as
independent confirmations of the same originating observation.

## Reliability history

Established 2026-08-20. Priority reflects verified assignment and access, not an earned blanket
grade. No confirmed-report or correction history has yet been scored.

### Independent beat rotation

- Strongest coverage areas: practice observation, injuries, personnel order, roster decisions.
- Known limitations: live blogs and podcasts can be updated or difficult to cite precisely.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on current roles.
- Evidence for assessment: ESPN identifies McManus as Eagles NFL Nation reporter; the Inquirer
  identifies Reiner as covering all aspects of the Eagles; current 2026 coverage confirms the
  remaining assignments.

## Usage notes

Use official records to establish status, independent reporting to explain changes, and measured
usage to test preseason conclusions. Attribute individual reporters and time-stamp live coverage.
