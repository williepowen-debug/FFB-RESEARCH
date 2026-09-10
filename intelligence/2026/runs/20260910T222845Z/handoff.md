# Run handoff — NE at SEA Week 1 postgame completion pass

- Run: `20260910T222845Z`
- Frozen window: `2026-09-09T21:07:06Z` to `2026-09-10T22:28:45Z`, contiguous with the pre-kickoff run.
- Pass type: postgame usage completion. Teams: NE, SEA.
- Syntheses: [`ti-2026-ne-20260910-001`](../../syntheses/2026-09-10/NE.md) · [`ti-2026-sea-20260910-001`](../../syntheses/2026-09-10/SEA.md)
- Board: [2026-09-10 priority board](../../priority/2026-09-10/priority-board.csv) — 13 rows, 2 escalate, 11 review.

## Result

Seattle 13, New England 10. New England led 10-0 into the second half, out-gained Seattle and held
the ball for 34:17, and lost on three interceptions. Both teams lost a significant player.

## Intake

| Reader | Lanes | Cap | Emitted | Sources reached |
|---|---|---|---|---|
| reader-ne-official | official_record, data | 13 | 13 | gamebook, patriots.com; ESPN reached, no attributable byline |
| reader-ne-beat | beat_reporting, analysis | 9 | 9 | Lazar, Kyed, Callahan, Perry; Reiss reached, no new material |
| reader-sea-official | official_record, data | 15 | 13 | gamebook, seahawks.com; ESPN reached, unbylined and undated |
| reader-sea-beat | beat_reporting, analysis | 8 | 8 | Boyle, Crabtree, Henderson |

43 observations. Caps were raised twice by ARCHITECT mid-run and both raises are recorded in the
assignment notes. Two sources were **inaccessible**: Bob Condotta (HTTP 403 on both candidate items)
and Michael-Shawn Dugar (host refused). Both are paywalled beats, and both are exactly where
rotation and alignment detail would live. That is a coverage gap, not silence.

## What this run established

- **Two escalations**, both official-record injuries with immediate Week 2 lineup consequences:
  Sam Darnold (hip, 5 of 50 snaps, injured on the opening possession) and A.J. Brown (ankle, ruled
  out to start Q4). **Neither has a prognosis.** No timetable, designation, roster move or named
  Week 2 starter exists for either player.
- **First measured usage of the season**, reconciled into
  [`usage-input.csv`](../../../../weekly/2026/week-01/usage-input.csv) as 27 rows against explicitly
  defined denominators. Headline findings: Stevenson at an 85% snap share with the entire two-minute
  role; a near-even Price/Holani committee at 24 snaps to 23; Rodney Thomas II at 70 of 71 defensive
  snaps beside Love with AJ Finley active and at zero.
- **A reusable denominator definition.** Statistical offensive plays and actual snaps differ by
  plays that were snapped and then wiped out by a live-ball penalty. NE 67+4=71, SEA 48+2=50, and
  the two teams' bases cross-check exactly. Written up in the
  [pilot audit](../../../../weekly/2026/week-01/usage-tracking.md).

## What this run could NOT establish, and why it matters

1. **No routes, no pass-block snaps, no coverage alignment.** The gamebook's participation table is
   the only participation artefact, it is self-labelled "Unofficial", and it carries no position
   labels. Seattle's nickel defender is unidentified by any source.
2. **Two null results.** New England ran ONE snap inside the Seattle 5; Seattle ran ZERO goal-to-go
   snaps. Both inside-five questions are unanswered rather than answered negatively.
3. **Neither injury prognosis is reported.** The A.J. Brown high-ankle-sprain diagnosis traces to
   NFL Network — unregistered — and Vrabel declined to confirm it. Circulating "3-to-6 weeks" and
   "2-to-6 weeks" figures are general expectations for the injury class, **not reported timelines
   for this player**, and were deliberately excluded.

## Registry gap opened by this run

**Ledger triggers have been naming evidence no registered source can supply.** Four open rows
required routes-versus-protection charting or coverage alignment. Those triggers can never fire, so
the rows would have sat "open" forever while appearing to be under active monitoring. All affected
triggers were rewritten to name obtainable evidence, and the gap is recorded as its own open row
(`til-2026-sea-20260910-009`). **Registering a route/alignment source is the highest-value
improvement available to this repository.**

## Repository changes made by ARCHITECT

- Ledger dispositions: NE and SEA each now carry 15 rows. Five prior rows were superseded rather
  than force-resolved, because their triggers fired only partially.
- **Validator fix.** `superseded` was documented in `INTELLIGENCE_PIPELINE.md` but unreachable in
  `scripts/validate_intelligence.py`: every disposition was pinned to a single permitted status, so
  no row could ever record that a later row replaced its decision. Fixed, documented, and covered by
  a regression test. This was found because this run produced the first partially-triggered rows.
- **Line-ending fix.** Python's `csv` module defaults to CRLF, which fails `git diff --check` — a
  gate command. Seven files normalised and a `.gitattributes` added so it cannot recur.

## Next checks

| Check | Owner | Trigger |
|---|---|---|
| Darnold prognosis and a NAMED Week 2 starter | SEA | First official Week 2 injury report |
| A.J. Brown status | NE | Vrabel's promised update, week of 2026-09-14 |
| TreVeyon Henderson Week 2 practice | NE | First Week 2 practice report; unestablished by any registered source |
| Whether the Price/Holani split holds | SEA | Week 2 at Arizona |
| Doubs snap and target share | NE | Week 2, assessed jointly with Brown's availability |
| Register a route/alignment source | ARCHITECT | Before Week 2 collection |
