---
name: architect-routing-and-handoff
description: How ARCHITECT calibrates synthesizer routing (escalate/review/log) and expects hand-off when promotion is not authorized
metadata:
  type: feedback
---

When promotion is not authorized, write the synthesis only; put proposed priority-board rows in a
scratchpad CSV (path given in the assignment) using the template header, and report prior-ledger
trigger status in the synthesis Run metrics without editing the ledger or board.

**Why:** ARCHITECT assembles the board and records ledger dispositions itself (2026-09-09 NE
Week 1 pregame run); a synthesizer writing into `intelligence/<season>/priority/` would
pre-empt that step.

**How to apply:** Routing calibration ARCHITECT confirmed: official OUT/IN designation with a
direct lineup consequence = `escalate`; team-site depth analysis plus one independent beat
confirmation of a forced (injury-driven) depth order describes the week but does not reach the
`review` bar for seasonal role hypotheses — route a `review` only to record a deferred disposition
and to flag that injury-absent usage is not a valid test of a timeshare hypothesis; contract
extensions and special-teams elevations = `log`. Match the prior dated synthesis's front-matter
and section shape exactly, use relative links, and count independent origins (not articles) in
the reconciled-evidence section.

**Postgame extension (confirmed 2026-09-10, NE Week 1 postgame run).** Measured official usage
raises the `review` bar's *supply*, not the `escalate` bar: a full postgame book can legitimately
produce one `escalate` and many `review`s, one per open hypothesis that the measurement touches.
Split reviews by *evidence*, not by hypothesis — hypotheses sharing one measurement (e.g. an alpha-WR
claim and a target-concentration claim off the same target table) are one signal. An in-game injury
recorded in the official play-by-play plus a head-coach statement of unknown availability DOES clear
the escalate bar, because the official record and the immediate next-week lineup consequence are both
present, even with no formal OUT designation yet.

**Do not regenerate `catalog.jsonl`.** `validate_repository.py` will report it stale after you add a
synthesis; that error is expected and is not "your own file".

**Why:** parallel team synthesizers in the same run hit the same staleness at the same time, and
concurrent `generate_catalog.py` writes to one shared file risk a torn write. ARCHITECT regenerates
once at the run's validation gate, after every team's synthesis has landed.

**How to apply:** run both validators, confirm the ONLY repository error is catalog staleness, verify
it is attributable to your new record (grep the record_id out of catalog.jsonl), and report it to
ARCHITECT as a pending gate step instead of fixing it.

**A truncated sample is not an absent sample (ARCHITECT overturned me on this, 2026-09-10).** Before
calling a hypothesis untestable because a player left early or arrived late, **try restricting the
denominator to the window he was actually available.** I filed A.J. Brown's alpha-WR1 question as
untestable off a 31-of-71-snap game; restricted to the snaps he played he led the team in targets
(4 of 13, ~31%), which is partial *confirming* evidence. The distinction that matters:

- Zero snaps (Henderson, inactive) → nothing computable → genuinely no evidence.
- Partial snaps (Brown, injured in Q3) → restrict the denominator → real evidence on a limited base.

Both still fail a *full-game* trigger, so the trigger exclusion can be right while the disposition is
wrong. Say "does not complete the trigger," not "untestable."

**Corollary — a beat claim that contradicts the official final line may be a scope difference, not an
error.** Callahan's "Brown led in receptions, targets and yards" was true at his exit and false at
the final whistle. Check the claim against the window the writer was describing before filing it as
a contradiction or as noise; the fix is a caveat, not exclusion.

**Why:** ARCHITECT checked this from the play-by-play because I flagged it as the one call to
overturn. Flagging the weakest call is what got it caught — keep doing that in the hand-off report.

**How to apply:** on any postgame synthesis involving an in-game injury, ejection, benching or
mid-game debut, compute the restricted-window split before writing the hypothesis-impact bullet, and
say explicitly which denominator each figure sits on.
