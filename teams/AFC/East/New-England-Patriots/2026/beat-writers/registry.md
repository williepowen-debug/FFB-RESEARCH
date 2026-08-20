---
schema_version: 1
record_id: bw-2026-ne-registry-001
record_type: beat_writer_registry
title: "New England Patriots 2026 Source Registry"
team_ids: ["NE"]
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
writer_ids: ["local-writer-mike-reiss", "local-writer-andrew-callahan", "local-writer-doug-kyed", "local-writer-christopher-price", "local-writer-nicole-yang"]
---

# New England Patriots 2026 Source Registry

This registry prioritizes sources that can establish or explain changes in availability, role,
usage, scheme, and roster construction. See [sources.csv](sources.csv),
[endpoints.csv](endpoints.csv), and the [monitoring guide](README.md).

## Essential monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| New England Patriots communications | New England Patriots | official | Transactions, roster, injury reports, transcripts, practice reports | Source of record for team announcements; team-produced analysis is not independent |
| NFL gamebooks and participation records | NFL | official | Participation, starters, statistics, play-by-play | Preferred postgame source of record |
| Mike Reiss | ESPN NFL Nation | reporting | Daily beat reporting, availability, roster and organizational context | ESPN identifies him as its Patriots NFL Nation reporter |
| Andrew Callahan | Boston Herald | reporting | Practice observations, roster, scheme and sourced reporting | Separate reported facts from columnist analysis |
| Doug Kyed | Boston Herald | reporting | Daily beat reporting, personnel, transactions and league sourcing | Podcast claims should be dated and corroborated when consequential |
| Christopher Price | Boston Globe | reporting | Training-camp observations, personnel and team context | Globe content is generally paywalled; summarize in original language |
| Nicole Yang | Boston Globe | reporting | Beat reporting, player roles, roster moves and features | Favor direct observations and sourced facts for role conclusions |

## Valuable monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Ben Volin | Boston Globe | reporting | Senior NFL reporting and Patriots organizational context | Commentary and league analysis should not be treated as transaction confirmation |
| Patriots Unfiltered | New England Patriots | team_analysis | Practice discussion, interviews and team context | Team-produced; useful detail without organizational independence |
| Pro Football Reference | Sports Reference | data | Game logs, snap counts and historical splits | Convenient secondary reference; verify consequential discrepancies |

## Reliability history

This registry was established on 2026-08-20. Priority reflects verified role and access, not a
blanket reliability grade. No repo-local record of confirmed early reports, corrections, or misses
has been accumulated yet.

### Mike Reiss

- Strongest coverage areas: roster status, availability, organizational context, daily beat reporting.
- Known limitations: national-platform articles may be updated after initial publication.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on verified assignment and access.
- Evidence for assessment: ESPN's current biography identifies Reiss as its New England Patriots
  NFL Nation reporter, verified 2026-08-20.

### Boston Herald beat rotation

- Strongest coverage areas: practice observation, personnel competition, transactions and scheme.
- Known limitations: reporting and analysis can appear in the same article or podcast.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on current beat assignments.
- Evidence for assessment: current 2026 outlet and podcast materials identify Andrew Callahan and
  Doug Kyed with the Patriots beat, verified 2026-08-20.

### Boston Globe beat rotation

- Strongest coverage areas: camp observation, player roles, roster and organizational context.
- Known limitations: paywall; multiple bylines require claim-level attribution.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on current beat assignments.
- Evidence for assessment: current Globe profiles and 2026 coverage identify Christopher Price
  and Nicole Yang as Patriots beat reporters, verified 2026-08-20.

## Usage notes

Start with official records, then use independent practice reporting to explain changes and game
usage to test whether preseason observations held. Attribute the individual reporter rather than
only the outlet. For a material fantasy conclusion, prefer one official or measured source plus
one independent reporting source. Time-stamp podcast and live-blog claims.
