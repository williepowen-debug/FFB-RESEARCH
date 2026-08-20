---
schema_version: 1
record_id: bw-2026-nyj-registry-001
record_type: beat_writer_registry
title: "New York Jets 2026 Source Registry"
team_ids: ["NYJ"]
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
writer_ids: ["local-writer-rich-cimini", "local-writer-brian-costello", "local-writer-connor-hughes", "local-writer-chelsea-sherrod"]
---

# New York Jets 2026 Source Registry

This registry prioritizes sources that can establish or explain changes in availability, role,
usage, scheme, and roster construction. See [sources.csv](sources.csv),
[endpoints.csv](endpoints.csv), and the [monitoring guide](README.md).

## Essential monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| New York Jets communications | New York Jets | official | Transactions, roster, injury reports, practice reports, interviews | Source of record for team announcements; team-produced analysis is not independent |
| NFL gamebooks and participation records | NFL | official | Participation, starters, statistics, play-by-play | Preferred postgame source of record |
| Rich Cimini | ESPN NFL Nation | reporting | Daily beat reporting, roster, injuries and organizational context | ESPN identifies him as its Jets NFL Nation reporter |
| Brian Costello | New York Post | reporting | Practice observations, personnel, transactions and roster decisions | Podcast claims should be dated and linked to written reporting when possible |
| Connor Hughes | SNY | reporting | Jets and Giants NFL reporting, sources, roster and coaching context | Not Jets-exclusive; confirm whether a report is sourced or analytical |
| Chelsea Sherrod | SNY | reporting | On-site Jets reporting and video updates | SNY added the Jets reporter role in 2026; preserve the segment date |

## Valuable monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| New York Post Jets coverage | New York Post | reporting | Daily beat coverage, columns and rapid roster news | Attribute the individual byline and distinguish columns from reporting |
| SNY Jets coverage | SNY | reporting | News, video, interviews and analysis | Separate sourced reporting from studio interpretation |
| Pro Football Reference | Sports Reference | data | Game logs, snap counts and historical splits | Convenient secondary reference; verify consequential discrepancies |

## Reliability history

This registry was established on 2026-08-20. Priority reflects verified role and access, not a
blanket reliability grade. No repo-local record of confirmed early reports, corrections, or misses
has been accumulated yet.

### Rich Cimini

- Strongest coverage areas: daily beat reporting, roster status, injuries and organizational context.
- Known limitations: analysis and reporting may appear in the same notebook or podcast.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on verified assignment and access.
- Evidence for assessment: ESPN's current biography identifies Cimini as its Jets NFL Nation
  reporter, verified 2026-08-20.

### Brian Costello

- Strongest coverage areas: practice observation, personnel competition, roster decisions.
- Known limitations: podcast delivery requires precise episode dating and claim-level attribution.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on current beat assignment.
- Evidence for assessment: the New York Post's current Gang's All Here program identifies Costello
  as its Jets beat writer and carries 2026 camp observations, verified 2026-08-20.

### SNY reporting team

- Strongest coverage areas: sourced coaching news, roster context, on-site video and interviews.
- Known limitations: Connor Hughes covers both New York teams; television segments require dates.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on verified current roles.
- Evidence for assessment: SNY identifies Hughes as its NFL insider covering the Jets and Giants
  and Chelsea Sherrod as its Jets reporter beginning in 2026, verified 2026-08-20.

## Usage notes

Start with official records, then use independent practice reporting to explain changes and game
usage to test whether preseason observations held. Attribute the individual reporter rather than
only the outlet. For a material fantasy conclusion, prefer one official or measured source plus
one independent reporting source. Time-stamp podcasts, live blogs, and television segments.
