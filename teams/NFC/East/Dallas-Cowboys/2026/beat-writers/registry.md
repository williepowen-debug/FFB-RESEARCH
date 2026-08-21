---
schema_version: 1
record_id: bw-2026-dal-registry-001
record_type: beat_writer_registry
title: "Dallas Cowboys 2026 Source Registry"
team_ids: ["DAL"]
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
writer_ids: ["local-writer-todd-archer", "local-writer-nick-harris", "local-writer-calvin-watkins", "local-writer-clarence-hill", "local-writer-joseph-hoyt", "local-writer-jon-machota", "local-writer-saad-yousuf", "local-writer-jane-slater", "local-writer-patrik-walker", "local-writer-bryan-broaddus", "local-writer-david-moore", "local-writer-newy-scruggs"]
---

# Dallas Cowboys 2026 Source Registry

Candidate discovery and omission-pass decisions are recorded in [candidates.csv](candidates.csv).

See [sources.csv](sources.csv), [endpoints.csv](endpoints.csv), and [README.md](README.md).

## Essential monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Dallas Cowboys communications | Cowboys | official | Roster, injuries, transactions, conferences | Team analysis is not independent |
| NFL gamebooks and participation | NFL | official | Participation and game records | Preferred postgame record |
| Todd Archer | ESPN NFL Nation | reporting | Daily beat, injuries, roster, organization | ESPN verifies assignment |
| Nick Harris | Fort Worth Star-Telegram | reporting | Camp observations, roles, transactions, draft | Paywalled; current 2026 bylines verify assignment |
| Calvin Watkins | Dallas Morning News | reporting | Daily camp, roles and organization | Lead beat reporter; paywalled |
| Clarence Hill | DLLS Sports | reporting | Breaking news, ownership, contracts and organization | Longest-tenured active beat voice |
| Jon Machota | The Athletic | reporting | Practice, roster construction, organization | Paywalled; summarize and attribute |

## Valuable monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Saad Yousuf | The Athletic / The Ticket | reporting | Camp, scheme, roles and local context | Separate radio opinion from reporting |
| Jane Slater | NFL Network | reporting | Breaking news, organization and interviews | National rather than daily rep coverage |
| Patrik Walker | Dallas Cowboys | team analysis | Camp observations and role battles | Team employee; not independent |
| Bryan Broaddus | 105.3 The Fan / Trust the Tape | film analysis | Film, scouting and line play | Evaluation source |
| Joseph Hoyt | DLLS Sports | reporting | Daily beat, camp and role battles | Current beat assignment verified |
| David Moore | D Magazine / The Ticket | reporting | Institutional context and long-form reporting | Lower cadence than daily beat |
| Newy Scruggs | NBC 5 DFW | reporting | Original interviews and local television | Separate guest reports from host analysis |
| Over the Cap | Over the Cap | contract data | Contracts and roster mechanics | Third-party reference |
| Pro Football Reference | Sports Reference | data | Logs and snap counts | Secondary reference |

## Coverage audit

| Lane | Included coverage |
|---|---|
| Official record | Cowboys communications; NFL gamebooks |
| Daily independent beat | Archer; Harris; Watkins; Hill; Hoyt; Machota |
| National or major local reporting | Slater; Dallas Morning News; Star-Telegram; ESPN |
| Local television and radio | Scruggs; Yousuf; Broaddus; Moore |
| Film and scheme analysis | Broaddus; Yousuf |
| Position usage and fantasy signal | Harris; Machota; Walker |
| Transactions and organization | Archer; Slater; Over the Cap |
| Team-controlled analysis | Walker; Cowboys podcasts |

The initial omission pass was reopened after comparison against current camp bylines and local
broadcasts. It added Watkins, Hill, Hoyt, Moore, and Scruggs, all of whom provide differentiated
reporting or access that the first draft missed. Aggregation-only fan channels and personalities
without verifiable original work remain excluded.

## Reliability history

Established 2026-08-21. No repo-local outcomes have yet been scored. Priority reflects verified
assignment and differentiated access, not a blanket accuracy grade.

## Usage notes

Use official records for status, independent beats for changes, and film or measured usage to test
role conclusions. Corroborate consequential organization claims and label projections.
