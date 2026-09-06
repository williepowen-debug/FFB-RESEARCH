---
schema_version: 1
record_id: bw-2026-kc-registry-001
record_type: beat_writer_registry
title: "Kansas City Chiefs 2026 Source Registry"
team_ids: ["KC"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-21
last_verified: 2026-09-06
confidence: medium
source_ids: []
supersedes: []
writer_ids: ["local-writer-adam-teicher", "local-writer-jesse-newell", "local-writer-pete-sweeney", "local-writer-matt-derrick", "local-writer-harold-kuntz", "local-writer-kent-swanson", "local-writer-matt-lane", "local-writer-craig-stout", "local-writer-matt-mcmullen", "local-writer-nate-taylor"]
---

# Kansas City Chiefs 2026 source registry

The September 6 repair restores missing endpoints and usable independent fallbacks. Existing source IDs and historical assignment evidence are preserved. This is a bounded repair, not a claim that every outlet or current article is covered. Candidate dispositions and verification limits are explicit in [candidates.csv](candidates.csv); operational access lives in [endpoints.csv](endpoints.csv).

## Active source rotation

Rows retaining August verification dates were not fully reverified during this repair. An active legacy registration is not a claim of successful September access; consult the candidate and endpoint notes before assigning it.

| Source | Outlet | Class / priority | Verified identity or access handling |
|---|---|---|---|
| Kansas City Chiefs communications | Kansas City Chiefs | official / essential | Team analysis is not independent. Identity checkpoint: 2026-08-21. |
| NFL gamebooks and participation records | NFL | official / essential | Use postgame source of record. Identity checkpoint: 2026-08-21. |
| Jesse Newell | The Athletic | reporting / essential | Summarize paywalled work and attribute. Identity checkpoint: 2026-08-21. |
| Pete Sweeney | Kansas City Star | reporting / essential | Summarize paywalled work and attribute. Identity checkpoint: 2026-08-21. |
| Matt Derrick | Chiefs Digest | reporting / valuable | Author bio and August 29/30 2026 original article bodies opened September 6. Practical independent written fallback for blocked Athletic/ESPN bodies; verify sourcing inside each article and distinguish own reporting from team announcements. Identity checkpoint: 2026-09-06. |
| Harold Kuntz | FOX4 Kansas City | reporting / valuable | Distinguish reported facts from studio analysis. Identity checkpoint: 2026-08-21. |
| Kent Swanson | KC Sports Network | analysis / valuable | Current archive and dated byline verified September 6; selected article offers public metadata/preview with paid full content. Use archive rather than thin homepage; do not imply full film/video review from preview. Identity checkpoint: 2026-09-06. |
| Matt Lane | KC Sports Network | film_analysis / valuable | Current archive and dated byline verified September 6; selected article offers public metadata/preview with paid full content. Use archive rather than thin homepage; do not imply full film/video review from preview. Identity checkpoint: 2026-09-06. |
| Craig Stout | KC Sports Network | film_analysis / valuable | Analysis source; establish facts independently. Identity checkpoint: 2026-08-21. |
| Matt McMullen | Kansas City Chiefs | team_analysis / valuable | Team employee; not independent confirmation. Identity checkpoint: 2026-08-21. |
| Pro Football Reference | Sports Reference | data / valuable | Secondary reference. Identity checkpoint: 2026-08-21. |
| Nate Taylor | ESPN NFL Nation | reporting / essential | ESPN bio confirms assignment since July 2025 and current team index confirms byline. September 3 article body hit a JavaScript/robot challenge; readable metadata is not full article access. Use Matt Derrick for an accessible independent fallback. Identity checkpoint: 2026-09-06. |

## Historical source

Adam Teicher remains `local-writer-adam-teicher`, now inactive for new assignments. His exact end date is intentionally blank. ESPN names Nate Taylor as its Chiefs reporter since July 2025, corroborated by current team-index bylines. This corrects the prior registry assignment; it does not rewrite past observation attribution.

- [ESPN Nate Taylor biography](https://espnpressroom.com/bio/nate-taylor/) — verified September 6.
- [ESPN historical podcast archive](https://www.espn.com/espnradio/podcast/archive?id=27767948) — February 5, 2025 episode retirement context available through search metadata; direct page challenged.

## Coverage-lane matrix

| Lane | Source and current access boundary |
|---|---|
| Official record | Chiefs communications and NFL game centers; news and scores indexes opened, specific records require dated retrieval. |
| Daily independent beat | Nate Taylor identity and current byline metadata; Matt Derrick original written reporting is the practical full-body fallback. |
| National or major local reporting | ESPN Taylor role confirmed; selected body challenged. Sweeney Star profile confirms assignment; full newspaper access remains article-specific. Newell Athletic access unavailable. |
| Local television and radio | Derrick has a current September 2 New Day radio episode metadata listing; no audio content reviewed. Kuntz FOX4 endpoint failed and remains a television access gap. |
| Film and scheme analysis | KCSN Lane and Swanson dated public previews; full video/text paid. Stout current original-work verification incomplete. |
| Position usage and fantasy signal | Derrick reporting and KCSN explicitly classified analysis; fresh measured usage requires separate game evidence. |
| Transactions and organization | Chiefs official announcements and Derrick independently sourced articles; distinguish own sources from restated team facts. |
| Team-controlled analysis | Chiefs news and Matt McMullen legacy team-reporter entry; team articles do not independently corroborate beat interpretation. |

## Reliability history

Original registry established 2026-08-21. No source has been outcome-scored in this repair. Endpoint success is an access result, not a reliability grade. Older identity dates remain visible in sources.csv.

## Usage notes

For each future monitoring assignment, freeze the current source ID, exact endpoint, lane and time window. Open the supporting item, verify its byline and original publication timestamp, and report access failures honestly. Never substitute a bio, search snippet, paid preview or aggregator for an article body or a listened segment.

The [September 6 source-repair audit](../../../../../../intelligence/2026/2026-09-06-buf-kc-source-repair.md) records phases, omissions and limits.
