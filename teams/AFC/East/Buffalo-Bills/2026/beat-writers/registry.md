---
schema_version: 1
record_id: bw-2026-buf-registry-001
record_type: beat_writer_registry
title: "Buffalo Bills 2026 Source Registry"
team_ids: ["BUF"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-20
last_verified: 2026-08-20
confidence: medium
source_ids: []
supersedes: []
writer_ids: ["local-writer-joe-buscaglia", "local-writer-katherine-fitzgerald", "local-writer-sal-capaccio"]
---

# Buffalo Bills 2026 Source Registry

This registry prioritizes sources that can establish or explain changes in
availability, role, usage, scheme, and roster construction. Priority describes
monitoring frequency; source class describes function. See [sources.csv](sources.csv),
[endpoints.csv](endpoints.csv), and the [monitoring guide](README.md).

## Essential monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Buffalo Bills communications | Buffalo Bills | official | Transactions, roster, unofficial depth chart, injury reports, transcripts, daily camp reports | Source of record for team announcements; editorial analysis is not independent |
| NFL gamebooks and participation records | NFL | official | Game participation, starters, statistics, play-by-play | Preferred postgame source of record |
| Joe Buscaglia | The Athletic | reporting | Daily beat reporting, roster construction, personnel, camp observation | Hosts The Buffalo Beat; paywalled, so summarize rather than reproduce |
| Katherine Fitzgerald | Buffalo News | reporting | Offseason and camp coverage, transactions, practice observation | Maintains a running 2026 offseason collection; partial paywall |
| Sal Capaccio | WGR 550 / Audacy | reporting | Daily radio reporting on roster, staff, and draft | Radio-first; time-stamp audio claims and prefer written corroboration |

## Valuable monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| ESPN Bills coverage | ESPN | reporting | Camp intel, free-agency tracking, injury reporting | Camp intel posts are updated in place; record the retrieval date with any claim |
| Bills Central | Sports Illustrated / OnSI | analysis | Snap counts, depth-chart reads, injury interpretation, roster bubble | Aggregation and analysis; verify primary claims upstream |
| Buffalo Rumblings | SB Nation | analysis | Structured scouting reports and roster analysis | Community analysis, not a reporting source of record |
| Pro Football Reference | Sports Reference | data | Game logs, snap counts, season and career splits | Snap counts unofficial; returned HTTP 403 to automated retrieval on 2026-08-20 |

## Situational monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Two Bills Drive | Two Bills Drive | analysis | Injury-timeline aggregation and coaching notes | Aggregates others' reporting; trace to the originating reporter before relying on a claim |

## Reliability history

This registry is newly established on 2026-08-20. No reliability judgments have been
earned from observed outcomes yet. The entries below record only what has been
verified about each source's role and access, plus the first checkpoints against which
reliability will be scored.

### Joe Buscaglia

- Strongest coverage areas: roster construction, personnel decisions, camp observation.
- Known limitations: paywalled; podcast segments are harder to date and cite precisely.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; treated as essential on role and access.
- Evidence for assessment: identified as The Athletic's Bills beat reporter and host of
  The Buffalo Beat, verified 2026-08-20.

### Katherine Fitzgerald

- Strongest coverage areas: offseason transaction sequencing and camp practice reports.
- Known limitations: partial paywall; individual bylines require checking against the
  Buffalo News Bills section index.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; treated as essential on role and access.
- Evidence for assessment: maintains a running Buffalo News collection covering the
  2026 Bills offseason, verified 2026-08-20.

### Sal Capaccio

- Strongest coverage areas: daily roster and staff news, draft coverage.
- Known limitations: radio-first delivery makes precise dating and quotation harder;
  the repository's existing Bills staff records already lean on WGR 550 reporting.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; treated as essential on role and access.
- Evidence for assessment: identified as a longtime Bills reporter and Buffalo radio
  host, verified 2026-08-20.

### First scoring checkpoints

Score these sources against outcomes already in motion, in this order:

1. Connor McGovern's actual Week 1 availability against each source's reported
   two-to-four-week timeline.
2. The left-guard winner between Alec Anderson and Austin Corbett against each
   source's preseason depth-chart read.
3. Whether James Cook's Weeks 1-4 route participation matches the receiving expansion
   attributed to Pete Carmichael.

## Usage notes

Attribute individual reports, distinguish reporting from interpretation, and update
reliability judgments from documented outcomes rather than reputation alone. Buffalo's
camp-intel pages at national outlets are updated in place, so always record the date a
claim was retrieved rather than assuming the page's publication date. Where a claim
originates in a podcast or radio segment, cite the segment and date and prefer a
written corroboration when one exists.
