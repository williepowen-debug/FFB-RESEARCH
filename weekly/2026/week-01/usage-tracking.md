---
schema_version: 1
record_id: rf-2026-w01-usage-tracking-001
record_type: research_finding
title: "Week 1 manual usage collection and ledger checks"
team_ids: ["TEN", "CLE", "DEN", "MIA", "ATL", "CAR", "NO", "DET", "SF", "ARI", "WAS", "NYG", "NE", "SEA", "GB", "PIT", "HOU"]
player_ids: []
season: 2026
week: 1
status: active
time_horizon: weekly
valid_as_of: 2026-09-09
last_verified: 2026-09-09
confidence: high
source_ids: ["local-source-nfl-gamebooks", "local-source-new-england-patriots", "local-source-seattle-seahawks"]
supersedes: []
---

# Week 1 manual usage collection and ledger checks

## Scope

This is a collection plan anchored to the **18 open team-ledger rows present after the September
6 catch-up**. Its method confidence does not imply confidence in a player projection. All Week 1
results, participation totals, routes and pressure measurements are **pending**. The linked
[opportunity watchlist](opportunity-watchlist.md) names conditional beneficiaries to test.

Use the existing [intelligence pipeline](../../../INTELLIGENCE_PIPELINE.md). No background job,
reminder, polling loop or automatic publication is configured by these files. The blank
[usage input CSV](usage-input.csv) is a manual working sheet, not a validated observation batch or
an alternate canonical dataset.

## Finding

A gamebook-first pilot with explicit sample boundaries can resolve eligibility and basic usage
without conflating offensive snaps, routes and touches. Complete route or pressure conclusions
require additional observable assignments; missing film remains a documented gap.

## Fantasy implication

The worksheet tests whether a conditional beneficiary actually earned useful opportunities. It
prevents inactive teammates, a few late touches or unobserved passing situations from being
misread as a stable role change in PPR, standard, tight-end-premium or IDP formats.

## Pilot one game before expanding

1. **Start with NE at SEA**, scheduled September 9 at 8:20 PM ET in the
   [canonical schedule](../../../league/schedule/2026.csv). Freeze a new run's publication window,
   registered source IDs and lanes only when beginning the actual intake. Re-read the relevant
   open ledgers and [matchup](games/NE-at-SEA.md); never reuse an old source timestamp for a new item.
2. **Before kickoff, verify eligibility.** Capture official final designations, inactive lists,
   elevations and late transactions. Record Henderson's status and Seattle's active backs. An
   active player is eligible to play; that alone does not promise an unrestricted workload.
3. **After the final, check the official gamebook.** An immediate factual triage may capture an
   injury or roster consequence. Do not perform a usage completion pass from highlights alone.
   If the book or participation data is unavailable, document the endpoint and gap and defer the
   dependent calculation.
4. **When the official book is available**, reconcile game ID, date, score, participants, carries,
   targets if provided, sacks and play-by-play. Record the exact downloadable document URL and
   page/table, publication timestamp if supplied, and actual retrieval time. A discovery page is
   not the supporting document. Missing publication precision remains a declared limitation; ARCH
   must resolve intake eligibility rather than inventing a timestamp.
5. **Chart only what the available evidence can support.** First pilot the NE and SEA backfields:
   opening-drive personnel, standalone series, routes versus protection, two-minute and inside-5
   opportunities. Use full-play footage with identifiable players for route work; record unseen
   assignments as unknown. If footage is insufficient, finish only the gamebook-supported portion.
6. **Audit before expanding.** Reconcile official volume totals; spot-check at least one ordinary
   drive and every claimed two-minute/inside-5 role change against the cited plays. Check each
   numerator against its denominator, list unknown plays and confirm that all calculations use
   the same QB/unit and game-state filters. An unobserved scoring or two-minute situation cannot
   resolve that role. Record what the pilot could and could not measure.
7. **Expand manually to the next relevant games** only after that audit, using the 18-row queue
   below plus the watchlist. A 24–48-hour completion pass is a planning window, not a guarantee:
   start later if gamebooks or usable footage are delayed. Preserve one-game sample limits. Emit
   atomic observations into the new run, validate them, synthesize, and route any ledger or
   canonical update through ARCH. For SF at LAR, include the [supplemental Nacua readiness
   gate](opportunity-watchlist.md#supplemental-early-game-gate) before interpreting his route sample.

## September 9 NE/SEA queue refresh

The 18-row list below is a **September 6 snapshot**, not a complete current queue. This
refresh covers the five open NE/SEA ledger rows added September 9; it does not re-audit
other teams. The [evidence audit](games/NE-at-SEA-evidence-audit.md) supplies the completed
historical work and source conflicts. Linked ledger triggers have been narrowed accordingly.

Eligibility is established by the [official 6:50 PM ET inactive list](https://www.patriots.com/news/week-1-inactives-patriots-at-seahawks),
published September 9: Henderson and Chism are inactive for NE; Horton, Okada, Emmanwori
and Kallerup are inactive for SEA. Previously recorded Clark/Bobo injured-reserve status
and the lack of a Bell elevation remain separate roster facts. Do not include them as
assumed game participants. Eligible does not mean a player ran a route or played a snap.

| Open ledger row | Collection after the official final book |
|---|---|
| SEA `til-2026-sea-20260909-002` | Thomas/Finley safety deployment beside Love; separately identify the actual nickel replacement and coverage assignments. Preserve unknown plays. |
| SEA `til-2026-sea-20260909-003` | Reuse that same secondary sample for the replacement-role finding; this is not an independent second measurement. A one-game forced pairing cannot settle the durable job. |
| SEA `til-2026-sea-20260909-005` | Price/Wilson/Holani opening series, designed carries, routes versus protection, two-minute and inside-five shares. |
| NE `til-2026-ne-20260909-002` | Stevenson/Kiner/Larison opportunities with matched denominators; follow Henderson's Week 2 availability separately. The healthy-timeshare hypotheses remain untested. |
| NE `til-2026-ne-20260909-003` | Reuse the same NE backfield chart for the canonical finding; separate absolute Stevenson involvement from a healthy Henderson comparison. |

Source-of-truth ledgers: [NE](../../../teams/AFC/East/New-England-Patriots/2026/intelligence-ledger.csv),
[SEA](../../../teams/NFC/West/Seattle-Seahawks/2026/intelligence-ledger.csv). All five remain open.
Extend the same pilot to Brown/Doubs/Douglas/Hollins/Kyle Williams receiving deployment and
Barner/Saubert/Arroyo routes versus blocking. Confirm actual position groups from participation
and film rather than interpreting the inactive list as a depth chart. Chart the opening offensive
lines, substitutions and identifiable pressure responsibility on that same sample.

No final book was recovered at the September 9 approximately 8:50 PM ET NFL game-center access
check. No measured usage rows are entered into the working CSV. Capture the actual final PDF
and participation table before calculating totals; record full-film coverage before calculating
route, assignment or blocker-loss rates. No background collection is configured.

## Original evidence access points

| Access point | Checked September 6 | Use after the game |
|---|---|---|
| [NFL scores](https://www.nfl.com/scores/) | Accessible; registered `local-source-nfl-gamebooks` discovery endpoint. | Select the completed game and follow its official book/participation link when exposed. |
| [NFL NE-at-SEA game center](https://www.nfl.com/games/patriots-at-seahawks-2026-reg-1) | Accessible pregame page. | Check for the completed game's statistics, play-by-play and linked book; capture the actual supporting URL. |
| [Seattle NE game center](https://www.seahawks.com/game-day/2026/reg-week1/seahawks-vs-patriots/) | Accessible pregame club page; no postgame book collected. | Official club fallback for the gamebook or participation attachment. |
| [Patriots schedule](https://www.patriots.com/schedule/) / [Seahawks schedule](https://www.seahawks.com/schedule/) | Accessible; no `Gamebook` link found in the retrieved schedule text. | Follow the applicable completed-game page and official postgame releases. Lack of a visible link is an access gap, not proof that no book exists. |

No Week 1 PDF URL is guessed or prefilled. Preserve the publisher's version and any later
correction date. Other games use each team's registered official endpoints and the NFL game
center; remain within the source IDs frozen for that intake. A team-employed recap and the same
team's gamebook are not independent reports. Paid or unavailable film is a coverage limitation,
not a reason to substitute highlights for complete route charting.

## Define the sample before counting

Keep the whole-game sample and any filtered sample separately identifiable. For each row record
team, player/unit, QB, quarter/clock range, score margin, personnel group, health/availability
context and method. Distinguish starting-QB play, reserve-QB play, an injury replacement, a
benched starter and late closing work. State any game-state filter precisely; do not label a
sample merely “competitive” or remove inconvenient plays after seeing the result.

For offensive film measures, exclude nullified no-plays and kneeldowns. Mark spikes and aborted
plays separately; exclude deliberate spikes from the route/dropback sample. Define dropbacks as
valid pass attempts, sacks and identifiable pass-play scrambles in the same sample. Do not count
a designed QB run as a scramble. Route assignments on scrambles follow the initial pass concept;
if that concept or player is not visible, mark unknown. Track penalties with erased touches as
context separately from official opportunities.

Official snap counts retain the publisher's definition. Do not force a custom filtered-play count
to equal a published offensive-snap denominator, and never label snap share as route share.

| Measure | Numerator | Matching denominator / context | Minimum evidence and limitation |
|---|---|---|---|
| Official offensive/defensive snap share | Published player snaps | Published corresponding team snaps | Cite the participation/snap table and its method. Leave share blank if the denominator is missing. Snaps include non-receiving assignments. |
| Route participation | Player routes | All qualifying team dropbacks in the defined sample | Complete identifiable routes are needed for a full-sample rate. Also report chartable/eligible dropback coverage and unknown plays. A known-subset rate must be labeled as such. |
| Targets per route | Targets on those charted routes | That player's charted routes in the same sample | Never divide full-game targets by partial-game routes. A target does not itself establish a first read. |
| Target share | Player targets | Team targets in the same sample | Use explicit target accounting; do not treat throwaways or unassigned attempts as player targets. Preserve the source definition. |
| RB rush share | Player designed RB rush attempts | Team designed RB rush attempts | Exclude QB scrambles/kneels from this denominator; separate play type and score state. A carry total alone misses routes and protection. |
| Receiving versus protection assignment | Routes and protection snaps, separately | Player pass-play snaps that can be classified | Record chip-and-release as a route with a chip note; unknown assignments are not protection zeros. |
| Two-minute role | Player snaps, routes and targets, separately | Team eligible snaps/dropbacks/targets with 2:00 or less remaining in Q2/Q4 | Keep quarter and score state; exclude kneels/spikes as above. Add a separately labeled observed hurry-up drive if it started earlier. No two-minute offense means no role test. |
| Inside-5 role | Player snaps, carries, routes and targets, separately | Team eligible plays, RB rushes, dropbacks or targets beginning at the opponent's 5-yard line or closer | Use the denominator matching the numerator. Separate rush from receiving opportunity; zero team opportunities leaves a share undefined. |
| Personnel/alignment | Player snaps or routes in a named group/alignment | Team eligible plays or dropbacks in that same group | Label 11/12/21 personnel by RB/TE count; verify players rather than inferring from outcome. Record outside/slot/in-line/backfield only when visible. |
| First-read rate | Plays on which a player's first-read assignment is discernible | Pass plays on which the first read is discernible | Film-based interpretation with method, locator and uncertainty; do not infer the read from the eventual target or from a head turn alone. |
| QB movement | Designed movement, pass-play scrambles and designed runs, separately | Identifiable relevant called pass/run plays | Separate opportunity from choice. No scramble in a clean pocket is not evidence of restricted mobility. |
| Line continuity | Player/combination snaps at the actual position | Chartable team offensive plays | Starting lineup can establish the opening five; mid-drive guard swaps and protection assignments require more evidence. |

## Defensive pressure and deployment

A gamebook can establish sacks and listed participation; it does **not** by itself establish a
complete pressure, blitz, alignment or rush-assignment chart. Published snap counts also do not
identify which snaps were pass rushes. If the film or a registered measured source cannot answer
a field, leave it unknown and keep the corresponding ledger trigger open.

Use a declared pressure method consistently: distinguish sacks, QB hits and attributed hurries;
identify whether the team dropback was pressured at least once. Multiple defenders can contribute
to one pressured dropback, so summed player pressures are not the team pressured-dropback count.
Keep credited sacks from the official book separate from a film evaluator's pressure attribution.

| Question | Required denominator and split | What cannot resolve it |
|---|---|---|
| Did the front pressure without extra rushers? | Team pressured dropbacks with exactly four rushers / chartable opponent dropbacks with exactly four rushers. Report five-plus and three-or-fewer separately, with counts and unknown-rusher plays. | Sack totals divided by pass attempts; highlight clips; calling every four-rusher simulated pressure a blitz. |
| Did an individual edge earn valuable work? | Player pass-rush snaps / opponent qualifying dropbacks; third-down rush snaps and early-down edge snaps in their own eligible situations. | Total defensive snaps without assignment or alignment. |
| Did blitzing improve pressure? | Pressured dropbacks with five-plus rushers / chartable five-plus-rusher dropbacks, using the same pressure definition as the four-rusher sample. | Comparing raw pressures when the rush opportunities differ; mixing source definitions of “blitz.” |

Here, **five-plus rushers** is an explicit counting convention, not a claim about another
provider's blitz taxonomy. Preserve the actual rusher count and provider definition if importing
measured data. With a small or incomplete sample, report counts and coverage rather than a
confident defensive quality upgrade.

## Evidence

### Eighteen open-ledger checks

Each row below names the existing ledger and target; it is not a new or duplicated ledger entry.
When an eligibility trigger occurs but usage remains unseen, resolve only the supported portion
and retain a narrower follow-up through ARCH. A future game having been played is not proof that
usable evidence of its trigger was recovered.

| Existing ledger / team | Target | Exact collection needed to test the trigger |
|---|---|---|
| [til-2026-mia-20260906-002](../../../teams/AFC/East/Miami-Dolphins/2026/intelligence-ledger.csv) — MIA | [rf-2026-mia-wide-receiver-personnel-001](../../../teams/AFC/East/Miami-Dolphins/2026/offense/wide-receivers/personnel-and-roster-paths.md) | Official active/elevated receivers and Bell participation; first-unit routes by alignment. Verify any Jarquez Hunter elevation separately: he is an RB, not a receiver-room route nominee. |
| [til-2026-cle-20260906-002](../../../teams/AFC/North/Cleveland-Browns/2026/intelligence-ledger.csv) — CLE | [rf-2026-cle-quarterback-receivers-001](../../../teams/AFC/North/Cleveland-Browns/2026/offense/quarterback-and-receivers.md) | Active receiver group after Tillman exit; Boston/Jeudy/Concepcion and other active WR routes in 11 and two-WR groups; red-zone targets and QB-unit context. |
| [til-2026-ten-20260829-001](../../../teams/AFC/South/Tennessee-Titans/2026/intelligence-ledger.csv) — TEN | [rf-2026-ten-backfield-receiver-allocation-001](../../../teams/AFC/South/Tennessee-Titans/2026/offense/backfield-and-receiver-allocation.md) | Active/absent pass catchers; routes/team dropbacks and targets/routes for the same QB and personnel groups; discernible first reads; RB passing-down and two-minute assignments. |
| [til-2026-den-20260822-001](../../../teams/AFC/West/Denver-Broncos/2026/intelligence-ledger.csv) — DEN | [den-off-qb-001](../../../teams/AFC/West/Denver-Broncos/2026/offense/hypotheses.csv) | Nix practice/game eligibility; designed launch-point movement, pass-play scrambles and full starting-unit drives; distinguish clean-pocket lack of opportunity from a physical restriction. |
| [til-2026-den-20260822-002](../../../teams/AFC/West/Denver-Broncos/2026/intelligence-ledger.csv) — DEN | [den-off-wr-001](../../../teams/AFC/West/Denver-Broncos/2026/offense/hypotheses.csv) | Waddle/Sutton/Mims/Engram routes, alignments, targets and discernible first reads on the same starting-QB dropbacks; separate 11/12 personnel and two-minute work. |
| [til-2026-den-20260822-003](../../../teams/AFC/West/Denver-Broncos/2026/intelligence-ledger.csv) — DEN | [den-off-rb-001](../../../teams/AFC/West/Denver-Broncos/2026/offense/hypotheses.csv) | Confirm active Dobbins/Harvey/Coleman comparison; opening series, RB rush share, routes, protection, two-minute and inside-5 opportunities with matched denominators. |
| [til-2026-nyg-20260906-002](../../../teams/NFC/East/New-York-Giants/2026/intelligence-ledger.csv) — NYG | [to-2026-nyg-overview-001](../../../teams/NFC/East/New-York-Giants/2026/overview.md) | Official Week 1 inactive/active specialist context and intervening kicker transactions for Zvada; gamebook participation if he plays. No field-goal attempt does not imply inactivity. |
| [til-2026-was-20260822-001](../../../teams/NFC/East/Washington-Commanders/2026/intelligence-ledger.csv) — WAS | [was-def-001](../../../teams/NFC/East/Washington-Commanders/2026/defense/hypotheses.csv) | Starting edges and rush opportunities; pressured qualifying dropbacks split by exactly four, five-plus and three-or-fewer rushers, with chartable coverage and unknowns. Sacks alone cannot close this. |
| [til-2026-det-20260822-001](../../../teams/NFC/North/Detroit-Lions/2026/intelligence-ledger.csv) — DET | [det-def-001](../../../teams/NFC/North/Detroit-Lions/2026/defense/hypotheses.csv) | Edges alongside Hutchinson: defensive snaps, early-down alignment, third-down rush packages and player rush opportunities; pressures require attributable complete film or a defined measured source. |
| [til-2026-atl-20260829-001](../../../teams/NFC/South/Atlanta-Falcons/2026/intelligence-ledger.csv) — ATL | [atl-2026-off-q03;atl-2026-off-q09](../../../teams/NFC/South/Atlanta-Falcons/2026/offense/hypotheses.csv) | Bijan/Brian Robinson usage by personnel; named run concepts only when chartable; designed screens, routes, two-minute and inside-5 opportunities. Concept installation alone does not show frequency. |
| [til-2026-car-20260822-001](../../../teams/NFC/South/Carolina-Panthers/2026/intelligence-ledger.csv) — CAR | [car-2026-off-q05](../../../teams/NFC/South/Carolina-Panthers/2026/offense/hypotheses.csv) | Hubbard/Brooks/Dillon active and in-game health context; opening-drive and standalone-series work, routes, protection and inside-5 allocation. An absent back prevents a healthy-group comparison. |
| [til-2026-car-20260825-001](../../../teams/NFC/South/Carolina-Panthers/2026/intelligence-ledger.csv) — CAR | [car-2026-off-q04](../../../teams/NFC/South/Carolina-Panthers/2026/offense/hypotheses.csv) | Waller routes/team dropbacks, targets/routes, third-down and red-zone packages versus other active TEs; separate a managed ramp from an established specialist role. |
| [til-2026-car-20260906-002](../../../teams/NFC/South/Carolina-Panthers/2026/intelligence-ledger.csv) — CAR | [car-2026-off-q03](../../../teams/NFC/South/Carolina-Panthers/2026/offense/hypotheses.csv) | Legette routes, first-read/target order and two-minute participation alongside available McMillan/Coker; practice return alone does not resolve receiving hierarchy. |
| [til-2026-no-20260821-002](../../../teams/NFC/South/New-Orleans-Saints/2026/intelligence-ledger.csv) — NO | [no-2026-off-q07](../../../teams/NFC/South/New-Orleans-Saints/2026/offense/hypotheses.csv) | Official Ruiz status and opening right guard from the gamebook; chart any RG rotation and attributable protection assignments. A depth-chart listing alone does not prove healthy game participation. |
| [til-2026-no-20260906-003](../../../teams/NFC/South/New-Orleans-Saints/2026/intelligence-ledger.csv) — NO | [rf-2026-no-skill-position-allocation-001](../../../teams/NFC/South/New-Orleans-Saints/2026/offense/skill-position-allocation.md) | Active/elevated receivers; Vele/Lance/Brown routes and targets relative to Olave by personnel, QB and red-zone/two-minute situation; do not promote a return-only role as a receiving role. |
| [til-2026-ari-20260821-003](../../../teams/NFC/West/Arizona-Cardinals/2026/intelligence-ledger.csv) — ARI | [ari-off-001](../../../teams/NFC/West/Arizona-Cardinals/2026/offense/hypotheses.csv) | Love return to practice, final game designation and active list first; if eligible, record workload and restrictions before applying a healthy lead-back test. |
| [til-2026-sf-20260821-001](../../../teams/NFC/West/San-Francisco-49ers/2026/intelligence-ledger.csv) — SF | [sf-off-rookie-001;sf-off-wr-001](../../../teams/NFC/West/San-Francisco-49ers/2026/offense/hypotheses.csv) | Stribling route participation and targets by QB unit, receiver availability and personnel; red-zone routes versus isolated preseason production. |
| [til-2026-sf-20260829-001](../../../teams/NFC/West/San-Francisco-49ers/2026/intelligence-ledger.csv) — SF | [sf-off-ol-001](../../../teams/NFC/West/San-Francisco-49ers/2026/offense/hypotheses.csv) | Opening left guard from official participation; Carver Willis and alternatives by offensive play, any substitutions and chartable protection assignments. |

The watchlist's GB, PIT, HOU and additional NO/NE/SEA allocation questions also receive a worksheet
row when their games are reviewed. They do not become extra open ledger entries merely by being
listed here. Link their existing hypothesis IDs and let synthesis determine whether review is
warranted.

## Filling the blank input CSV

Use **one row per player/unit, metric and precisely defined sample**. The header-only file contains
no measured values or placeholder zeros. `player_or_unit` is a human-readable working label;
resolve canonical player IDs when creating the immutable observation, rather than inventing them.

- `numerator` and `denominator` are counts for the same metric/sample. Keep the calculation out of
  the raw cells; compute a rate only after checking the counts. If the denominator is zero, leave
  the rate undefined. Do not use a zero numerator for missing evidence.
- `eligible_plays` is the full eligible sample; `chartable_plays` is the part for which that metric
  can be observed; `unknown_plays` is the remainder. For play-charted samples, require
  `eligible_plays = chartable_plays + unknown_plays`. For non-play eligibility checks, leave these
  fields blank rather than forcing an invented denominator.
- `quarter_filter`, `game_clock_filter`, `score_margin_filter`, `qb_unit` and `personnel_filter`
  describe the exact sample. `player_available_context` records inactive peers, injuries, planned
  limitations and substitutions. Do not merge rows with different filters into one percentage.
- `source_id` is the registered source actually supporting the row. `source_url` points to the
  original item; `source_locator` identifies page/table or play/film timestamp. Publication and
  retrieval fields use exposed ISO timestamps with timezone. Leave unavailable precision blank
  in this working sheet and state the gap in `notes`; do not emit a compliant-looking fabricated
  timestamp into the validated intake.
- `method` distinguishes official gamebook, published snaps, complete film chart, partial film
  chart or reported expectation. `status` should say pending, partial, measured or unavailable.
  An expectation is not a measured count. `ledger_id` may be blank for watchlist-only candidates;
  `target_ids` uses existing record/question IDs, separated with semicolons where needed.

Before synthesis, preserve the source and audit notes, then emit the substantive claims using
[reader-observations.csv](../../../templates/reader-observations.csv), not this worksheet's shape.
All denominators, scope limits and source relationships must survive into the observation notes
or supporting synthesis. Run the existing intelligence/repository checks; this task adds no
validator, automated workflow or alternate observation schema.

## Assessment

Keep a ledger deferred when its relevant situations never occurred, player availability spoiled
the comparison, or the evidence cannot identify the assignments. Promote official eligibility
changes separately from usage conclusions. One early game can establish a role observation for
that game; it cannot by itself establish a season-long percentage.

The first deliverable after kickoff is a source-access and eligibility check. The first usage
completion deliverable waits for the official book and sufficient additional evidence. Pending
work is collection, charting, spot checks, new observations, synthesis and ARCH disposition—not
filling the current blank sheet with estimates.

## Sources

- [September 6 readiness handoff](../../../intelligence/2026/runs/20260906T210715Z/handoff.md) — supplemental early-game status checks; route samples still require game evidence.
- [September 6 catch-up handoff](../../../intelligence/2026/runs/20260906T193157Z/handoff.md) — roster and availability baseline, verified 2026-09-06.
- Team intelligence ledgers linked in the 18-row table — open state read 2026-09-06; individual historical review dates remain in those files.
- [Reader/synthesis pipeline](../../../INTELLIGENCE_PIPELINE.md) and [preseason two-pass runbook](../../../PRESEASON_GAME_RUNBOOK.md) — existing provenance, access-gap and promotion controls; the one-game regular-season pilot above applies them without scheduling anything.
- Official NFL and club access points in the source table — accessibility checked 2026-09-06; Week 1 gamebooks and results remain pending.
