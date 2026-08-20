---
schema_version: 1
record_id: rf-2026-league-adp-baseline-002
record_type: research_finding
title: "Slot-10 availability windows — corrected draft board for 2026-08-21"
team_ids: []
player_ids: ["local-player-james-cook-2022", "local-player-josh-allen-2018"]
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-20
last_verified: 2026-08-20
confidence: medium
source_ids: ["ffc-2026-adp-api", "espn-2026-fantasy-api"]
supersedes: ["rf-2026-league-adp-baseline-001"]
---

# Finding: the "fallback tier at 15" named in the prior baseline is a 35 percent proposition, and Josh Allen is a coin flip at 34

## Scope

- Area: availability windows at slot 10 (picks 10, 15, 34, 39, 58, 63) for the
  2026-08-21 Gridiron Guru's Only draft
- Data: `2026-08-19-ffc-12team-ppr.csv` (266 players, 6,885 real 12-team PPR drafts,
  sampled 2026-08-12 to 2026-08-19). The underlying snapshot CSVs are unchanged and
  remain the data of record; this supersedes only the *analysis* in
  `rf-2026-league-adp-baseline-001`.
- Method: each player's draft position modeled as normal(ADP, stdev) from the FFC
  sample; availability at pick *n* is P(draft position > n). This is an approximation —
  real draft positions are right-skewed and bounded — so treat the middle of the range
  as more reliable than the tails.

## Finding

The prior baseline's data was sound and its headline conclusion holds: **at pick 10 the
elite skill tier is effectively guaranteed** — there is a 96 percent chance at least
one of Drake London, De'Von Achane, CeeDee Lamb, or Justin Jefferson is on the board.

Two of its downstream claims do not survive the arithmetic.

**Correction 1 — Cook and Chase Brown are not a "fallback tier at 15."** James Cook is
13 percent to last to pick 15 and Chase Brown 25 percent; the chance that *either* is
available is **35 percent**. Planning around them at 15 is planning around a coin flip
that lands wrong two times in three. The genuinely reliable pick-15 tier is Derrick
Henry (79 percent), A.J. Brown (76 percent), George Pickens (92 percent), and Saquon
Barkley (91 percent) — at least one of those four is a **100 percent** proposition.

**Correction 2 — Josh Allen is not reliably available at 34.** The prior record
suggested taking elite skill at 10 and 15 and the first quarterback at 34. That works
for the *tier-2* quarterbacks (Maye 99 percent at 34, Burrow and Jackson 100 percent).
It does not work for Allen specifically: he is **40 percent at pick 34 and 20 percent
at 39**, with an unusually wide stdev of 8.3 that reflects a market with no consensus on
him. Anyone who wants Allen in particular is choosing between taking him at 15 (98
percent) and accepting roughly even odds at 34.

## Evidence

Availability at picks 10 and 15, FFC 12-team PPR:

| Player | Pos | ADP | stdev | @10 | @15 |
|---|---|---|---|---|---|
| Jonathan Taylor | RB | 7.4 | 1.8 | 4% | 0% |
| Drake London | WR | 10.1 | 1.6 | 40% | 0% |
| De'Von Achane | RB | 10.2 | 1.9 | 44% | 0% |
| CeeDee Lamb | WR | 10.7 | 2.0 | 54% | 1% |
| Justin Jefferson | WR | 11.8 | 2.2 | 72% | 5% |
| **James Cook III** | RB | 12.3 | 2.8 | **74%** | **13%** |
| Chase Brown | RB | 13.7 | 2.7 | 88% | 25% |
| Rashee Rice | WR | 14.8 | 2.2 | 97% | 38% |
| Ashton Jeanty | RB | 15.3 | 3.0 | 95% | 47% |
| Derrick Henry | RB | 17.6 | 2.6 | 100% | 79% |
| A.J. Brown | WR | 17.7 | 3.1 | 99% | 76% |
| George Pickens | WR | 19.5 | 2.8 | 100% | 92% |
| Saquon Barkley | RB | 20.3 | 3.5 | 100% | 91% |
| Nico Collins | WR | 21.2 | 2.7 | 100% | 98% |

Quarterback windows:

| Player | ADP | stdev | @15 | @34 | @39 |
|---|---|---|---|---|---|
| Josh Allen | 32.5 | 8.3 | 98% | **40%** | 20% |
| Drake Maye | 50.5 | 6.6 | 100% | 99% | 95% |
| Joe Burrow | 56.0 | 8.1 | 100% | 100% | 98% |
| Lamar Jackson | 56.8 | 7.4 | 100% | 100% | 99% |
| Dak Prescott | 65.8 | 8.3 | 100% | 100% | 100% |
| Jayden Daniels | 72.9 | 9.9 | 100% | 100% | 100% |

Joint probabilities:

- At least one of London / Achane / Lamb / Jefferson at pick 10: **96 percent**
- At least one of Cook / Chase Brown at pick 15: **35 percent**
- At least one of Henry / A.J. Brown / Pickens / Barkley at pick 15: **100 percent**

## Fantasy implication

- **Pick 10 is a genuine choice, not a scramble.** The elite tier will be there. The
  question is which member, and that is a valuation question rather than an
  availability one.
- **Do not treat Cook as deferrable.** At 74 percent available at 10 and 13 percent at
  15, pick 10 is the price of admission if he is wanted. This is the specific error the
  prior record encouraged.
- **Pick 15 should be planned around the reliable tier**, not the coin-flip tier. Enter
  the pick expecting Henry, A.J. Brown, Pickens, or Barkley and treat Cook, Chase Brown,
  Rice, or Jeanty falling as upside.
- **The Allen decision is a 15-or-34 fork, not a 34 plan.** Given this league's scoring
  and the finding that Allen's format floor is roughly 26.5 points per game even in his
  worst passing season in six years, taking him at 15 is defensible on value; waiting to
  34 is a live gamble at even odds. Tier-2 quarterbacks are genuinely safe to wait on.
  See [Buffalo's passing-volume decline](../../../teams/AFC/East/Buffalo-Bills/2026/offense/passing-volume-decline.md)
  and the [Josh Allen profile](../../../players/josh-allen/profile.md).
- **Roster-construction reminder:** Allen and Cook draw scoring from the same goal-line
  snaps. Rostering both concentrates rather than diversifies that exposure. See
  [red zone and touchdown share](../../../teams/AFC/East/Buffalo-Bills/2026/offense/red-zone-and-touchdown-share.md).
- The prior record's room-behavior caveat still stands and is reinforced: ESPN sorts by
  league-scoring projections, so quarterbacks will appear at the top of league-mates'
  lists. Allen's 8.3 stdev is direct evidence that the market has not settled him.

## Assessment

- Confidence: medium
- Reason: the sample is large (6,885 drafts) and current, but a normal approximation
  overstates tail precision, FFC's public drafts are not this league's room, and the
  data predates the draft by two days.
- Fact/inference boundary: the ADP, stdev, high, and low values are facts from the
  snapshot. The probabilities are modeled estimates, and the roster-construction advice
  is inference.
- What would invalidate this: this league's actual draft behavior diverging from public
  PPR drafts, which is likely to some degree given ESPN's projection sort in a 6-point
  passing-touchdown format. Two or more quarterbacks off the board before pick 30 is the
  signal that the room is not drafting neutrally.
- Next review: after the 2026-08-21 draft, score these windows against what actually
  happened and record the room's tendencies for 2027.

## Correction log

- 2026-08-20 — supersedes `rf-2026-league-adp-baseline-001`. That record described
  Cook and Chase Brown as "the fallback tier at 15" (35 percent) and implied Allen was
  a reliable pick-34 target (40 percent). Both are corrected above. The 08-19 snapshot
  CSVs are unchanged and remain the data of record; only the analysis is replaced.

## Sources

- `league/rankings/adp/2026-08-19-ffc-12team-ppr.csv` — Fantasy Football Calculator public API, 6,885 12-team PPR drafts sampled 2026-08-12 to 2026-08-19.
- `league/rankings/adp/2026-08-19-espn-adp.csv` — ESPN fantasy read API, default ranks and live ADP.
- League format: [Gridiron Guru's Only 2026](../../scoring-formats/gridiron-gurus-only-2026.md).
