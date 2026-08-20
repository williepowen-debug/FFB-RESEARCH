---
schema_version: 1
record_id: rf-2026-league-buf-early-rb-sos-001
record_type: research_finding
title: "Validating Buffalo's hardest-early-RB-schedule flag against opponent run defenses"
team_ids: ["BUF", "HOU", "DET", "LAC", "NE", "LAR"]
player_ids: ["local-player-james-cook-2022"]
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-20
last_verified: 2026-08-20
confidence: medium
source_ids: ["local-source-nfl-com", "local-source-pff", "athlon-2026-fantasy-sos", "ffb-2026-schedule"]
supersedes: []
---

# Finding: the hardest-early-RB-schedule flag survives independent testing, and 2026 roster movement made the slate harder rather than easier

## Scope

- Area: validation of `early-season-sos.csv` (BUF RB early rank 1, average opponent
  rank 26.4) and watchlist `wl-2026-sos-buf-rb-001`
- Opponents tested: Weeks 1-5 — HOU (away), DET, LAC, NE (home), LAR (away)
- Season: 2026
- Status: active
- Last verified: 2026-08-20

## Finding

The existing strength-of-schedule flag was derived from prior-season *fantasy points
allowed*, a crude proxy that carries no information about 2026 roster change. Tested
against actual 2025 run-defense performance and 2026 front-seven movement, the flag
holds — and the offseason moved the slate in the wrong direction for James Cook.

**All five of Buffalo's first opponents were better than league average against the run
in 2025.** They allowed between 93.7 and 114.5 rushing yards per game, in a league whose
2025 range ran from 85.6 (Jacksonville, best) to 147.1 (Cincinnati, worst). The group
average was 105.2 yards per game at 4.24 yards per carry. For scale, Buffalo's own
defense allowed 136.2 per game at 5.1 — Cook will not face anything resembling the
unit he practices against.

**2026 movement made four of the five stronger up front.** Los Angeles traded for
reigning Defensive Player of the Year Myles Garrett and now holds PFF's top-ranked
defensive line. Houston, already the stingiest run defense of the group, returns its
edge duo and added interior help, with PFF placing it in the league's top three.
New England pairs Milton Williams and Christian Barmore — among the league's best
interior tandems — and added Dre'Mont Jones. Los Angeles added nose tackle Dalvin
Tomlinson and a first-round defensive lineman specifically to address the one weakness
in this group.

**The single exploitable spot is the Chargers' interior, in Week 3 at home.** Only one
projected Chargers interior starter graded above 65.0 in 2025, and that is the softest
front Buffalo sees before Week 6 — though Los Angeles spent the offseason trying to
fix precisely that.

## Evidence

### Facts

2025 rushing defense (17 games), from NFL.com team defense stats:

| Team | Week | Rush yds allowed | Per game | Yds/carry | Rush TD allowed |
|---|---|---|---|---|---|
| Houston | 1 (away) | 1,593 | 93.7 | 4.0 | 13 |
| New England | 4 (home) | 1,729 | 101.7 | 4.2 | 11 |
| LA Chargers | 3 (home) | 1,791 | 105.4 | 4.3 | 16 |
| LA Rams | 5 (away) | 1,884 | 110.8 | 4.3 | 8 |
| Detroit | 2 (home) | 1,947 | 114.5 | 4.4 | 16 |
| *Buffalo (reference)* | — | *2,315* | *136.2* | *5.1* | *24* |

- League context 2025: Jacksonville best at 85.6 rushing yards allowed per game,
  Cincinnati worst at 147.1.
- Buffalo's first-five average: 105.2 rushing yards allowed per game at 4.24 yards per
  carry — every opponent in the better half of the league.
- PFF 2026 defensive line rankings: the Rams lead the league; the Steelers and Texans
  round out the top three.
- Rams acquired Myles Garrett from Cleveland on 2026-06-01 for Jared Verse and multiple
  picks. Garrett is the reigning Defensive Player of the Year.
- Houston returns Will Anderson Jr. and Danielle Hunter (a combined 27 sacks and 45
  quarterback hits) and added Logan Hall, Kayden McDonald, Reed Blankenship, and
  Dominique Robinson; coverage expects Houston to be better against the run in 2026.
- New England's interior pairs Milton Williams and Christian Barmore, with Dre'Mont
  Jones added off the edge.
- Chargers: Khalil Mack posted an 80.7 PFF run-defense grade, but Teair Tart was the
  only projected interior starter above a 65.0 PFF grade. Los Angeles hired a new
  defensive coordinator, drafted Akheem Mesidor in round one, and signed nose tackle
  Dalvin Tomlinson.
- Detroit allowed the most rushing yards per game of the five (114.5) at the worst
  yards per carry (4.4), and this repository's Detroit record describes its
  complementary pass rush as being rebuilt around Hutchinson and Jack Campbell.
- Buffalo's Week 7 bye follows this stretch.

### Inferences

- The original flag was directionally right for the wrong reason. Prior-season fantasy
  points allowed happened to agree with actual run-defense quality here, but that is a
  coincidence of this particular slate, not a validation of the metric.
- Detroit in Week 2 and the Chargers in Week 3 — both at home — are the two most
  favorable spots in the opening stretch, and both are only *relatively* favorable.
- Because four of five fronts improved, the honest read is that Cook's Weeks 1-5
  efficiency risk is higher today than when the flag was written on 2026-08-17.
- This compounds with the interior-line churn documented in the Bills tree: a new
  center or left guard meets the strongest fronts on the calendar.

## Fantasy implication

- **The `avoid_early_panic` posture on Cook is confirmed and should be held more
  firmly, not less.** Poor Weeks 1-3 yardage is the expected outcome of this slate, not
  evidence of a role problem.
- Judge Cook on snap share, touch count, and goal-line involvement through Week 5.
  Yards per carry is the single noisiest signal available in this window.
- The buy-low window on Cook, if one opens, is most likely after Week 3 and before the
  Week 7 bye. A manager in this league holding Cook should expect to be offered less
  than his true value during that stretch.
- For opposing-defense streaming, Houston (Week 1) and the Rams (Week 5) are the
  premium spots against Buffalo's run game; both also carry top-three PFF defensive
  lines.
- This record does **not** revise Cook's season-long projection. It sharpens the
  distribution's front end.

## Assessment

- Confidence: medium
- Reason: the 2025 rushing-defense figures are official and internally consistent, and
  the 2026 personnel moves are documented. But 2025 team run-defense yardage is itself
  schedule- and game-script-dependent, and no 2026 snap has been played.
- Fact/inference boundary: the yardage table, the league range, the PFF rankings, and
  the roster moves are facts. The claim that the slate got *harder* is inference from
  personnel movement rather than from measured 2026 performance.
- Data-quality note: a StatMuse ranking table for the same season returned rank values
  inconsistent with its own yardage column and was discarded. The figures above come
  from NFL.com and were cross-checked against StatMuse's raw yardage, which agreed.
- What would invalidate this: 2026 run-defense performance diverging from these
  baselines in the first month, particularly Houston or the Rams proving soft against
  zone runs; or Buffalo's interior line settling early and Cook producing normally
  through the stretch.
- Next review: after Week 5, scoring these five opponents' actual run defense against
  the 2025 baselines recorded here.

## Repository gap identified

This is the first run-defense analysis of any kind in the repository. All 32 teams'
defensive records are built around pass rush and secondary, which means **RB matchup
questions currently have no durable evidence layer**. Recommend a league-wide
run-defense baseline table as a standing module rather than answering this per team,
per week.

## Sources

- NFL.com — [2025 NFL defense rushing stats by team](https://www.nfl.com/stats/team-stats/defense/rushing/2025/reg/all) — verified 2026-08-20.
- PFF — [2026 NFL defensive line rankings](https://www.pff.com/news/nfl-defensive-line-rankings-2026) — verified 2026-08-20.
- PFF — [2026 NFL season preview: strengths, concerns and breakout candidates for all 32 teams](https://www.pff.com/news/nfl-season-preview-all-32-teams) — verified 2026-08-20.
- StatMuse — [Rushing yards per game allowed by NFL defense, 2025](https://www.statmuse.com/nfl/ask/rushing-yards-per-game-allowed-by-nfl-defense-rankings-2025) — used only to cross-check raw yardage and to establish the league best/worst range; its rank column was internally inconsistent and was not used. Verified 2026-08-20.
- Internal: [`early-season-sos.csv`](../early-season-sos.csv), [`watchlists.csv`](../watchlists.csv), [`../../2026.csv`](../../2026.csv).
