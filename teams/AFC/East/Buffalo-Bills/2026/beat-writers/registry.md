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
last_verified: 2026-09-06
confidence: medium
source_ids: []
supersedes: []
writer_ids: ["local-writer-joe-buscaglia", "local-writer-katherine-fitzgerald", "local-writer-sal-capaccio"]
---

# Buffalo Bills 2026 source registry

The September 6 repair restores missing endpoints and usable independent fallbacks. Existing source IDs and historical assignment evidence are preserved. This is a bounded repair, not a claim that every outlet or current article is covered. Candidate dispositions and verification limits are explicit in [candidates.csv](candidates.csv); operational access lives in [endpoints.csv](endpoints.csv).

## Active source rotation

Rows retaining August verification dates were not fully reverified during this repair. An active legacy registration is not a claim of successful September access; consult the candidate and endpoint notes before assigning it.

| Source | Outlet | Class / priority | Verified identity or access handling |
|---|---|---|---|
| Buffalo Bills communications | Buffalo Bills | official / essential | Source of record for team announcements; team-produced editorial and analysis are not independent. Identity checkpoint: 2026-08-20. |
| NFL gamebooks and participation records | NFL | official / essential | Use the game-specific book or game center as the postgame source of record. Identity checkpoint: 2026-08-20. |
| Joe Buscaglia | The Athletic | reporting / essential | Athletic author/team pages could not be opened September 6. Current self-profile still identifies Bills beat role; fresh publisher role/byline verification remains incomplete. Podcast-title metadata is a discovery lead only. Use registered Sal Capaccio written reporting for accessible independent intake; do not substitute aggregates for Athletic article bodies. Identity checkpoint: 2026-08-20. |
| Katherine Fitzgerald | Buffalo News | reporting / essential | Maintains a running 2026 offseason coverage collection. Partial paywall. Identity checkpoint: 2026-08-20. |
| Sal Capaccio | WGR 550 / Audacy | reporting / essential | Current bylined written practice reporting and Bills section verified September 6. Author article list is stale; use the section and inspect each byline. Audio requires a dated segment/timecode. WGR homepage returned 403 while section/article opened. Identity checkpoint: 2026-09-06. |
| ESPN Bills coverage | ESPN | reporting / valuable | National desk; camp intel posts are updated in place so record the retrieval date. Identity checkpoint: 2026-08-20. |
| Bills Central | Sports Illustrated / OnSI | analysis / valuable | Aggregation and analysis; verify primary claims against official or beat sources. Identity checkpoint: 2026-08-20. |
| Buffalo Rumblings | SB Nation | analysis / valuable | Community analysis; useful for structured player breakdowns but not a reporting source of record. Identity checkpoint: 2026-08-20. |
| Two Bills Drive | Two Bills Drive | analysis / situational | Aggregates other outlets' reporting; always trace to the originating reporter before relying on a claim. Identity checkpoint: 2026-08-20. |
| Pro Football Reference | Sports Reference | data / valuable | Snap counts are unofficial; verify material discrepancies. Rate-limits automated access. Identity checkpoint: 2026-08-20. |

## Coverage-lane matrix

| Lane | Source and current access boundary |
|---|---|
| Official record | Bills communications and NFL game centers; official news and scores index opened. Specific injury/transaction/gamebook content still requires its own dated retrieval. |
| Daily independent beat | Sal Capaccio: current WGR section and bylined practice article opened; Buscaglia primary article access remains unavailable. |
| National or major local reporting | Unavailable as a fully reverified current original-body lane in this repair. Legacy ESPN/Buffalo News rows retained; Fitzgerald section redirected to Tollbit and Athletic body was blocked. |
| Local television and radio | Sal Capaccio written and radio rotation; Matt Bové independently verified as an optional discovery fallback, not activated to duplicate the current repair. |
| Film and scheme analysis | Fresh full film review unavailable in this repair. Buffalo Rumblings legacy analysis retained; Cover 1 primary 2026 film example verified and dispositioned as an optional specialist. |
| Position usage and fantasy signal | Capaccio firsthand practice reporting and Bills official context; neither nominal participation nor commentary establishes measured route shares. |
| Transactions and organization | Bills official announcements plus independently attributed Capaccio reporting; Two Bills Drive remains discovery-only aggregation. |
| Team-controlled analysis | Bills news/interview index; in-house analysis is not independent confirmation. |

## Reliability history

Original registry established 2026-08-20. No source has been outcome-scored in this repair. Endpoint success is an access result, not a reliability grade. Older identity dates remain visible in sources.csv.

## Usage notes

For each future monitoring assignment, freeze the current source ID, exact endpoint, lane and time window. Open the supporting item, verify its byline and original publication timestamp, and report access failures honestly. Never substitute a bio, search snippet, paid preview or aggregator for an article body or a listened segment.

The [September 6 source-repair audit](../../../../../../intelligence/2026/2026-09-06-buf-kc-source-repair.md) records phases, omissions and limits.
