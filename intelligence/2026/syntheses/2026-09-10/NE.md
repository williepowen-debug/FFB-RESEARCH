---
schema_version: 1
record_id: "ti-2026-ne-20260910-001"
record_type: "team_intelligence"
title: "New England Patriots intelligence synthesis — 2026-09-10"
team_ids: ["NE"]
player_ids: []
season: 2026
week: 1
status: "active"
time_horizon: "weekly"
valid_as_of: "2026-09-10"
last_verified: "2026-09-10"
confidence: "high"
source_ids: ["local-source-nfl-gamebooks", "local-source-new-england-patriots", "local-writer-doug-kyed", "local-writer-andrew-callahan", "local-writer-evan-lazar", "local-writer-phil-perry"]
supersedes: []
observation_ids: ["obs-2026-ne-20260910t222845z-001", "obs-2026-ne-20260910t222845z-002", "obs-2026-ne-20260910t222845z-003", "obs-2026-ne-20260910t222845z-004", "obs-2026-ne-20260910t222845z-005", "obs-2026-ne-20260910t222845z-006", "obs-2026-ne-20260910t222845z-007", "obs-2026-ne-20260910t222845z-008", "obs-2026-ne-20260910t222845z-009", "obs-2026-ne-20260910t222845z-010", "obs-2026-ne-20260910t222845z-011", "obs-2026-ne-20260910t222845z-012", "obs-2026-ne-20260910t222845z-013", "obs-2026-ne-20260910t222845z-101", "obs-2026-ne-20260910t222845z-102", "obs-2026-ne-20260910t222845z-103", "obs-2026-ne-20260910t222845z-104", "obs-2026-ne-20260910t222845z-105", "obs-2026-ne-20260910t222845z-106", "obs-2026-ne-20260910t222845z-107", "obs-2026-ne-20260910t222845z-108", "obs-2026-ne-20260910t222845z-109"]
run_ids: ["20260910T222845Z"]
---

# New England Patriots intelligence synthesis — 2026-09-10

Postgame completion snapshot for the Week 1 opener at Seattle (Seattle 13, New England 10). The
official book is published and measured usage exists for the first time this season. This synthesis
supplements, and does not supersede, the pre-kickoff [September 9 snapshot](../2026-09-09/NE.md);
that record's designations remain the state of the world going into the game, and this one records
what the game actually measured.

## Executive signal

A.J. Brown was injured on a third-and-4 incompletion at 13:30 of the third quarter, was declared Out
of the game at the start of the fourth, and Mike Vrabel said on September 10 that Brown faces
further testing, that an update comes next week, and that he does not know whether Brown will be
available for the next game. That is the one material, time-sensitive change. The widely carried
high-ankle-sprain diagnosis is **not** an official fact: it traces to a single unregistered origin,
Vrabel was asked directly and would not confirm it, and no assigned source sourced it independently.

Everything else is measurement. Rhamondre Stevenson was a bell-cow by snap share (60 of 71, 85%),
took 18 of 31 team carries and 6 of 31 targets, and was on the field for all 11 two-minute snaps in
both halves — but on 2.8 yards per carry behind a line that Lazar and Kyed both graded poorly.
Corey Kiner played 8 snaps and Lan Larison 3 with zero carries, so the Henderson-absent depth chart
compressed rather than distributed. Drake Maye threw three interceptions on a 54.9 rating against a
film-charted 38.1% pressure rate. Romeo Doubs played 40 snaps, fewer than both Mack Hollins and
DeMario Douglas, and caught none of his three targets. **None of this tests the healthy
Stevenson–Henderson timeshare, and none of it may count toward `ne-2026-off-q07`'s first-two-games
trigger:** TreVeyon Henderson was an official Week 1 inactive.

## Reconciled evidence

Twenty-two rows collapse into nineteen `dedup_key` clusters drawn from **seven originating sources**
— six registered (the NFL gamebook, patriots.com communications, Kyed, Callahan, Lazar, Perry) and
one unregistered (NFL Network). Read the atomic claims in the
[official batch](../../runs/20260910T222845Z/reader-ne-official/observations.csv) and the
[beat batch](../../runs/20260910T222845Z/reader-ne-beat/observations.csv), and the coverage record in
the [official run report](../../runs/20260910T222845Z/reader-ne-official/run-report.csv) and the
[beat run report](../../runs/20260910T222845Z/reader-ne-beat/run-report.csv).

### 1. A.J. Brown's injury — three rows, one official event, one unregistered diagnosis

`ne-2026-w01-ajbrown-injury` carries `obs-...-009`, `-010` and `-101`. They are not three
confirmations; they are two official items and one relay, and the boundary between them is the most
important separation in this synthesis.

- **Official fact** (`-009`, gamebook play-by-play): Brown was injured on the play at 13:30 of Q3,
  his return was listed Questionable at 12:41 of Q3, and he was declared Out of the game at the start
  of Q4. **The book records no injury type.**
- **Official fact** (`-010`, patriots.com Vrabel transcript, `update` on `-009`): further testing,
  an update next week, no knowledge of availability for the next game, and — asked directly about a
  reported high ankle sprain — **no confirmation of a diagnosis**.
- **Reported fact from an unregistered origin** (`-101`, Kyed, `update`): high ankle sprain, MRI
  Thursday. Kyed attributes this to "multiple reports," not his own sourcing. The origin is an NFL
  Network report by Rapoport and Garafolo that the reader could not retrieve; the earliest retrievable
  carrier is an ESPN story bylined **"Multiple Authors," not Mike Reiss**, whose lede credits NFL
  Network. Phil Perry relays the same origin ("what's been reported as") and was deliberately not
  rowed. **One origin, three carriers, zero independent corroboration.**

Independent-origin count on the diagnosis: **one, and it is unregistered.** Independent-origin count
on the fact that Brown left the game and did not return: **two official items.** No assigned source
reported an expected absence specific to Brown; Kyed's "3-to-6 weeks" is a general expectation for
the injury class and the ESPN relay's "2-to-6" is the same, neither is a reported timeline for Brown.

### 2. Measured usage — one official origin, one independent measurement check

`obs-...-001` through `-008` and `-013` all come from the single NFL gamebook. They are nine distinct
atomic claims but **one origin**, and they must not be counted as nine supporting observations.
Observations `-001` (Stevenson rushing) and `-006` (target distribution) were independently
re-derived by the reader from the ESPN box score for game `401872656` and matched exactly; that page
carries no byline, so it is a measurement check, not a second registered source. `-012` (inactives)
was likewise cross-confirmed against the gamebook's page 1 "Not Active" block.

Final measured offense, reconciled by ARCHITECT into
[`usage-input.csv`](../../../../weekly/2026/week-01/usage-input.csv):

| Player | Snaps (of 71) | Carries (of 31) | Targets (of 31) | Rec | Yds |
|---|---:|---:|---:|---:|---:|
| Rhamondre Stevenson | 60 (85%) | 18 | 6 | 5 | 44 |
| Hunter Henry | 54 (76%) | — | 3 | 3 | 26 |
| Mack Hollins | 50 (70%) | — | 5 | 4 | **51** |
| DeMario Douglas | 44 (62%) | — | **7** | 5 | 20 |
| Romeo Doubs | 40 (56%) | — | 3 | **0** | 0 |
| Eli Raridon | 38 (54%) | — | 1 | 1 | 2 (TD) |
| A.J. Brown | 31 (44%) *partial* | — | 4 | 3 | 26 |
| Corey Kiner | 8 (11%) | 6 | 0 | 0 | 0 |
| Lan Larison | 3 (4%) | **0** | 2 | 2 | 9 |
| Drake Maye | 71 (100%) | 7 | — | — | — |

**Targets restricted to the window Brown was on the field** (reconciled by ARCHITECT from the
official play-by-play behind `-006` and `-009`; 13 targets thrown before his exit at Q3 13:30):
Brown 4, Douglas 3, Henry 2, Stevenson 1, Hollins 1, Larison 1, Raridon 1, **Doubs 0**. Brown led at
roughly a 31% share. Brown shows five raw play-by-play mentions; the fifth is the Q2 9:22 deep
incompletion nullified by Jobe's DPI, which is correctly not a statistical target — that reconciles
the play-by-play to his official 4 and is an independent check on the negated-snap model in item 3
below. The 13 in-window targets plus 18 after his exit recover the official 31.

### 3. Denominators — a reconciliation, not a source conflict

`obs-...-005` and `-013` settle the arithmetic and remove what an earlier reader pass had mistaken
for a reliability problem. New England took **71 actual offensive snaps** = 67 statistical offensive
plays (33 pass attempts + 31 rushes + 3 sacks) + 4 snapped plays negated by live-ball penalty (Jobe
DPI, Campbell illegal block, Campbell holding, Vera-Tucker ineligible downfield). Both bases are
valid: **71 for snap share, 67 for per-play rates.** The same method applied to Seattle yields
exactly 2 nullified snaps and matches its 50-vs-48 gap, so the reconciliation holds independently on
both sides of the same book.

Two consequences that must not be lost:

- **Team targets are 31, not 33.** Two Maye attempts had no intended receiver. Every target share in
  this synthesis is on the 31 base.
- **Lazar's 57-of-67 and 60-of-71 Stevenson figures are consistent, not contradictory.** Three of the
  four nullified snaps had Stevenson on the field, so 57 + 3 = 60. The beat reader's earlier framing
  of this as a self-conflict was withdrawn in the run report and is withdrawn here. Mixing the bases
  is the error, not the source. Correspondingly, Stevenson's share on the 67-play base is bounded at
  83.6–86.6% and **is not 60/67 = 90%**; the book exposes no per-player participation on nullified
  snaps.

### 4. Two null results that are findings in themselves

- **Inside the 5: n = 1.** New England ran exactly one snap inside the Seattle 5 all game, the
  2-yard touchdown pass to Raridon. Stevenson's zero inside-5 carries therefore resolve **nothing**
  about the goal-line role for any back. This is a null result, not evidence against him.
- **Two-minute: 11 of 11.** Stevenson was on the field for all eleven offensive snaps inside 2:00 of
  either half and took touches in each (a 5-yard reception and a 2-yard carry in Q2, an 8-yard carry
  in Q4). Kiner and Larison took zero Q2 two-minute snaps; Larison had one Q4 target. This is the
  one backfield sub-role the game *did* measure cleanly.

### 5. Receiver deployment — one measured distribution, four interpretive origins

The distribution itself is official (`-006`, `-008`). Four separate origins offer explanations of it,
and each is interpretation layered on that one measurement, not additional measurement:

- **Kyed** (`-105`, `analysis`): Hollins played more than expected and was used heavily as a run
  blocker, which Kyed reads as the reason Doubs and Douglas saw fewer **first-half** snaps. This
  predates Brown's Q3 injury and is a materially different mechanism from cluster item 3 below.
- **Callahan** (`-106`, `analysis`): once Brown left, Maye came off most receivers except Hollins,
  naming Hollins the replacement primary read on the fourth-down conversion and on the final end-zone
  interception, and noting all three interceptions came after Brown's exit.
- **Lazar** (`-103`, `analysis`, team-employed): projects a large Hollins role *if* Brown misses
  time, citing two Q4 conversions (a 19-yard dig on second-and-21, an 11-yard slant on fourth-and-9).
  This is a forward projection conditional on an absence no assigned source has had confirmed.
- **Perry** (`-104`, `analysis`): calls Doubs's usage curious — fewer snaps than both Hollins and
  Douglas despite repping as a starting receiver alongside Brown all training camp — and questions
  how the staff views his fit. Perry's training-camp starter observation is reported fact; the fit
  question is interpretation. He adds that Doubs said postgame he was not locked in, and that a Doubs
  drop preceded Maye's second interception.

**Source concentration warning.** Lazar is team-employed and carries three of the nine beat rows
(`-103`, `-107`, `-108`). Under the registry a team-employed source never carries a role conclusion
alone, and three of the four interpretive origins above are Boston Herald (Kyed, Callahan) or
Patriots.com (Lazar). Only Kyed's `-109` is an organizationally independent check on Lazar's line
charting.

### 6. Pass protection — the batch's one genuine independent confirmation

`ne-2026-w01-pass-protection` carries `-108` (Lazar, film charting: 38.1% pressure rate, four hurries
charged to LG Alijah Vera-Tucker, a sack to Campbell, a QB hit to Stevenson, a hurry to Wilson,
Maye charged with a sack/hit/hurry of his own, Moses charted clean) and `-109` (Kyed, independently
assessing Vera-Tucker as the line's weak link in his New England debut, allowing multiple hurries,
and flagged for ineligible man downfield). Same conclusion, different outlet, different viewing,
different `origin_url`: **two supporting observations, not one recirculated claim.** This is the only
cluster in the batch with genuine organizationally independent corroboration.

Kyed's ineligible-man-downfield observation is one of the four penalty-negated snaps in `-013`, so
his read is consistent with the official record at the play level.

**Reliability signal, isolated:** Lazar re-measured the *same* metric on the *same* base from 28.6%
"on initial viewing" to 38.1% on film. That is a real self-revision and it lowers confidence in the
precise figure while leaving the direction corroborated by Kyed. It is kept strictly separate from
the Stevenson snap figures in item 3, which are not a revision at all.

### 7. Kind separation

Official facts: `-005` through `-009`, `-011`, `-012`, `-013`, and the measured lines in `-001`
through `-004`, `-006`. Reported fact from an unregistered origin: the diagnosis half of `-101`.
Reported fact from a registered origin: Kyed's receiver-room roster list in `-102` and Perry's
training-camp starter observation inside `-104`. Firsthand observation: the play descriptions inside
`-103`, `-106`, `-107` and `-109`. Analysis: everything else, including every causal explanation of
the measured distribution and every forward projection.

## Hypothesis impact

Baseline read:
[offense hypotheses](../../../../teams/AFC/East/New-England-Patriots/2026/offense/hypotheses.csv),
[receiving hierarchy finding](../../../../teams/AFC/East/New-England-Patriots/2026/offense/receiving-hierarchy.md),
[backfield timeshare finding](../../../../teams/AFC/East/New-England-Patriots/2026/offense/backfield-timeshare.md),
the [September 9 synthesis](../2026-09-09/NE.md),
[`wm-2026-w01-ne-sea-001`](../../../../weekly/2026/week-01/games/NE-at-SEA.md), and the reconciled
[Week 1 usage rows](../../../../weekly/2026/week-01/usage-input.csv).

- **`ne-2026-off-q01` (Brown as defined alpha WR1 and clear target leader): partial CONFIRMING
  evidence on an availability-limited sample.** *(Disposition corrected by ARCHITECT ruling,
  2026-09-10; this synthesis originally recorded the hypothesis as untestable. The correction is
  recorded here rather than silently applied.)* Restricted to the snaps Brown was actually on the
  field for, **he led the team in targets: 4 of the 13 thrown before his exit, roughly a 31% share**
  (Douglas 3, Henry 2, Stevenson, Hollins, Larison and Raridon 1 each, **Doubs 0**). That is a real
  if truncated sample, and it points the same way the hypothesis does. The asymmetry with q07 is the
  whole point: Henderson played zero snaps and nothing can be computed, whereas Brown played 31 and
  a restricted denominator is available. The full-game ordering that shows Brown fourth in targets
  behind Douglas, Stevenson and Hollins is an **artefact of his absence for the final 24 minutes**
  and must never be cited against q01 without that caveat. What the game cannot do is *complete* the
  test: a 44%-snap game is not a full-game test of a target-leader hypothesis, so **Week 1 does not
  count toward q01's two-game trigger.** His while-available snap share remains bounded below at 44%
  and is not exactly derivable, but his while-available *target* share is.
- **`ne-2026-off-q02` (targets concentrate around Brown rather than spreading): weakly challenged,
  contextual.** The measured distribution was flat — seven pass catchers with between 1 and 7 targets
  and a team high of 7 — but it is one Brown-partial game against a four-game review trigger. Nothing
  promotes.
- **`ne-2026-off-q04` (Doubs a stable complementary starter): materially challenged, n = 1.** This is
  the sharpest measured challenge in the batch. Doubs played 40 snaps, **behind Hollins (50) and
  Douglas (44)**, and caught **zero** of three targets; Callahan reports he saw no target until the
  fourth quarter, which the play-by-play confirms — **Doubs was the only pass catcher with zero
  targets over the window Brown was on the field**, while Brown led it. The hypothesis's named disconfirming condition is losing outside snaps to a younger
  receiver — the receiver who passed him is Hollins, a veteran, and Kyed's first-half run-blocking
  explanation (`-105`) offers a scheme reason that is not a demotion. Both readings survive one game.
  Trigger is first two regular-season games; this is game one.
- **`ne-2026-off-q05` (Henry retains a steady middle-field and red-zone tight-end role): mixed.**
  Henry led all pass catchers in snap share at 76% (the confirming branch, using snaps as a route
  proxy — actual route data does not exist for this game) but drew only 3 targets. Rookie Eli Raridon
  played 38 snaps (54%), caught the only touchdown, and was the target on the **only** snap New
  England ran inside the Seattle 5 — which is the hypothesis's named disconfirming condition, on a
  sample of one snap. Henry also left the game and returned (`-011`). Trigger is first two games;
  this is game one.
- **`ne-2026-off-q06` (Stevenson lead early-down and short-yardage back): descriptively supported,
  but this sample cannot supply confirming or disconfirming evidence.** Stevenson took 18 of 31 team
  carries, 85% of snaps and all 11 two-minute snaps. **Henderson was an official Week 1 inactive
  (`-012`), so the hypothesis's disconfirming branch — "Henderson takes a three-down role; committee
  by series" — was structurally untestable.** The short-yardage half is unresolved for the separate
  reason that only one inside-5 snap existed.
- **`ne-2026-off-q07` (Henderson wins the passing-down and explosive-play role): no evidence, and
  this game must not count toward the trigger.** Henderson did not play. Per the hypothesis row as
  amended on 2026-09-09, the "first two regular-season games" trigger runs from Henderson's
  availability; **Week 1 is not one of the two.** What the game does supply is a Henderson-absent
  baseline for the role he is hypothesised to win: Stevenson took 6 of 31 targets and all 11
  two-minute snaps, Larison's 3 snaps produced 2 targets and 0 carries, and Kiner's 6 carries were
  all first- or second-down with five of six in Q2 and no targets at all. Kiner is an early-down-only
  usage pattern in this sample; Larison is a passing-situation-only one.
- **`ne-2026-off-q08` (Maye takes another step): challenged, game one of four.** 23 of 33 for 178
  gross yards, 1 touchdown, **3 interceptions**, 3 sacks, a 54.9 rating, and 7 carries for 47 yards,
  in a 13-10 loss with 5-of-16 on third down. The hypothesis's named disconfirming condition is
  "pressure or turnover issues" and both appeared. Two mitigating facts are on the record and neither
  is decisive: Lazar charts the pressure rate at 38.1% and assigns most of it to blockers rather than
  to Maye, and Callahan notes all three interceptions came after Brown left. Trigger is first four
  games.
- **`ne-2026-off-q09` (interior line and tackle spot stabilize): mixed, with the batch's only
  independent corroboration on the negative side.** Confirming: the starting five each played all 71
  snaps (`-008`) — the "stable first-unit five" branch held exactly, and Ben Brown's absence removed
  no starter. Disconfirming: "rising pressure" is the named condition and a 38.1% charted pressure
  rate with two independent origins converging on Vera-Tucker is real evidence for it. Trigger is
  first two games with protection charting; this is game one, and the charting is beat charting
  rather than measured data.
- **`rf-2026-ne-backfield-timeshare-001`: partially triggered, no change to the finding.** Its stated
  next review was Week 1 usage charting. The absolute-usage half is now measured (snap share, carry
  share, target share, two-minute involvement). The route-participation half **could not be
  collected** — the gamebook exposes playtime percentages only, no route or target-share
  participation, and no other route source was assigned. The healthy Stevenson–Henderson split
  remains untestable until Henderson returns, exactly as the finding says.
- **`rf-2026-ne-receiving-hierarchy-001`: one stated fact is now stale.** Its Week 1 status paragraph
  records that "the receiver and tight-end room therefore opens the season intact." That ceased to be
  true at 13:30 of Q3. Its role table entry for Doubs ("starting complementary receiver") and for
  Brown ("clear target leader") both now have one game of contrary measurement against them, in
  Brown's case from a partial game that cannot bear the weight.
- **`wm-2026-w01-ne-sea-001`: changes.** The game is complete; the record should carry the final
  score, the measured usage now in `usage-input.csv`, Brown's in-game injury and non-return, and the
  fact that its Stevenson/Kiner measurement question is answered for absolute usage and unanswered
  for routes.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| escalate | A.J. Brown was injured at 13:30 of Q3, declared Out of the game at the start of Q4, faces further testing, and Vrabel does not know whether he is available for Week 2. The high-ankle-sprain diagnosis is a single unregistered origin that Vrabel declined to confirm and is **not** an official fact. | `obs-2026-ne-20260910t222845z-009`; `obs-2026-ne-20260910t222845z-010`; `obs-2026-ne-20260910t222845z-101` | Promote the official in-game injury record and Vrabel's September 10 statement to `wm-2026-w01-ne-sea-001` and open a Week 2 availability row. Treat Brown as unresolved, not out: record the diagnosis as reported-only with its unregistered origin named. Next check is the first Week 2 practice report and the official Week 2 injury report; a registered source independently sourcing the diagnosis, or a team designation, would upgrade it. |
| review | Brown led the team in targets **while he was on the field** — 4 of the 13 thrown before his exit, about 31% — so Week 1 supplies partial evidence **consistent with** the alpha-WR1 hypothesis on an availability-limited sample. The full-game order (Douglas 7, Stevenson 6, Hollins 5, Brown 4) and Hollins's team-high 51 yards are artefacts of the final 24 minutes without him and must not be cited against q01 uncaveated. The sample cannot *complete* the two-game trigger. | `obs-2026-ne-20260910t222845z-006`; `obs-2026-ne-20260910t222845z-008`; `obs-2026-ne-20260910t222845z-102`; `obs-2026-ne-20260910t222845z-103`; `obs-2026-ne-20260910t222845z-106` | Record a deferred disposition against `ne-2026-off-q01` capturing the in-sample target lead as evidence (not "no evidence"), and against `ne-2026-off-q02`. Add an explicit partial-game sample limit to `rf-2026-ne-receiving-hierarchy-001`, whose "room opens intact" line is now stale. Do not count Week 1 toward q01's two-game trigger — a 44%-snap game cannot complete a target-leader test. Next trigger: the first game Brown plays start to finish, or a Week 2 target distribution measured with him confirmed out. |
| review | Romeo Doubs played 40 snaps — behind Hollins (50) and Douglas (44) — and caught none of his three targets, with no target until Q4; Perry questions the staff's view of his fit and Kyed offers a first-half run-blocking explanation that is not a demotion. | `obs-2026-ne-20260910t222845z-006`; `obs-2026-ne-20260910t222845z-008`; `obs-2026-ne-20260910t222845z-104`; `obs-2026-ne-20260910t222845z-105` | Record a deferred disposition against `ne-2026-off-q04`. One game with a scheme-based competing explanation is below the promotion bar. Next trigger is Week 2 snap and target share with Brown's status known, which is the game that separates "Doubs is being passed" from "Doubs lost first-half snaps to a run-blocking package." |
| review | Measured Henderson-absent backfield usage: Stevenson 60/71 snaps, 18/31 carries, 6/31 targets and 11 of 11 two-minute snaps; Kiner 8 snaps, 6 early-down carries, 0 targets; Larison 3 snaps, 0 carries, 2 targets. Inside-5 is a null result at n=1 and route participation could not be collected. | `obs-2026-ne-20260910t222845z-001`; `obs-2026-ne-20260910t222845z-002`; `obs-2026-ne-20260910t222845z-003`; `obs-2026-ne-20260910t222845z-006`; `obs-2026-ne-20260910t222845z-008`; `obs-2026-ne-20260910t222845z-012` | Close the measurement half of `til-2026-ne-20260909-002` and `-003` against the reconciled `usage-input.csv` rows; keep both **open** on the untriggered half. Promote the absolute Week 1 usage as descriptive Henderson-absent data only. `ne-2026-off-q06` and `ne-2026-off-q07` stay unchanged and Week 1 must not count toward q07's first-two-games trigger. Next trigger: Henderson's Week 2 practice participation, plus a route-participation source if one can be registered. |
| review | Drake Maye threw 3 interceptions on a 54.9 rating with 3 sacks taken and a 5-of-16 third-down day, against a film-charted 38.1% pressure rate; all three interceptions came after Brown's exit. | `obs-2026-ne-20260910t222845z-007`; `obs-2026-ne-20260910t222845z-005`; `obs-2026-ne-20260910t222845z-108`; `obs-2026-ne-20260910t222845z-106` | Record a deferred disposition against `ne-2026-off-q08`. The turnover-and-pressure disconfirming branch appeared in game one of a four-game trigger; do not revise the hypothesis on one game, and do not let the supporting-cast confound (Brown's exit) become an excuse that is never retested. Next trigger: Weeks 2–4 turnover and pressure rates. |
| review | Pass protection: Lazar charts a 38.1% pressure rate with four hurries on LG Alijah Vera-Tucker; Kyed independently reaches the same Vera-Tucker conclusion from a separate outlet and viewing. The starting five nonetheless played all 71 snaps. | `obs-2026-ne-20260910t222845z-108`; `obs-2026-ne-20260910t222845z-109`; `obs-2026-ne-20260910t222845z-008` | Record a deferred disposition against `ne-2026-off-q09` capturing both branches: the stable-five condition is confirmed by official participation, the rising-pressure condition is supported by two independent charting origins. Note Lazar's 28.6%→38.1% self-revision as a confidence limit on the exact figure. Next trigger: Week 2 protection charting, which completes the two-game trigger. |
| review | Hunter Henry led pass catchers in snap share (54, 76%) but drew 3 targets, while rookie Eli Raridon played 38 snaps (54%), caught the only touchdown, and was the target on the only snap New England ran inside the Seattle 5. | `obs-2026-ne-20260910t222845z-006`; `obs-2026-ne-20260910t222845z-008`; `obs-2026-ne-20260910t222845z-011` | Record a deferred disposition against `ne-2026-off-q05`. Raridon's snap share is real two-tight-end usage; his goal-line touchdown is n=1 and settles nothing. Next trigger: Week 2 tight-end snap and target split, which completes the two-game trigger. |
| log | Week 1 inactives (Prunty, Henderson, Hunter, Rouse, Ben Brown, Chism, Morton as emergency QB) — already promoted from the September 9 run; retained here because they are the official basis for every sample limit in this synthesis. | `obs-2026-ne-20260910t222845z-012` | None. Cite as the sample-limit authority; do not re-promote. |
| log | Moses, Henry and Carlton Davis III each left the Seattle game and returned; Vrabel does not believe any injury beyond Brown's will keep a player out. | `obs-2026-ne-20260910t222845z-011` | None. This is a coach's characterisation, not a designation — Vrabel explicitly declined to give an injury report. Confirm against the official Week 2 injury report before treating any of the three as healthy. |
| log | Snap-denominator reconciliation: 71 actual offensive snaps = 67 statistical plays + 4 penalty-negated snaps; team targets are 31, not 33; Stevenson's share on the 67 base is bounded 83.6–86.6% and is not 90%. | `obs-2026-ne-20260910t222845z-005`; `obs-2026-ne-20260910t222845z-013` | None as a role signal. Carry the 71/67 split as the standing denominator convention for every Week 1 usage row and every future gamebook pass; it is method, not evidence about a player. |
| log | Conflict retained: Lazar's charting credits Stevenson with 50 of his 51 rushing yards after contact and assigns the failure to blocking; Kyed's independent read says the line was ineffective **and** that Stevenson was not creating on his own. | `obs-2026-ne-20260910t222845z-107`; `obs-2026-ne-20260910t222845z-109` | None. Preserve both readings and lower confidence in any efficiency conclusion about Stevenson from this game. Kyed's competing read was not rowed separately because of the observation cap; row it if the question becomes decision-relevant. |
| log | Repository coverage gap: Mack Hollins, Eli Raridon and Lan Larison have no canonical `players/` profiles, yet between them they took 91 offensive snaps and produced the team lead in receiving yards and the only touchdown. | `obs-2026-ne-20260910t222845z-003`; `obs-2026-ne-20260910t222845z-006`; `obs-2026-ne-20260910t222845z-008` | None from this synthesis. Flagged to ARCHITECT: three unresolved `player_ids` fields in this batch trace to missing profiles, and Hollins is now a live weekly name. |
| log | The relayed A.J. Brown diagnosis retained as provenance only. | `obs-2026-ne-20260910t222845z-101` | None. Counted once as a carrier of one unregistered origin, never as corroboration of the injury record in `-009` or of the coach's statement in `-010`. |

Fantasy implication for the escalated signal: A.J. Brown is a Week 2 unknown, not a Week 2 out —
the only official statements are that he did not return and that the head coach does not know. No
absence length is asserted here because no registered source reported one. If Brown misses time, the
measured Week 1 distribution says the targets in front of him were already going to Douglas (7) and
Stevenson (6) and the yards to Hollins (51), and three separate origins expect Hollins to absorb the
outside role — but that expectation is interpretation from a 27-minute sample and no numerical
projection follows from it. Doubs is the name whose Week 1 measurement and Week 2 opportunity point
in opposite directions and is the roster decision most likely to be got wrong this week.

## Conflicts and uncertainty

- **The diagnosis.** Brown's high ankle sprain is reported by one unregistered origin (NFL Network),
  carried by an unbylined ESPN story and relayed by two registered sources without independent
  sourcing, and Vrabel would not confirm it when asked directly. It is possible the diagnosis is
  correct and simply not yet officially acknowledged; it is equally possible it is premature. What
  resolves it: the official Week 2 injury report, or a registered source sourcing it independently.
- **Brown's true role rate — partly resolved.** His while-available *target* share is derivable
  from the play-by-play and he led the team on it (4 of 13, ~31%). His while-available *snap* share
  is not: all 31 snaps came before 13:30 of Q3 and the book exposes no snap-by-snap timeline, so it
  is bounded below at 44% and not otherwise derivable. No full-game projection follows from either.
- **Route participation does not exist for this game.** The gamebook exposes an "Unofficial"
  playtime-percentage table and no route or target-share participation, and the NFL game center
  exposed no separate participation report. This is the single largest measurement gap in the run and
  it is what keeps both open backfield ledger rows from closing completely.
- **Stevenson's efficiency.** Lazar (team-employed, own charting) and Kyed (independent) disagree on
  whether 2.8 yards per carry was the line or the back. Unresolved; a second independent charting
  source or Week 2 rushing data resolves it.
- **Lazar's pressure figure.** The same metric on the same base moved 28.6% → 38.1% between his two
  same-window pieces. Take 38.1% as his settled film figure, but treat the precision as soft. The
  direction is independently corroborated by Kyed; the magnitude is not.
- **Source concentration.** Nine beat rows come from four registered writers, three of them from one
  team-employed analyst, and two of the remaining three writers share an outlet. Kyed's `-109` is the
  only organizationally independent check on Lazar's line charting in the entire batch.
- **Uncollected material overflow that a future run should capture.** Reiss firsthand-observed Brown
  in a protective boot in the locker room and described the mechanism as Pritchett's knee landing on
  the right ankle; Callahan has multiple players saying the final interception was a designed quick
  passing concept; Lazar has 16 first-down runs at a 24% early-down rushing success rate and Seattle
  in zone on 88.1% of Maye's 42 drop-backs; Perry has the running backs at 2.6 yards per carry and 16
  first-down runs for 49 yards. **None of these are rowed, so none is evidence here.** The Reiss boot
  observation is the one worth rowing next run — it would be the first firsthand severity evidence on
  Brown from a registered source, independent of the NFL Network origin.
- **Not measured at all:** routes, alignment, red-zone target share beyond the single goal-line snap,
  Henderson's timeline, and whether Kiner's early-down-only and Larison's passing-down-only patterns
  are role assignments or the residue of a game script that never reached garbage time.

## Excluded noise

- **The `3-to-6 weeks` and `2-to-6 weeks` figures.** Kyed's is a general expectation for the injury
  class and the ESPN relay's is the same; neither is a reported timeline for Brown. Excluded from
  routing entirely — carrying them would manufacture an absence length no source reported.
- **Perry's relay of the sprain diagnosis.** Deliberately not rowed by the reader: one origin, one
  cluster. Correct call, retained as an exclusion rather than a coverage gap.
- **Kyed's Boutte counterfactual** in `-102` — that a traded player might have stepped into a
  starting role had he still been rostered. Speculation about a player with no New England role;
  `ne-2026-off-q03` is resolved. Not routed.
- **Lazar's forward projection** in `-103` that Hollins "could be in for a large role." The two Q4
  conversions he cites are firsthand film observation and are kept as context inside the receiver
  review; the projection itself is a team-employed forward look conditional on an unconfirmed
  absence, and is not routed as role evidence.
- **Callahan's "Brown led the Patriots in receptions, targets and receiving yards."** *(Reframed by
  ARCHITECT ruling, 2026-09-10; this synthesis originally excluded it as a resolved contradiction.)*
  Not a false positive and **not** contradicted: it was **accurate at Brown's exit**, and the
  play-by-play confirms why — Brown led in targets over the window he played. It is a scope
  difference, not an error, and it must be carried with the "at his exit" caveat rather than
  discarded or repeated bare. What is wrong is only the unqualified present-tense reading against
  the official final line in `-006`. Note his separate "caught all three targets" phrasing and the
  official 3-of-4 are both accurate, because Brown's fourth target is the incompletion on which he
  was injured — that target is not a drop or a coverage failure and must not be counted as one.
- **Kyed's five-man post-Brown receiver list** in `-102`. Efton Chism was inactive for this game per
  `-012`, so the group that actually dressed behind Brown was four, not five. The list is retained as
  reported roster context with that correction attached, not as a depth chart.
- **Rejected bylines, no rows emitted:** ESPN's "Multiple Authors" injury story, Greg Dudek (Boston
  Herald), and Justin Leger (NBC Sports Boston). None is in the NE source registry. The Doubs quote
  was taken from Perry's own registered piece instead of Leger's dedicated one.
- **The unbylined ESPN box score** used as a measurement spot check on `-001` and `-006`. It matched
  exactly, but it carries no byline and nothing is attributed to `local-writer-mike-reiss` from it.
  Counted as a measurement check, never as an independent registered origin.
- **Withdrawn reader framings, correctly not carried forward:** the beat reader's initial reading of
  Lazar's 57-of-67 and 60-of-71 Stevenson figures as a self-conflict (withdrawn — they reconcile
  exactly), and the reader rows for Perry's receiver snap counts and Lazar's snap figures (withdrawn
  in favour of the gamebook). No reliability inference attaches to Lazar from the snap counts.
- **The September 9 Larison and Wishnowsky practice-squad elevations.** Flagged by the official
  reader as unrowable inside the window; ARCHITECT ruled them already collected and promoted in the
  prior run. Not a coverage gap and not new.

## Run metrics

- Raw observations: 22 (13 official, 9 beat)
- Unique evidence clusters: 19 `dedup_key` clusters
- Originating sources: 7 — six registered (NFL gamebook, patriots.com communications, Kyed, Callahan,
  Lazar, Perry) and one unregistered (NFL Network, via an unbylined ESPN carrier)
- Independent origins per material cluster: the Brown injury *event* has 2 official origins; the
  Brown *diagnosis* has 1, unregistered; pass protection has 2 organizationally independent origins;
  every measured-usage cluster has 1 origin (the gamebook) plus 1 unbylined measurement check
- Repeats removed: 2 carriers of the single NFL Network origin collapsed (Perry's relay unrowed, the
  ESPN carrier unattributable); no rowed observation is a `repeat`
- Independent confirmations: 1 rowed (`-109` confirming `-108` on Vera-Tucker). Plus 3 unrowed
  measurement cross-checks: ESPN box score against `-001` and `-006`, and the gamebook "Not Active"
  block against `-012`
- Updates to prior observations: 2 (`-010` and `-101`, both updating `-009`)
- Contradictions: 2 — Lazar against Kyed on Stevenson's yards after contact, and Lazar's own
  28.6%→38.1% pressure revision. Plus 2 apparent contradictions resolved as **not** conflicts:
  Lazar's 57-of-67 and 60-of-71 Stevenson figures (different valid bases), and Callahan's
  "Brown led the team" against the official final line (a scope difference — true at his exit,
  per the ARCHITECT ruling recorded above)
- False positives excluded from routing: 8 (listed above); the `3-to-6 weeks` figure is the single
  item most likely to propagate if left unmarked. Callahan's target-lead claim was reclassified out
  of this count by the ARCHITECT ruling — it is true-at-exit evidence needing a caveat, not noise
- Routing: **1 escalate, 6 review, 6 log**
- Prior ledger trigger status, `til-2026-ne-20260909-002` (`ne-2026-off-q06`, `ne-2026-off-q07`):
  **partially triggered, keep open.** Its trigger reads "Official Week 1 RB totals then
  Stevenson/Kiner/Larison routes, protection, two-minute and inside-5 shares; Henderson Week 2
  practice." Occurred: official RB totals, snap share, carry share, target share, and two-minute
  involvement (11 of 11). Occurred but null: inside-5, n=1. **Not occurred:** route participation
  (no source exposes it for this game), protection (only team-employed charting), and Henderson's
  Week 2 practice. The row's own caveat — that a Henderson-absent Week 1 cannot test the healthy
  timeshare or count toward q07's trigger — holds unchanged and is reaffirmed by this synthesis.
- Prior ledger trigger status, `til-2026-ne-20260909-003` (`rf-2026-ne-backfield-timeshare-001`):
  **partially triggered, keep open.** Its trigger reads "Chart Stevenson/Kiner/Larison absolute
  route, protection, two-minute and inside-5 involvement after the official book." Two-minute is
  charted and inside-5 is charted as a null; **absolute route involvement could not be charted at
  all** and protection rests on one team-employed source. The finding needs no change. As the
  preflight notes, this row is the same sample as `-002` and is not an independent second
  measurement, so it cannot be closed on evidence `-002` could not close on.
- Synthesis elapsed time: about 25 minutes from assignment receipt to file write.
- Reader coverage:
  [official](../../runs/20260910T222845Z/reader-ne-official/run-report.csv),
  [beat](../../runs/20260910T222845Z/reader-ne-beat/run-report.csv).
- Proposed priority-board rows (not written to the board; promotion not authorized):
  [`scratchpad-priority-NE.csv`](../../runs/20260910T222845Z/scratchpad-priority-NE.csv).

## Sources

- [local-source-nfl-gamebooks](https://static.www.nfl.com/image/upload/v1789038923/gamecenter/a8fb0d78-4feb-11f1-abca-2c54536568a9.pdf) — published 2026-09-10T11:15:23Z (CDN asset stamp, not a publisher-declared publication time; see the timestamp limitation in every row's `notes` and the patriots.com publication anchor dated 2026-09-10T03:35:57Z); retrieved 2026-09-10T22:29:56Z; `obs-2026-ne-20260910t222845z-001` through `-009` and `-013`.
- [local-source-new-england-patriots](https://www.patriots.com/news/transcript-head-coach-mike-vrabel-press-conference-9-10-x2106) — published 2026-09-10T18:57:00Z; retrieved 2026-09-10T22:30:30Z; `obs-2026-ne-20260910t222845z-010`, `-011`.
- [local-source-new-england-patriots](https://www.patriots.com/news/week-1-inactives-patriots-at-seahawks) — published 2026-09-09T22:50:03Z; retrieved 2026-09-10T22:30:30Z; `obs-2026-ne-20260910t222845z-012`.
- [local-writer-doug-kyed](https://www.bostonherald.com/2026/09/10/patriots-a-j-brown-set-for-more-testing-after-reported-high-ankle-sprain-diagnosis/) — published 2026-09-10T15:28:09Z; retrieved 2026-09-10T22:30:00Z; `obs-2026-ne-20260910t222845z-101`, `-102`. Origin of the diagnosis is unregistered: NFL Network via https://www.espn.com/nfl/story/_/id/49891924/sources-aj-brown-believed-high-ankle-sprain-set-mri, bylined "Multiple Authors".
- [local-writer-doug-kyed](https://www.bostonherald.com/2026/09/09/best-and-worst-what-we-learned-in-patriots-13-10-demoralizing-loss-to-seahawks/) — published 2026-09-10T03:28:19Z; retrieved 2026-09-10T22:30:00Z; `obs-2026-ne-20260910t222845z-105`, `-109`.
- [local-writer-evan-lazar](https://www.patriots.com/news/after-further-review-drake-maye-breakdown-patriots-defense-review-and-quick-hit-film-notes-from-the-loss-to-the-seahawks) — published 2026-09-10T21:21:23Z; retrieved 2026-09-10T22:32:00Z; `obs-2026-ne-20260910t222845z-103`, `-107`, `-108`. Team-employed; not organizationally independent.
- [local-writer-phil-perry](https://www.nbcsportsboston.com/nfl/new-england-patriots/stock-watch-drake-maye-romeo-doubs-seahawks/802309/) — published 2026-09-10T12:41:54-04:00; retrieved 2026-09-10T22:31:00Z; `obs-2026-ne-20260910t222845z-104`.
- [local-writer-andrew-callahan](https://www.bostonherald.com/2026/09/10/callahan-drake-mayes-immature-play-cost-patriots-in-seattle-can-he-rebound-without-a-j-brown/) — published 2026-09-10T16:08:55Z; retrieved 2026-09-10T22:30:00Z; `obs-2026-ne-20260910t222845z-106`.
