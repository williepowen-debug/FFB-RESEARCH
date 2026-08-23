---
schema_version: 1
record_id: ti-2026-det-20260822-001
record_type: team_intelligence
title: "Detroit Lions intelligence synthesis — 2026-08-22"
team_ids: ["DET"]
player_ids: []
season: 2026
week: null
status: draft
time_horizon: seasonal
valid_as_of: 2026-08-22
last_verified: 2026-08-22
confidence: medium
source_ids: ["local-source-detroit-lions"]
supersedes: []
observation_ids: ["obs-2026-det-20260822t232931z-001", "obs-2026-det-20260822t232931z-002", "obs-2026-det-20260822t232931z-003", "obs-2026-det-20260822t232931z-004", "obs-2026-det-20260822t232931z-005"]
run_ids: ["20260822T232931Z"]
---

# Detroit Lions intelligence synthesis — 2026-08-22

## Executive signal

D.J. Wonnum sacked Jayden Daniels during Washington's only starting-offense possession, while
rookie Derrick Moore recorded a sack and forced fumble in his preseason debut. Those separate
performances are directionally supportive of Detroit's complementary-edge hypothesis and warrant
review after role-specific snap evidence arrives. Skyler Gill-Howard's early first-team snaps are
a useful depth-development signal but do not map directly to an active P1. The batch does not test
Detroit's four offensive P1 questions, Jack Campbell's role, or the starting safeties' health. No
signal meets the escalation threshold and no current conclusion changes.

## Reconciled evidence

- **Team offensive result:** Detroit gained 279 yards and converted 52.9 percent of third downs in
  the win (`obs-2026-det-20260822t232931z-001`). This is one official result cluster, but mixed
  units and the absence of the team's core fantasy players from the observation make it unsuitable
  for judging the Petzing offense or rebuilt line.
- **Derrick Moore debut:** Moore recorded a sack, forced fumble, and tackle for loss
  (`obs-2026-det-20260822t232931z-002`) after returning from a minor groin injury. This is one
  performance cluster from the team notebook, with no snap count or package context.
- **Gill-Howard deployment and production:** Gill-Howard received early first-team defensive snaps
  (`obs-2026-det-20260822t232931z-003`) and recorded a quarterback hit and tackle for loss while
  producing additional pressure (`obs-2026-det-20260822t232931z-004`). These are distinct role and
  performance clusters from one team-controlled origin, not independent confirmation.
- **Wonnum versus Washington's first unit:** Wonnum sacked Daniels during Washington's sole
  starting-offense possession (`obs-2026-det-20260822t232931z-005`). This is the strongest opponent
  context in the batch, but it remains one play from one drive.

All five observations have unique deduplication keys. There are no emitted repeats,
confirmations, updates, or contradictions.

## Hypothesis impact

- `det-off-001` (Gibbs workload): **not addressed; no change.** No Gibbs or healthy first-team
  backfield usage entered the batch.
- `det-off-002` (LaPorta route role): **not addressed; no change.** No first-team tight-end routes,
  targets, personnel groups, or red-zone usage entered the batch.
- `det-off-003` (St. Brown target floor): **not addressed; no change.** The aggregate team offense
  result contains no Goff/St. Brown first-team target distribution.
- `det-off-005` (offensive-line transition): **not testable; no change.** Team yardage and third-down
  rate across mixed units do not establish the final starting five or clean first-team protection;
  Washington also recorded five sacks in the game, but that opponent observation was not admitted
  to Detroit's batch as a line-specific measured claim.
- `det-def-001` (Hutchinson and edge rotation): **review, directionally supportive but unchanged.**
  Wonnum produced against Washington's first unit, and Moore supplied splash production in his
  debut. The batch lacks their rush-package snaps, win or pressure rates, alignment, and work
  alongside Hutchinson.
- `det-def-002` (Jack Campbell): **not addressed; no change.** No green-dot, snap, tackle-funnel, or
  subpackage evidence entered the batch.
- `det-def-003` (Joseph and Branch health): **not addressed; no change.** Neither safety has an
  availability or participation observation in this run.

Detroit has no open intelligence-ledger rows. ARCH retains authority over any new ledger
disposition created from this synthesis.

## Routing decisions

| Level | Signal | Observation IDs | Next action |
|---|---|---|---|
| review | Wonnum produced a sack against Washington's first unit and Moore recorded a sack and forced fumble in his debut. | `obs-2026-det-20260822t232931z-002`; `obs-2026-det-20260822t232931z-005` | Obtain edge snaps, third-down rush packages, alignments, and pressures alongside Hutchinson before reconsidering `det-def-001`. |
| log | Gill-Howard received early first-team snaps and generated a quarterback hit and tackle for loss. | `obs-2026-det-20260822t232931z-003`; `obs-2026-det-20260822t232931z-004` | Check final interior rotation and regular-season subpackage snaps; preserve as developmental depth evidence. |

Routing totals: one `log`, one `review`, and zero `escalate` signals.

## Conflicts and uncertainty

There are no direct conflicts or independent confirmations. All five observations derive from
Detroit's team-controlled reporting. The NFL endpoint supplied no downloadable 2026 gamebook or
participation report, four assigned reporters produced no attributable in-window game item, and
the MLive endpoint was inaccessible. The missing snap, route, personnel, and pressure data leaves
both the edge review and every offensive question provisional.

## Excluded noise

- Detroit's 279 yards and 52.9 percent third-down conversion rate
  (`obs-2026-det-20260822t232931z-001`) were excluded from routing. Mixed-unit aggregate output
  without core-player or line context does not test an active hypothesis.

## Run metrics

- Raw observations: 5
- Unique evidence clusters: 5
- Repeats removed: 0
- Independent confirmations: 0
- Conflicts: 0
- False positives excluded: 1
- Routing: 1 log, 1 review, 0 escalate
- Applicable active P1 hypotheses assessed: 7 (`det-off-001`, `det-off-002`, `det-off-003`,
  `det-off-005`, `det-def-001`, `det-def-002`, `det-def-003`); 1 routed for review, 0 changed
- Promotions: 0 (not authorized)
- Synthesis elapsed time: approximately 9 minutes

## Sources

- Detroit Lions, [Recap: Lions vs. Commanders](https://www.detroitlions.com/news/recap-lions-vs-commanders-dobbs-meeks-williams), published 2026-08-22T15:27:00-04:00, retrieved 2026-08-22T23:31:57Z — `obs-2026-det-20260822t232931z-001`.
- Detroit Lions, [Notebook: Rookie Moore makes impact in preseason debut](https://www.detroitlions.com/news/notebook-rookie-moore-makes-impact-detroit-lions-preseason-debut-gill-howard-meeks), published 2026-08-22T17:03:00-04:00, retrieved 2026-08-22T23:31:57Z — `obs-2026-det-20260822t232931z-002` through `obs-2026-det-20260822t232931z-005`.
