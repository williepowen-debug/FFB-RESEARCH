---
schema_version: 1
record_id: rf-2026-w01-ne-sea-evidence-audit-001
record_type: research_finding
title: "NE at SEA: remaining-gap audit and source reconciliation"
team_ids: ["NE", "SEA"]
player_ids: []
season: 2026
week: 1
status: active
time_horizon: weekly
valid_as_of: 2026-09-09
last_verified: 2026-09-09
confidence: medium
source_ids: ["local-source-seattle-seahawks", "local-source-new-england-patriots", "local-source-nfl-gamebooks", "local-writer-evan-lazar"]
supersedes: []
---

# NE at SEA: remaining-gap audit

## Scope

September 9, 2026 ET, after the scheduled 8:20 PM kickoff. This extends the
[earlier supplement](NE-at-SEA-research-supplement.md), existing team findings and canonical player
profiles. It uses historical data and pregame publications; it contains no live-game analysis.
The [8:03 PM forecast](NE-at-SEA.md) remains a dated forecast, not retroactively improved evidence.

## Finding

The six gaps have been worked through. Historical counts, pressure context, motion/play-action
and a reproducible opponent adjustment are now documented. Actual 2026 coverage assignments,
blocker responsibility and workload remain evidence-dependent; the updated collection queue
names exactly what must be measured. No unavailable field is treated as a zero or a confirmed role.

| Gap and existing foundation | Work completed | Remaining limitation |
|---|---|---|
| Older player statistics — canonical profiles already contained career tables | Checked 19 official biographies; retained 87 NFL count rows for 18 players, verified Price's 2025 college line, corrected three profiles and added Darnold's missing sack/fumble columns | Older targets, returns and college rows are not all independently verified; official blank cells remain unknown |
| Protection — team line/front records and earlier sack comparison | Added PFR pressure conversion, NGS time to throw and FTN rusher-count splits | Individual blocker losses, quick pressure and complete protection assignments remain unmeasured |
| Coverage — existing secondary records and Lazar's matchup breakdown | Reconciled coverage versus rusher count; corroborated the Super Bowl's four-rusher sacks with FTN | No verified Week 1 shadow, slot, TE matchup or replacement-safety assignment chart |
| Offensive usage — existing allocation findings and manual pilot | Added historical scoring opportunities, corrected eligibility context and expanded the five open NE/SEA review triggers | Current routes/protection, two-minute work and personnel shares require participation plus identifiable film |
| Opponents and tendencies — earlier raw EPA baseline | Added opponent context, motion, under-center and play-action frequencies | No reliable snap-pace or complete personnel-frequency sample; 2025 is not a measurement of Fleury's 2026 offense |
| Stale references and corroboration — existing weekly/ledger records | Updated stale profile claims, linked canonical findings to this audit, refreshed the September 9 queue | One PFR snapshot discrepancy remains explicitly unresolved; sources sharing an origin are not counted twice |

## Fantasy implication

**Inference:** Seattle's defensive advantage has firmer historical support, but the absent
safety/nickel personnel still matter. Maye's response to pressure is a distinct risk from his
line's sack total. New England retains the stronger historical offensive EPA after this simple
schedule check. That supports a competitive matchup rather than a confident repeat of the Super
Bowl. These additions do not produce a calibrated score, spread, player projection or win probability.

For PPR, historical catches cannot settle who runs routes tonight. Stevenson remains an
injury-forced volume candidate; Price's lead listing still needs a measured share against Wilson
and Holani. Henry and Barner have documented scoring-area opportunity, with current receiving
competition and protection duties left open.

## Evidence

### Historical counts corrected or completed

- **Darnold:** added previously omitted sack and fumble columns. His 2025 counts are
  27 sacks and 35 rushes; career totals are 224 sacks and 311 rushes. The earlier rushing
  column was correctly labeled; this is an addition, not a correction to those rush counts.
- **Maye:** 2025 fumbles are 9, not 8; career fumbles are 18, not 17. Lost-fumble totals are unchanged.
- **Charbonnet:** six starts in 2024 and eight career starts, correcting 11 and 13.
- **Stevenson:** all four 2025 playoff games total 58 carries/217 yards and 12 catches/126 yards,
  with one receiving TD. The old three-game table omitted the Super Bowl. His 2025 ordinary target count is 37. The first nflverse filter
  admitted a two-point attempt and returned 38; excluding conversions resolves that discrepancy.
  The earlier target seasons still need an independent same-method check.

The [primary count snapshot and limits](../research/ne-sea/audit/README.md#official-player-table-audit)
link each original biography. Eleven source career receiving-average displays conflict with their
own counts; the profiles retain arithmetic from yards/receptions rather than copying those errors.

### Pressure is not just sacks

| 2025 regular season | Maye | Darnold |
|---|---|---|
| PFR sacks / pressures, season snapshot | 47 / 131 | 27 / 109 |
| Sacks per pressure | 35.9% | 24.8% |
| PFR published pressure percentage | 21.8% | 21.0% |
| NFL NGS average time to throw | 2.97 sec | 2.87 sec |

PFR's weekly Maye rows total **132** pressures, giving 35.6% sack conversion; the season table
has one fewer hurry. Both versions are retained. In the Super Bowl, PFR counted 18 Maye pressures
and six sacks versus 14 Darnold pressures and one sack. That supports separating pressure arrival
from its outcome, not assigning every sack to the QB or line. NGS release time also reflects
play design and situations; it is neither quick-pressure rate nor time between snaps.
See [pressure data](../research/ne-sea/audit/pfr-pressure.csv),
[conflict](../research/ne-sea/audit/pfr-reconciliation.csv) and
[NGS data](../research/ne-sea/audit/ngs-passing.csv).

FTN independently charts **five of Seattle's six Super Bowl sacks with exactly four rushers**:
45 such NE dropbacks produced five sacks; eight against five-plus produced one. This corroborates
the existing team-site breakdown. Rusher count does not identify the coverage shell, disguise,
individual block lost or pressure frequency. The stored subjective QB-fault flags are not adopted
as proven responsibility. [FTN Data via nflverse; CC BY-SA 4.0 adaptation](../research/ne-sea/audit/README.md#source-definitions-and-reuse).

### Opponent context

The audit also corrects the baseline's inclusion of conversion tries: ordinary offense,
assigned targets and scoring opportunities now exclude two-point attempts. The earlier
supplement and generated CSVs were corrected together; prior versions remain in Git history.

| 2025 EPA/play | Raw | One-step opponent normalized |
|---|---:|---:|
| NE offense | +0.157 | +0.130 |
| SEA offense | +0.030 | +0.031 |
| NE defense, EPA allowed | −0.046 | −0.002 |
| SEA defense, EPA allowed | −0.118 | −0.130 |

New England's defensive schedule had weaker opposing offensive results; Seattle's had stronger
ones. This simple leave-focal-team-out calculation changes the comparison materially, while NE's
offensive advantage remains. It is descriptive, without QB/lineup or game-state adjustment.
[Full denominators, opponent rows and method](../research/ne-sea/audit/README.md).

### Tendencies and scoring opportunities

| 2025 regular-season offense | NE | SEA |
|---|---:|---:|
| Under center / known QB locations | 452 / 1,011 (44.7%) | 531 / 994 (53.4%) |
| Motion / known eligible plays | 536 / 1,014 (52.9%) | 567 / 994 (57.0%) |
| Play-action dropbacks / dropbacks with known flag | 148 / 613 (24.1%) | 131 / 518 (25.3%) |
| EPA/dropback, play action / other | +0.339 / +0.293 | +0.405 / +0.020 |

[FTN Data via nflverse; CC BY-SA 4.0 adaptation](../research/ne-sea/audit/README.md#source-definitions-and-reuse).
All eligible NE/SEA plays matched charting rows; three NE regular-season QB-location fields were
unknown. Play-action efficiency is selected by situation and does not prove that calling it more
would reproduce that result. Seattle's coaching continuity is an inference, not a 2026 frequency.

Historical PBP adds specificity: Henry had 22 assigned targets inside the 20 and six inside the
five; Barner had 13 and three. Stevenson had 11 inside-five designed carries to Henderson's eight;
Seattle's Charbonnet had 18 to Walker's eight. Those departed/absent backs' shares do not transfer
automatically to Price. [Counts and definitions](../research/ne-sea/audit/historical-scoring-opportunities.csv).

### Coverage and current usage boundaries

The existing [Seattle secondary finding](../../../../teams/NFC/West/Seattle-Seahawks/2026/defense/secondary-replacement-roles.md)
already separates Emmanwori's nickel role from Okada's safety role. Thomas/Finley availability
does not prove who takes either coverage assignment. Likewise, the existing Lazar NGS table's
Maye cover-six result (−0.28 EPA/dropback on only 36 dropbacks) is a small historical split,
not evidence of tonight's exact matchups.

The official pregame list also excludes NE receiver **Efton Chism** and SEA tight end **Nick
Kallerup**, alongside the already recorded Henderson, Horton, Okada and Emmanwori absences.
That narrows the eligible comparison groups; it establishes no route hierarchy.
[Official inactive list, published September 9, 6:50 PM ET](https://www.patriots.com/news/week-1-inactives-patriots-at-seahawks).

At the 8:50 PM ET access check, no final gamebook was recovered from the NFL game center.
The [manual tracking plan](../usage-tracking.md#september-9-nesea-queue-refresh) preserves the open
film and participation questions and explicitly excludes unavailable players from comparisons.
This is an access finding, not proof that an attachment cannot exist elsewhere.

## Sources

- Original club biographies — dynamic; retrieved September 9, 2026; individual URLs and hashes in
  [biography provenance](../research/ne-sea/audit/official-biography-provenance.csv).
- NFL play-by-play, FTN Data, PFR and NFL NGS via nflverse — historical 2025 snapshots retrieved
  September 9; exact URLs, hashes, definitions and license in the [audit methods](../research/ne-sea/audit/README.md).
- Evan Lazar, Patriots.com — [How Patriots QB Drake Maye can be even better in his third NFL season](https://www.patriots.com/news/how-patriots-qb-drake-maye-can-be-even-better-in-his-third-nfl-season) — September 8, 2026; reused original analysis, checked September 9.
- Patriots.com — [Week 1 inactives](https://www.patriots.com/news/week-1-inactives-patriots-at-seahawks) — September 9, 2026, 6:50 PM ET; reused official eligibility evidence.
- NFL — [NE at SEA game center](https://www.nfl.com/games/patriots-at-seahawks-2026-reg-1) — discovery endpoint checked September 9 at approximately 8:50 PM ET; no final book recovered.

## Assessment

- Confidence: medium. Historical measurements are reproducible, but translating them to changed
  2026 personnel and coaching remains inference.
- Fact/inference boundary: counts and explicit source conflicts are evidence; matchup implications
  are interpretation. Two sources hosted by nflverse can have separate charting origins, while
  a team article quoting NGS and the NGS dataset share one origin.
- What would invalidate this: corrected source snapshots, materially different current protection
  or deployment, or a full film sample contradicting the inferred continuity.
- Next review: official final book/participation first; then chartable full-game assignments. Keep
  coverage, blocker attribution, snap pace and healthy backfield comparisons open until supported.
