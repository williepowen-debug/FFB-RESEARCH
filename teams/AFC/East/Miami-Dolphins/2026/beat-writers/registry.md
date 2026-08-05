---
schema_version: 1
record_id: bw-2026-mia-registry-001
record_type: beat_writer_registry
title: "Miami Dolphins 2026 Source Registry"
team_ids: ["MIA"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-05
last_verified: 2026-08-05
confidence: high
source_ids: []
supersedes: []
writer_ids: ["local-writer-alfredo-arteaga", "local-writer-alain-poupart", "local-writer-barry-jackson", "local-writer-cameron-wolfe", "local-writer-chris-kouffman", "local-writer-chris-perkins", "local-writer-c-isaiah-smalls-ii", "local-writer-david-furones", "local-writer-hal-habib", "local-writer-joe-schad", "local-writer-kyle-crabbs", "local-writer-marcel-louis-jacques", "local-writer-omar-kelly", "local-writer-simon-clancy", "local-writer-travis-wingfield"]
---

# Miami Dolphins 2026 Source Registry

This registry prioritizes sources that can establish or explain changes in player availability, role, usage, coaching, scheme, and roster construction. Priority describes monitoring frequency; source class describes function. See [sources.csv](sources.csv) for normalized records, [endpoints.csv](endpoints.csv) for links, and the [monitoring guide](README.md) for the operating workflow.

## Essential monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Miami Dolphins communications | Miami Dolphins | official | Injury reports, transactions, transcripts, press conferences, practice notebooks | Source of record for team announcements; notebooks and team-produced analysis are not independent |
| NFL gamebooks and participation records | NFL | official | Game participation, starters, statistics, play-by-play, officials, scoring | Preferred postgame source of record; retrieve the game-specific book |
| Barry Jackson | Miami Herald | reporting | Sourced team reporting, roster and organizational context | Separate sourced reporting from analysis |
| Marcel Louis-Jacques | ESPN NFL Nation | reporting | National-platform beat reporting, availability, transactions, team context | ESPN identifies him as its Miami Dolphins NFL Nation reporter |
| David Furones | South Florida Sun Sentinel | reporting | Daily beat coverage, practice observations, injuries, roster movement | Favor concrete observations over camp evaluations |
| Joe Schad | Palm Beach Post | reporting | Beat reporting, practice and player usage, roster and coaching context | Cross-check material role claims with official records or another observer |
| Omar Kelly | Miami Herald | reporting | Firsthand observations, sourced reporting, and commentary | Hybrid beat reporter/columnist; classify each claim as reporting or interpretation |
| C. Isaiah Smalls II | Miami Herald | reporting | Dolphins coverage, features, and team context | Active Dolphins coverage; do not omit from the Herald beat map |
| Hal Habib | Palm Beach Post | reporting | Veteran local reporting and organizational context | Publication cadence may be less daily than the primary beat rotation |
| Alain Poupart | Miami Dolphins On SI | reporting | Credentialed practice-by-practice observations, roster reporting, historical context | Treat as primary reporting when based on direct attendance; separate mailbag opinion |
| Kyle Crabbs | Locked On Dolphins / A to Z Sports | film_analysis | Film, roster construction, draft, scheme, and role interpretation | Analysis source, not an official record or substitute for credentialed reporting |
| 3 Yards Per Carry | Five Reasons Sports Network | film_analysis | Detailed Dolphins discussion, camp reports, film and scheme interpretation | Collective analysis; attribute the individual host when possible |
| Travis Wingfield | Miami Dolphins | team_analysis | Practice recaps, film study, interviews, and scheme explanation | Team employee; valuable detail but not organizationally independent |

## Valuable monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Chris Perkins | South Florida Sun Sentinel | commentary | Dolphins column, team context, and practice interpretation | Commentary-first; pair conclusions with Furones or another reporting source |
| Cameron Wolfe | NFL Network | reporting | National reporting, league context, and selected on-site Dolphins updates | Not a daily beat feed; high value when actively reporting a Dolphins item |
| Pro Football Focus | PFF | data | Charting, grades, alignments, routes and pressure context | Proprietary methodology; grades are evaluations, not facts |
| Pro Football Reference | Sports Reference | data | Convenient game logs, snap counts, rosters, and historical comparisons | Snap counts are identified as unofficial; verify consequential discrepancies |
| Over the Cap | Over the Cap | contract_data | Contract structure, cap charges, dead money, and roster-management context | Third-party interpretation of contract data; cross-check unusual figures |
| Spotrac | Spotrac | contract_data | Contract, transaction, and roster reference | Useful cross-check; not an official transaction or contract filing |
| The Phinsider | SB Nation | aggregation | Fast aggregation, community context, and links to original reports | Cite the original source for consequential claims |
| RotoWire | RotoWire | aggregation | Rapid injury, roster, and fantasy-role summaries | Follow attribution back to the reporter or official source |
| Fantasy Life | Fantasy Life | fantasy_analysis | Fantasy-specific usage and projection context | Downstream interpretation; establish team facts elsewhere first |

## Supplemental monitoring

Local radio, national fantasy programs, and social-media aggregators can surface leads. Add them to a research record only when the item is attributable, reproducible, and relevant. Do not promote an account solely because it posts frequently or quickly.

## Reliability history

### Baseline status

This is the initial 2026 registry. It does not assign blanket reliability grades because no repo-local outcome history has yet been recorded. “Essential” means the source fills an important monitoring function, not that every claim should be accepted without verification.

- Strongest coverage areas: recorded per source in `sources.csv`.
- Known limitations: recorded in each source's `handling_note`.
- Confirmed early reports: none logged in this registry yet.
- Corrections or misses: none logged in this registry yet.
- Current reliability assessment: pending documented outcomes.
- Evidence for assessment: add dated examples and downstream record IDs before changing an assessment.

### Role-drift controls

Role changes are retained as status data. Omar Kelly's move from Sun Sentinel columnist to a Miami Herald hybrid beat-reporter/columnist role is recorded without treating his prior affiliation as current. Chris Perkins is recorded as the Sun Sentinel Dolphins columnist. Future departures should set `status` to `inactive` and populate `ended_on`, `current_role`, and `replacement_if_known` rather than deleting history.

## Usage notes

Start with official records and direct observations. Use reporting to establish what changed, analysis to explain why it matters, and measured usage to test whether the interpretation held up. Attribute individual reports, distinguish reporting from interpretation, and update reliability judgments from documented outcomes rather than reputation alone.

For a material fantasy conclusion, prefer one official or measured source plus one independent reporting source. If only one source supports a consequential claim, label the conclusion provisional and state the next verification step.
