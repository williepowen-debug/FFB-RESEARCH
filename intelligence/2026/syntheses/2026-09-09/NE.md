---
schema_version: 1
record_id: "ti-2026-ne-20260909-001"
record_type: "team_intelligence"
title: "New England Patriots intelligence synthesis — 2026-09-09"
team_ids: ["NE"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-09"
last_verified: "2026-09-09"
confidence: "high"
source_ids: ["local-source-new-england-patriots", "local-writer-mike-reiss", "local-writer-doug-kyed", "local-writer-andrew-callahan"]
supersedes: []
observation_ids: ["obs-2026-ne-20260909t210706z-001", "obs-2026-ne-20260909t210706z-002", "obs-2026-ne-20260909t210706z-003", "obs-2026-ne-20260909t210706z-004", "obs-2026-ne-20260909t210706z-005", "obs-2026-ne-20260909t210706z-006", "obs-2026-ne-20260909t210706z-007", "obs-2026-ne-20260909t210706z-008", "obs-2026-ne-20260909t210706z-009", "obs-2026-ne-20260909t210706z-010", "obs-2026-ne-20260909t210706z-011", "obs-2026-ne-20260909t210706z-012"]
run_ids: ["20260909T210706Z"]
---

# New England Patriots intelligence synthesis — 2026-09-09

Pre-kickoff snapshot for the Week 1 opener at Seattle (2026-09-09, 8:20 PM ET). The game has not
been played; nothing below is postgame or measured-usage evidence.

## Executive signal

TreVeyon Henderson is officially OUT for Week 1 (ankle; DNP Sunday through Tuesday), which resolves
the September 6 next-check and makes Rhamondre Stevenson the lead back by availability. Corey Kiner
is the reported No. 2 and practice-squad elevation Lan Larison the third back. Ben Brown is OUT but
the starting five offensive linemen are reported intact. Barmore carries no designation. The
Gonzalez extension and the Wishnowsky elevation are contract- and special-teams-lane facts only.

## Reconciled evidence

Twelve rows collapse into nine originating clusters. Grouped by `dedup_key`; read the atomic claims
in the [reader batch](../../runs/20260909T210706Z/reader-ne/observations.csv) and the coverage
record in the [run report](../../runs/20260909T210706Z/reader-ne/run-report.csv).

1. **Henderson OUT** (`ne-w01-henderson-out`) — official fact.
   `obs-2026-ne-20260909t210706z-001` is the team's dated Week 1 injury-report article (DNP/DNP/DNP,
   OUT). It `update`s the September 5 "assess at practice" briefing
   (`obs-2026-ne-20260906t193157z-002`) and Reiss's September 6 "has not practiced since August 24"
   report (`obs-2026-ne-20260906t210715z-001`). `obs-2026-ne-20260909t210706z-008` (Reiss, ESPN)
   restates the designation and is a `repeat`, not corroboration; Kyed's
   `obs-2026-ne-20260909t210706z-009` also carries it without a separate row. One origin, official.
2. **Ben Brown OUT** (`ne-w01-brown-out`) — official fact, `obs-2026-ne-20260909t210706z-002`; same
   official item as cluster 1. The report notes he did not travel. One origin, official.
3. **Barmore full participation, no designation** (`ne-w01-barmore-full-no-designation`) — official
   fact, `obs-2026-ne-20260909t210706z-003`; same official item. The team-site analysis in cluster 7
   had anticipated his removal from the report; the official item confirms it. Defense only.
4. **Larison elevated** (`ne-w01-elevation-larison`) — official transaction,
   `obs-2026-ne-20260909t210706z-004`. Kyed's `obs-2026-ne-20260909t210706z-010` is a `repeat` of the
   transaction with depth framing (Larison behind Stevenson and Kiner; Haskins stays on the practice
   squad). Larison, not Haskins, was chosen. One origin, official.
5. **Wishnowsky elevated at punter** (`ne-w01-elevation-wishnowsky`) — official transaction,
   `obs-2026-ne-20260909t210706z-005`; Baringer's IR status comes from the roster page and predates
   the window. Special teams only.
6. **Starting five intact; Van Roten primary interior backup** (`ne-w01-ol-brown-backup-van-roten`)
   — team-site analysis, `obs-2026-ne-20260909t210706z-006`. Team-produced, so not organizationally
   independent, but it is the only item that addresses the center question and it is consistent
   with Kyed describing Brown as a backup guard/center in `obs-2026-ne-20260909t210706z-009`. One
   analysis origin plus one independent beat description of Brown's role.
7. **Stevenson primary, Kiner No. 2, elevation candidate third**
   (`ne-w01-backfield-stevenson-lead`) — `obs-2026-ne-20260909t210706z-007` is team-site analysis
   (Lazar); `obs-2026-ne-20260909t210706z-009` (Kyed, Boston Herald) independently `confirm`s the
   same depth order. Reiss's `obs-2026-ne-20260909t210706z-008` states the same order but is rowed
   as a repeat of the designation and is not counted. Independent origins: two (team analysis plus
   one independent beat reporter). Both are interpretations of a depth chart that is forced by
   Henderson's absence; neither is measured usage, and both plausibly draw on the same team
   briefings. Sufficient to describe the Week 1 depth order as reported; insufficient to say
   anything about the Stevenson–Henderson split when both are healthy.
8. **Stevenson as the only back trusted in pass protection; Larison in a scout-team jersey**
   (`ne-w01-stevenson-pass-pro-only-trusted-back`) — `obs-2026-ne-20260909t210706z-011` (Callahan,
   September 7 column). The jersey detail is a firsthand practice observation from September 6 and
   is consistent with Larison's practice-squad status before the September 9 elevation. The
   pass-protection judgment is columnist analysis written before the official designation. One
   origin; the analysis portion stays interpretation.
9. **Gonzalez four-year extension** (`ne-w01-gonzalez-extension`) — reported fact,
   `obs-2026-ne-20260909t210706z-012` (Kyed, citing Schultz as first reporter; a team-site "Report:"
   item citing Rapoport was inspected but not rowed). The earliest origin was not retrieved and the
   team's own confirmation is a photo post rather than a retrieved announcement, so this remains a
   reported fact. Contract lane only.

Kind separation: clusters 1–5 are official facts; 6 and 7 are analysis and reported interpretation;
8 mixes a firsthand observation with analysis; 9 is a reported fact. No measured data arrived.

## Hypothesis impact

Baseline read: [offense hypotheses](../../../../teams/AFC/East/New-England-Patriots/2026/offense/hypotheses.csv),
[defense hypotheses](../../../../teams/AFC/East/New-England-Patriots/2026/defense/hypotheses.csv),
[backfield timeshare finding](../../../../teams/AFC/East/New-England-Patriots/2026/offense/backfield-timeshare.md),
the [September 6 synthesis](../2026-09-06/NE.md), the
[September 6 readiness supplement](../2026-09-06/NE-readiness.md), and
[`wm-2026-w01-ne-sea-001`](../../../../weekly/2026/week-01/games/NE-at-SEA.md).

- `wm-2026-w01-ne-sea-001`: **changes.** The conditional Henderson row and the "official
  participation and final designation" next check are answered. Henderson is OUT; Stevenson leads
  by availability with Kiner and Larison behind him; Brown is OUT with the starting five reported
  intact; Barmore has no designation. The weekly record should carry these dated facts and
  replace the Stevenson/Henderson split question with a Stevenson/Kiner measurement question.
- `ne-2026-off-q06` (Stevenson lead early-down/short-yardage): **contextual, no change.** Week 1
  will show Stevenson leading, but by absence rather than by choice, so it cannot supply the
  hypothesis's confirming or disconfirming evidence ("Henderson takes a three-down role; committee
  by series"). The two reported-depth origins describe a forced order, not the contested split.
- `ne-2026-off-q07` (Henderson passing-down role): **contextual, no change.** Henderson does not
  play. The review trigger "first two regular-season games" should not count Week 1 as one of the
  two games that test his passing-down share; ARCHITECT may wish to note that in the ledger.
- `rf-2026-ne-backfield-timeshare-001`: **no change.** Its stated next review is "Week 1 usage
  charting"; that charting will be a Henderson-absent sample. Useful for Stevenson's absolute
  route and two-minute involvement and for Kiner's role, not for the timeshare resolution.
- `ne-2026-off-q09` (offensive line): **weakly supportive, contextual.** "Starting five intact" and
  a named interior backup come from one team-produced analysis; Brown's OUT status removes a
  reserve, not a starter. No promotion.
- `ne-2026-def-q06` (Gonzalez): **no change.** An extension is neither a role nor a health change.
- `ne-2026-def-q02` (Dre'Mont Jones): **no evidence.** Barmore's availability is adjacent context
  for the interior rotation only.

The independent-origin bar for a hypothesis review on q06/q07/rf-001 is not reached: the only
official fact is availability, and the role reporting is two interpretive origins describing a
forced depth chart. The bar for escalating the availability change itself is met by the official
designation and the immediate lineup consequence.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| escalate | Henderson officially OUT for Week 1; Stevenson is the lead back by availability with Kiner No. 2 and Larison elevated as the third back. | `obs-2026-ne-20260909t210706z-001`; `obs-2026-ne-20260909t210706z-004`; `obs-2026-ne-20260909t210706z-007`; `obs-2026-ne-20260909t210706z-009` | Promote the dated designation and reported depth order to `wm-2026-w01-ne-sea-001`; treat Henderson as unavailable in every Week 1 lineup decision; close the September 6 Henderson next-check. Then chart actual Stevenson and Kiner carries, routes, two-minute and goal-line work postgame. |
| review | Week 1 backfield usage is a Henderson-absent sample and must not be read as evidence on the Stevenson–Henderson split; Kiner (about five practices) and Larison depth and Callahan's pass-protection assessment need measured usage before any seasonal claim. | `obs-2026-ne-20260909t210706z-007`; `obs-2026-ne-20260909t210706z-009`; `obs-2026-ne-20260909t210706z-010`; `obs-2026-ne-20260909t210706z-011` | Record a deferred disposition against `ne-2026-off-q06`, `ne-2026-off-q07`, and `rf-2026-ne-backfield-timeshare-001`; next trigger is postgame Week 1 snap, route, and goal-line data for Stevenson and Kiner, plus Henderson's Week 2 practice participation. |
| log | Ben Brown OUT (did not travel); starting five reported intact with Van Roten the primary interior backup. | `obs-2026-ne-20260909t210706z-002`; `obs-2026-ne-20260909t210706z-006` | Note in the weekly injury context; no change to `ne-2026-off-q09` until protection or first-unit rotation evidence exists. |
| log | Barmore full participation Monday and Tuesday, no designation. | `obs-2026-ne-20260909t210706z-003` | None for offense; defense context only. |
| log | Gonzalez four-year extension reported (Kyed citing Schultz). | `obs-2026-ne-20260909t210706z-012` | None; contract lane. Update a player or contract record only if one is later created. |
| log | Wishnowsky elevated at punter with Baringer on IR. | `obs-2026-ne-20260909t210706z-005` | None; special teams. |
| log | Reiss and Kyed recirculations of the official designation and elevation. | `obs-2026-ne-20260909t210706z-008`; `obs-2026-ne-20260909t210706z-010` | None; retained as provenance for the depth framing, not counted as independent evidence. |

Fantasy implication for the escalated signal: Henderson cannot be started; Stevenson's Week 1
volume floor rises because the alternatives are a five-practice acquisition and a practice-squad
elevation, but his route, two-minute, and goal-line shares are unmeasured and no numerical
projection is asserted here. Kiner is a name-only depth note, not a start candidate.

## Conflicts and uncertainty

- Injury site: Callahan's September 6 daily post (superseded, not rowed) called Henderson's injury a
  knee; the official report, Reiss, Kyed, and Callahan's own September 7 post all say ankle. The
  reader treated the knee reference as a typo; the official designation controls. No conclusion
  depends on the distinction because the status is OUT either way.
- Depth numbering: the team site calls Kiner the "No. 2 on the active roster" while Kyed calls him
  the "third back". Kyed's later elevation report places Larison behind Stevenson and Kiner, so the
  difference is whether the injured Henderson is counted; it is not a contradiction about who
  plays second.
- Brown's position: the roster page lists him at center while both the team-site analysis and Kyed
  describe him as an interior backup. The starting-center identity is not stated in any rowed item;
  "starting five intact" comes from a single team-produced analysis.
- Gonzalez: terms are reported, not officially announced in a retrieved item; the fully guaranteed
  figure is unreported.
- Reader overflow: at cap the reader did not row the September 7 Vrabel transcript (Henderson to be
  assessed; Barmore to practice; praise for Stevenson's protection) or the team-site "Report:"
  Gonzalez item. Both are superseded or duplicative; the Stevenson protection praise is a coach
  statement that would only add a third interpretive voice to cluster 8, not measurement.
- Unmeasured: actual carries, routes, targets, two-minute snaps, and goal-line work for Stevenson,
  Kiner, and Larison; Henderson's timeline beyond Week 1; the actual starting center. Postgame
  gamebook, snap, and route data would resolve the first; Week 2 practice reports the second.
- Everything here is pre-kickoff. Nothing in this synthesis is postgame evidence.

## Excluded noise

- `obs-2026-ne-20260909t210706z-008` as corroboration: Reiss restates the official designation and
  depth order; counted once as provenance, not as an independent origin.
- `obs-2026-ne-20260909t210706z-010` as corroboration: Kyed restates the official elevation; its
  spelling and release-date discrepancies are immaterial.
- The pass-protection "only trusted back" judgment in `obs-2026-ne-20260909t210706z-011`: columnist
  interpretation without rep or usage evidence; kept as context, not routed as role evidence.
- Unrowed and superseded items from the run report: Vrabel's September 7 assessment plans, Callahan's
  September 6 and 7 daily injury posts, the team-site "Report:" Gonzalez item, the Pats Chat episode
  metadata, and an unregistered-byline Herald notebook. None adds a claim beyond the rowed clusters.
- Roster-page position labels and practice photographs do not establish a starting center or a
  measured role.

## Run metrics

- Raw observations: 12
- Unique evidence clusters: 9
- Repeats removed: 2 (`-008`, `-010`)
- Independent confirmations: 1 (`-009` confirming `-007`); no cluster has more than two origins
- Updates to prior observations: 1 (`-001` updating `obs-2026-ne-20260906t193157z-002` and
  `obs-2026-ne-20260906t210715z-001`)
- Contradictions rowed: 0 (one unrowed knee/ankle discrepancy noted above)
- False positives excluded from routing: 3 rowed items (`-008`, `-010`, the analysis half of
  `-011`) plus the unrowed overflow
- Routing: 1 escalate, 1 review, 5 log
- Prior ledger triggers: `til-2026-ne-20260906-001` and `-002` (already resolved) named the
  Henderson final designation as the next check; that trigger occurred (`-001`). The second half of
  `-002`'s trigger, "actual passing-down allocation", has not occurred. Board rows
  `sig-2026-ne-20260906-001` and `-002` can move from `monitoring` once ARCHITECT records this run.
- Synthesis elapsed time: about 20 minutes from assignment receipt to file write.
- Reader coverage: [`run-report.csv`](../../runs/20260909T210706Z/reader-ne/run-report.csv).

## Sources

- [local-source-new-england-patriots](https://www.patriots.com/news/week-1-injury-report-patriots-at-seahawks) — published 2026-09-08T20:50:00Z; retrieved 2026-09-09T21:08:56Z; `obs-2026-ne-20260909t210706z-001`, `-002`, `-003`.
- [local-source-new-england-patriots](https://www.patriots.com/news/patriots-elevate-two-players-from-the-practice-squad-x2562) — published 2026-09-09T20:00:00Z; retrieved 2026-09-09T21:08:56Z; `obs-2026-ne-20260909t210706z-004`, `-005`.
- [local-source-new-england-patriots](https://www.patriots.com/news/injury-report-analysis-patriots-rb-treveyon-henderson-ankle-ruled-out-for-season-opener-vs-seahawks) — published 2026-09-08T20:51:56Z; retrieved 2026-09-09T21:08:56Z; `obs-2026-ne-20260909t210706z-006`, `-007`.
- [local-writer-mike-reiss](https://www.espn.com/nfl/story/_/id/49872328/patriots-henderson-seahawks-okada-ruled-sb-rematch) — published 2026-09-08T21:12:36Z; retrieved 2026-09-09T21:09:41Z; `obs-2026-ne-20260909t210706z-008`.
- [local-writer-doug-kyed](https://www.bostonherald.com/2026/09/08/patriots-get-bad-news-in-final-injury-report-before-season-opener-vs-seahawks/) — published 2026-09-08T21:10:47Z; retrieved 2026-09-09T21:09:36Z; `obs-2026-ne-20260909t210706z-009`.
- [local-writer-doug-kyed](https://www.bostonherald.com/2026/09/09/patriots-add-two-including-running-back-to-play-vs-seahawks-in-week-1/) — published 2026-09-09T20:14:54Z; retrieved 2026-09-09T21:09:37Z; `obs-2026-ne-20260909t210706z-010`.
- [local-writer-andrew-callahan](https://www.bostonherald.com/2026/09/07/callahan-why-rhamondre-stevenson-is-the-patriots-key-at-seattle-and-more-week-1-thoughts/) — published 2026-09-07T09:00:44Z; retrieved 2026-09-09T21:09:38Z; `obs-2026-ne-20260909t210706z-011`.
- [local-writer-doug-kyed](https://www.bostonherald.com/2026/09/08/patriots-christian-gonzalez-agree-to-four-year-extension-ahead-of-deadline/) — published 2026-09-08T05:02:21Z; retrieved 2026-09-09T21:09:38Z; `obs-2026-ne-20260909t210706z-012`.
