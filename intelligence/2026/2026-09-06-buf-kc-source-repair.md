---
schema_version: 1
record_id: rf-2026-buf-kc-source-repair-001
record_type: research_finding
title: "BUF and KC September 6 source-access repair"
team_ids: ["BUF", "KC"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-09-06
last_verified: 2026-09-06
confidence: medium
source_ids: []
supersedes: []
---

# BUF and KC source-access repair

## Finding

The repair provides usable independent intake paths and corrects Kansas City's ESPN assignment.
It does not collect football observations, reopen completed reader runs, or claim a complete
current audit of every legacy source. All access checks below occurred September 6, 2026.

## Evidence

### Discovery and omission review

Initial discovery inspected the two existing registries, current outlet biographies, news indexes,
and selected bylined items. The legacy directories lacked `candidates.csv`; durable ledgers were
added during discovery before construction. The initial candidate sets contain 10 BUF identities
and 13 KC identities, including the newly discovered Nate Taylor assignment.

A separate omission pass used fresh reporter, podcast and film-analysis queries and community
recommendations strictly as discovery leads. It checked WKBW, Cover 1, the Star, and KCSN primary
pages and identified additional newspaper, television and podcast candidates. Candidates lacking
current original evidence remain explicitly unverified. Verified optional sources were excluded
from activation when they would broaden or duplicate this focused repair.

After construction, another publisher-restricted omission search found additional WGR interview
metadata, including Buscaglia and Matt Parrino. No audio was heard and no football claim was
derived from it. Parrino was added to the discovery ledger as unverified.

## Sources

| Source | Evidence and usable path | Limit |
|---|---|---|
| `local-writer-joe-buscaglia` | Added the [Athletic author page](https://www.nytimes.com/athletic/author/joe-buscaglia/) and team feed; his [current self-profile](https://bsky.app/profile/joebuscaglia.bsky.social) identifies the Bills beat | Both Athletic endpoints failed to open. The self-profile and older publisher episode do not replace fresh publisher verification. His August identity date is retained. |
| `local-writer-sal-capaccio` | [WGR Bills section](https://www.audacy.com/wgr550/sports/bills) and a [September 1 bylined practice report](https://www.audacy.com/wgr550/sports/bills/bills-get-key-players-back-at-practice-tuesday) opened | The author listing is stale and the homepage returned 403. Use the current section and exact byline; distinguish his observations from embedded third-party reporting. |
| `local-writer-nate-taylor` | [ESPN biography](https://espnpressroom.com/bio/nate-taylor/) identifies the Chiefs assignment since July 2025; current team index carries his byline | A selected September 3 article encountered a JavaScript challenge. Metadata confirms identity; it does not provide article evidence. |
| `local-writer-adam-teicher` | Retained as inactive historical identity, with Taylor recorded as replacement | [ESPN archival episode metadata](https://www.espn.com/espnradio/podcast/archive?id=27767948) discussed impending summer retirement in February 2025; the exact end day remains blank. No past attribution is changed. |
| `local-writer-matt-derrick` | [Author archive](https://chiefsdigest.com/author/admin/) and [August 29 original reporting](https://chiefsdigest.com/chiefs-acquire-ot-diego-pounds-from-baltimore-for-2028-conditional-sixth-rounder/) opened, as did his August 30 roster article | Practical independent written fallback. A roster transcription and an independently sourced report have different evidentiary value. |
| KCSN Lane / Swanson / Stout | Added the usable [dated archive](https://www.kcsn.com/archive); Lane's September 1 and Swanson's August 27 bylines and previews opened | The homepage exposed only an image; full selected content is paid. Stout's current original-work role was not separately reverified. |

Missing BUF NFL game-center and Two Bills Drive endpoints were also supplied. The latter is
discovery-only aggregation. Buffalo News redirected to a Tollbit endpoint without an inspected
article body; FOX4 retrieval failed; Athletic access remains unavailable. These are access gaps,
not findings of no news. Podcast metadata for Joe B. Football was discovered but direct retrieval
failed; the old Buffalo Beat title is no longer asserted as verified current branding.

## Coverage and reconciliation

Both registries now contain all eight required coverage lanes, with unavailable fresh evidence
explicitly identified. BUF current independent written coverage is supplied by Capaccio; its fresh
national/major-local original-body and full film-review lanes remain unavailable in this repair.
KC has Derrick's full original reporting, Taylor's verified current assignment, and dated KCSN
analysis previews. Full paid analysis and television access remain limited.

- BUF: 10 retained source IDs, 17 endpoints, 20 candidate rows; 4 included, 3 excluded from the
  activated rotation, 13 unverified in this repair. Nine source endpoints were added.
- KC: 13 source IDs including one addition, 26 endpoints, 20 candidate rows; 7 included, 5 excluded
  from the activated rotation, 8 unverified. Eleven endpoints were added; one existing mapping was
  clarified as historical.
- Every source has an endpoint; every included person has a registry `writer_id`; all existing
  stable identities remain present. Unverified legacy rows retain their prior identity dates and
  are not claimed as freshly audited. No new monitoring assignment should rely solely on them.
- WKBW's Matt Bové and Cover 1 were verified optional discoveries, not added to the source rotation.
  The [WKBW bio](https://www.wkbw.com/matt-bove) exposes original practice reporting; the
  [Cover 1 site](https://www.cover1.net/about-cover-1/) and a 2026 Film Room sample establish a
  differentiated film option for a later assignment.

The scoped files are the five registry artifacts in each team directory plus this audit.
ARCHITECT owns catalog regeneration and publication. Marking Teicher inactive exposed a historical
assignment validation issue: the validator originally required every past assignment's source to
remain active today. Historical IDs and runs are preserved; ARCHITECT corrected historical validation to resolve registered identities; active-source selection
remains a new-run preflight responsibility. Regression checks cover retirement and removal.

## Fantasy implication

Future fantasy updates can reach accessible independent reporting instead of repeatedly exhausting
a blocked endpoint or assigning a historical reporter. This repair makes no player-role, ranking
or lineup change.

## Assessment

Confidence is high in the verified assignment correction and observed endpoint outcomes, and medium
in overall coverage because substantial legacy and paid-source verification remains incomplete.
A changed outlet assignment or a newly failing endpoint would require another source check.

### Next review

Use the repaired Capaccio and Derrick paths for new bounded assignments. Recheck exact supporting
item timestamps and bylines at intake. Reverify blocked publisher roles and inspect paid or audio
content only through authorized access; do not infer their content from snippets. Source access
success has not been converted into a scored reporting-reliability judgment.
