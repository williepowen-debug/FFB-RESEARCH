---
schema_version: 1
record_id: bw-2026-atl-registry-001
record_type: beat_writer_registry
title: "Atlanta Falcons 2026 Source Registry"
team_ids: ["ATL"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-17
last_verified: 2026-08-17
confidence: high
source_ids: []
supersedes: []
writer_ids: ["local-writer-will-mcfadden", "local-writer-kelsey-conway", "local-writer-tori-mcelhaney", "local-writer-josh-kendall", "local-writer-daniel-flick", "local-writer-marc-raimondi", "local-writer-michael-rothstein", "local-writer-d-orlando-ledbetter"]
---

# Atlanta Falcons 2026 Source Registry

Candidate discovery and omission-pass decisions are recorded in [candidates.csv](candidates.csv).

This registry prioritizes sources that can establish or explain changes in player availability, role, usage, coaching, scheme, and roster construction for the 2026 Atlanta Falcons. Priority describes monitoring frequency; source class describes function. See [sources.csv](sources.csv) for normalized records, [endpoints.csv](endpoints.csv) for links, and the [monitoring guide](README.md) for the operating workflow.

The 2026 Falcons beat had material turnover: D. Orlando Ledbetter retired from the AJC after roughly two decades on the beat (March 2026) and Daniel Flick took the AJC beat (May 2026); Marc Raimondi is ESPN's Falcons NFL Nation reporter after Michael Rothstein moved to enterprise work. Weight current-role sources accordingly.

## Essential monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Atlanta Falcons communications | Atlanta Falcons | official | Injury reports, transactions, transcripts, press conferences, unofficial depth chart | Source of record for team announcements; team-produced analysis is not organizationally independent |
| Will McFadden | Atlanta Falcons | official | Camp previews, roster notes, and the club's unofficial depth chart | Team-employed; publishes the official-voice depth chart, not independent reporting |
| Kelsey Conway | Atlanta Falcons | official | Roster moves, transactions, presser recaps, video | Team-employed; watch promotional framing and cross-check consequential claims |
| Tori McElhaney | Atlanta Falcons | official | Feature depth, locker-room access, scheme and roster context | Strong reporting pedigree (ex-The Athletic beat) but now an official voice |
| Josh Kendall | The Athletic | reporting | Sourced beat reporting, roster analysis, quarterback room | Subscription paywall; separate sourced reporting from column analysis |
| Daniel Flick | Atlanta Journal-Constitution | reporting | Daily beat, camp intel, offensive line and right-tackle coverage | Took the AJC beat May 2026; favor concrete observations over camp evaluations |
| Marc Raimondi | ESPN (NFL Nation) | reporting | Camp intel, position battles, roster cuts, quarterback room | Primary ESPN Falcons voice since 2024; separate reporting from national speculation |

## Valuable monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| D. Orlando Ledbetter | BowtieSports (independent) | reporting | Long institutional memory, historical and organizational context | Retired from the AJC beat March 2026; now independent at a lower cadence |
| NFL communications | NFL | official | League transactions, suspensions, official announcements | Authoritative on suspensions (e.g., Pearce) and official transactions |
| The Falcoholic | SB Nation | team_analysis | Daily camp notes, unofficial depth-chart breakdowns, position battles | Fan-site with consistent daily coverage; attribute the individual author |
| Pro Football Reference | Sports Reference | data | Game logs, snap counts, rosters, historical comparisons | Snap counts are unofficial; not a real-time camp source |
| Pro Football Focus | PFF | film_analysis | Grades, alignment, route and pressure data | Proprietary methodology; grades are evaluations, not facts |
| Over the Cap | Over the Cap | contract_data | Contract structure, cap charges, dead money | Third-party interpretation; cross-check unusual figures |

## Supplemental monitoring

Michael Rothstein (ESPN enterprise) surfaces on off-field and legal items rather than daily camp coverage. Blogging Dirty (FanSided) and Spotrac are aggregation and reference sources; add a claim from them to a research record only when it is attributable, reproducible, and relevant, and follow the link back to the original report.

## Reliability history

### Baseline status

This is the initial 2026 registry. It does not assign blanket reliability grades because no repo-local outcome history has been recorded yet. "Essential" means the source fills an important monitoring function, not that every claim should be accepted without verification.

- Strongest coverage areas: recorded per source in `sources.csv`.
- Known limitations: recorded in each source's `handling_note`.
- Confirmed early reports: none logged in this registry yet.
- Corrections or misses: none logged in this registry yet.
- Current reliability assessment: pending documented outcomes.
- Evidence for assessment: add dated examples and downstream record IDs before changing an assessment.

### Role-drift controls

Role changes are retained as status data, not deletions. D. Orlando Ledbetter's move from AJC Falcons beat writer to independent publisher is recorded with `former_role` and `ended_on`; Daniel Flick is recorded as his AJC replacement. Michael Rothstein's move from Falcons beat to enterprise work is recorded with Marc Raimondi as the replacement on the beat. Future departures should set `status` to `inactive` and populate `ended_on`, `former_role`, and `replacement_if_known` rather than deleting history.

## Usage notes

Start with official records and direct observations. Use reporting to establish what changed, analysis to explain why it matters, and measured usage to test whether the interpretation held up. Attribute individual reports, distinguish reporting from interpretation, and update reliability judgments from documented outcomes rather than reputation alone.

For a material fantasy conclusion, prefer one official or measured source plus one independent reporting source. Team-employed reporters (McFadden, Conway, McElhaney) are valuable for access and detail but are not organizationally independent; pair their consequential claims with Kendall, Flick, or Raimondi. If only one source supports a consequential claim, label the conclusion provisional and state the next verification step.
