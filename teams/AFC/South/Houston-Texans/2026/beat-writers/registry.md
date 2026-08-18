---
schema_version: 1
record_id: bw-2026-hou-registry-001
record_type: beat_writer_registry
title: "Houston Texans 2026 Source Registry"
team_ids: ["HOU"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-18
last_verified: 2026-08-18
confidence: high
source_ids: []
supersedes: []
writer_ids: ["local-writer-dj-bien-aime", "local-writer-jonathan-m-alexander", "local-writer-aaron-wilson", "local-writer-john-harris", "local-writer-deepi-sidhu", "local-writer-marc-vandermeer", "local-writer-drew-dougherty"]
---

# Houston Texans 2026 Source Registry

This registry prioritizes sources that can establish or explain changes in availability, role, usage, scheme, and roster construction. Priority describes monitoring frequency; source class describes function. See [sources.csv](sources.csv), [endpoints.csv](endpoints.csv), and the [monitoring guide](README.md).

## Essential Monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Houston Texans communications | Houston Texans | official | Transactions, roster, unofficial depth chart, injury reports, press releases, and practice notes | Source of record for team announcements; editorial analysis is not independent |
| NFL gamebooks and participation records | NFL | official | Game participation, starters, statistics, play-by-play, and scoring | Preferred postgame source of record |
| DJ Bien-Aime | ESPN NFL Nation | reporting | Beat reporting, injuries, roster movement, and team context | ESPN identifies Bien-Aime as its Houston Texans NFL Nation reporter |
| Jonathan M. Alexander | Houston Chronicle | reporting | Daily beat, roster projection, injuries, practice, and features | Distinguish reported facts from newsletter or projection analysis |
| Aaron Wilson | KPRC 2 | reporting | Transactions, injuries, sourced roster reporting, and practice context | High-volume reporter; preserve original attribution |
| John Harris | Houston Texans | team_analysis | Practice observations, Harris Hits, scheme, and player usage | Team employee; valuable access but not independent confirmation |

## Valuable Monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Deepi Sidhu | Houston Texans | team_analysis | Team features, interviews, and official context | Team employee; use for access and official context |
| Marc Vandermeer | Houston Texans | team_analysis | Texans All Access, interviews, and team context | Team employee and broadcaster |
| Drew Dougherty | Houston Texans | team_analysis | Fan Q&A, official context, and interviews | Team employee; useful for explanations |
| Battle Red Blog | SB Nation | aggregation | Community analysis, roster discussion, and links | Follow consequential claims to original reporting |
| Ourlads | Ourlads | data | Unofficial depth charts and roster ordering | Cross-check only; not usage evidence |
| Pro Football Reference | Sports Reference | data | Game logs, snap counts, rosters, and historical comparisons | Snap counts are unofficial |
| Pro Football Focus | PFF | data | Proprietary charting, alignments, routes, pressures, and grades | Grades are evaluations; do not commit paid exports |
| Over the Cap | Over the Cap | contract_data | Contract structure and cap context | Third-party interpretation |
| Spotrac | Spotrac | contract_data | Contract, transaction, and roster reference | Cross-check; not an official transaction filing |
| RotoWire | RotoWire | aggregation | Injuries, transactions, and fantasy news | Retrieve and cite the underlying report |
| Fantasy Life | Fantasy Life | fantasy_analysis | Usage framing and fantasy implications | Establish team facts with reporting or official records first |

## Supplemental Monitoring

Local radio, podcasts, national fantasy programs, and social feeds can surface leads. Promote a claim into research only when it is attributable, reproducible, and supported by a source appropriate to the claim.

## Reliability history

### Baseline Status

This is the initial Houston registry. It does not assign blanket reliability grades. "Essential" means the source fills an important monitoring function, not that every statement should be accepted without verification.

- Strongest coverage areas: recorded per source in [sources.csv](sources.csv).
- Known limitations: recorded in each source's `handling_note`.
- Confirmed early reports: none scored in the registry yet.
- Corrections or misses: none scored in the registry yet.
- Current reliability assessment: pending documented outcomes.
- Evidence for assessment: add dated examples and downstream record IDs before changing an assessment.

### Role-Drift Controls

Update source rows when beat assignments change. Do not delete historical rows; mark inactive and record replacement when verified.

## Usage notes

Start with official records and measured usage. Use reporting to establish what changed, team analysis to understand context, and fantasy/data sources to test implications. For a material fantasy conclusion, prefer one official or measured source plus one independent reporting source. If only one source supports a consequential claim, label it provisional and state the next test.
