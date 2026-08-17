---
schema_version: 1
record_id: bw-2026-lac-registry-001
record_type: beat_writer_registry
title: "Los Angeles Chargers 2026 Source Registry"
team_ids: ["LAC"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-16
last_verified: 2026-08-16
confidence: high
source_ids: []
supersedes: []
writer_ids: ["local-writer-kris-rhim", "local-writer-fernando-ramirez", "local-writer-joaquin-ruiz", "local-writer-eric-smith", "local-writer-omar-navarro", "local-writer-sam-farmer", "local-writer-daniel-popper"]
---

# Los Angeles Chargers 2026 Source Registry

This registry prioritizes sources that can establish or explain changes in availability, role, usage, scheme, and roster construction. Priority describes monitoring frequency; source class describes function. See [sources.csv](sources.csv), [endpoints.csv](endpoints.csv), and the [monitoring guide](README.md).

## Essential monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Los Angeles Chargers communications | Los Angeles Chargers | official | Transactions, roster, unofficial depth chart, injury reports, transcripts, and press conferences | Source of record for team announcements; editorial analysis is not independent |
| NFL gamebooks and participation records | NFL | official | Game participation, starters, statistics, play-by-play, and scoring | Preferred postgame source of record |
| Kris Rhim | ESPN NFL Nation | reporting | Daily beat reporting, availability, roster movement, and team context | ESPN identifies Rhim as its Chargers NFL Nation reporter |
| Fernando Ramirez | The Sporting Tribune | reporting | Credentialed camp observations, personnel usage, and local team reporting | Separate firsthand reporting from commentary and podcast discussion |
| Joaquin Ruiz | Los Angeles Times | reporting | Chargers reporting, practice observations, injuries, and scheme context | Use dated observations; the Times' team page also includes broader NFL coverage |
| Eric Smith | Los Angeles Chargers | team_analysis | Camp reports, interviews, position previews, and official context | Team employee; valuable access but not organizationally independent |
| Omar Navarro | Los Angeles Chargers | team_analysis | Position previews, roster features, and camp reporting | Team employee; roster facts can be authoritative, evaluations require corroboration |

## Valuable monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Sam Farmer | Los Angeles Times | reporting | Veteran NFL reporting and selected on-site Chargers coverage | Broader NFL remit; not a daily Chargers-only feed |
| Daniel Popper | The Athletic | reporting | Historical Chargers context, personnel, contracts, and national NFL reporting | Inactive for daily Chargers monitoring after moving to a national role in July 2026 |
| Pro Football Reference | Sports Reference | data | Game logs, snap counts, rosters, and historical comparisons | Snap counts are unofficial; verify material discrepancies |
| Over the Cap | Over the Cap | contract_data | Contract structure, cap charges, and roster-management context | Third-party interpretation; cross-check consequential figures |
| Spotrac | Spotrac | contract_data | Contract, transaction, and roster reference | Useful cross-check, not an official transaction filing |
| Pro Football Focus | PFF | data | Proprietary charting, routes, alignments, pressures, and grades | Grades are evaluations and paid exports must not be committed |

## Supplemental monitoring

Podcasts, local radio, fantasy outlets, and aggregators can surface leads. Promote a claim into research only when it is attributable, reproducible, and supported by a source appropriate to the claim. Follow aggregations to the original report.

## Reliability history

### Baseline status

This is the initial Chargers registry. It does not assign blanket reliability grades. “Essential” means the source fills an important monitoring function, not that every statement should be accepted without verification.

- Strongest coverage areas: recorded per source in `sources.csv`.
- Known limitations: recorded in each source's `handling_note`.
- Confirmed early reports: none scored in the registry yet.
- Corrections or misses: none scored in the registry yet.
- Current reliability assessment: pending documented outcomes.
- Evidence for assessment: add dated examples and downstream record IDs before changing an assessment.

### Role-drift controls

Daniel Popper announced in late July 2026 that he was leaving the daily Chargers beat after seven seasons for a national NFL role focused on personnel, free agency, contracts, and the salary cap. Preserve his historical row as inactive. Do not name an Athletic replacement until the outlet verifies one.

## Usage notes

Start with official records and measured usage. Use reporting to establish what changed, analysis to explain why it matters, and later game evidence to test whether the interpretation held up. For a material fantasy conclusion, prefer one official or measured source plus one independent reporting source. If only one source supports a consequential claim, label it provisional and state the next test.

