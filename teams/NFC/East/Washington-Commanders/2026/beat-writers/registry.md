---
schema_version: 1
record_id: bw-2026-was-registry-001
record_type: beat_writer_registry
title: "Washington Commanders 2026 Source Registry"
team_ids: ["WAS"]
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
writer_ids: ["local-writer-john-keim", "local-writer-tashan-reed", "local-writer-nicki-jhabvala", "local-writer-jp-finlay", "local-writer-ben-standig", "local-writer-mark-bullock", "local-writer-logan-paulsen", "local-writer-zach-selby"]
---

# Washington Commanders 2026 Source Registry

Candidate discovery and omission-pass decisions are recorded in [candidates.csv](candidates.csv).

See [sources.csv](sources.csv), [endpoints.csv](endpoints.csv), and [README.md](README.md).

## Essential monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| Commanders communications | Commanders | official | Status, transactions, conferences and camp notebooks | Team analysis is not independent |
| NFL gamebooks and participation | NFL | official | Participation and game records | Preferred postgame record |
| John Keim | ESPN NFL Nation | reporting | Daily beat, injuries, organization and podcast | ESPN verifies assignment |
| Tashan Reed | The Washington Post | reporting | Camp observations, roster, scheme and organization | Current August 2026 bylines verify assignment |
| Nicki Jhabvala | The Athletic | reporting | Practice, roster, organization and roles | Current 2026 camp work; paywalled |
| Ben Standig | Last Man Standig | reporting | Daily camp, roster, transactions and organization | Independent subscription work |

## Valuable monitoring

| Source | Outlet | Class | Primary value | Handling note |
|---|---|---|---|---|
| JP Finlay | NBC4 / 106.7 The Fan | reporting | Breaking news, camp, interviews and radio context | Separate reporting from opinion |
| Mark Bullock | Independent | film analysis | All-22, scheme, quarterback and line play | Evaluation source |
| Logan Paulsen | Commanders / Last Man Standig | film analysis | Scheme, personnel roles and line/TE play | Team role is not independent |
| Zach Selby | Washington Commanders | team analysis | Camp notebooks, interviews and roster context | Team employee |
| Over the Cap | Over the Cap | contract data | Contracts and roster mechanics | Third-party reference |
| Pro Football Reference | Sports Reference | data | Logs and snap counts | Secondary reference |

## Coverage audit

| Lane | Included coverage |
|---|---|
| Official record | Commanders communications; NFL gamebooks |
| Daily independent beat | Keim; Reed; Jhabvala |
| National or major local reporting | ESPN; Washington Post; The Athletic |
| Local television and radio | Finlay |
| Film and scheme analysis | Bullock; Paulsen; Reed |
| Position usage and fantasy signal | Jhabvala; Keim; Standig; Bullock; Paulsen |
| Transactions and organization | Reed; Keim; Over the Cap |
| Team-controlled analysis | Selby; Command Center |

The reopened omission pass added Standig, whose independent daily camp reporting remained essential
after leaving The Athletic, and Paulsen, whose scheme work fills a distinct analyst lane. Aggregation-
only shows remain excluded. The Post's 2026 beat transition is reflected by using Reed rather than
departed reporters.

## Reliability history

Established 2026-08-21. No repo-local outcomes have yet been scored. Priority reflects verified
assignment, access, and differentiated value.

## Usage notes

Use official records for status, independent reporting to explain changes, and film or measured
usage to test conclusions. Time-stamp camp observations and label projections.
