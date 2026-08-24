# 2026 Preseason Week 2 Coverage Audit

This audit compares the official 2026 preseason Week 2 schedule against completed FFB intelligence
runs. It is current as of the Saturday B run on 2026-08-24 UTC. Use it to choose the next
reader batches before starting Week 3.

## Schedule Source

- NFL preseason Week 2 schedule page lists 16 games from Thursday, August 20 through Sunday,
  August 23, 2026.
- NFL Week 2 preview page lists the same 16-game preseason slate and confirms kickoff times.
- SEA/TEN is scheduled for Sunday, August 23, 2026 at 8:00 PM ET and had not produced postgame
  evidence when `intelligence/2026/runs/20260823T034234Z/preflight.md` was created.

## Coverage Matrix

| Game | Kickoff | Repo coverage | Status | Next action |
|---|---:|---|---|---|
| Raiders at Texans | Thu Aug 20, 8:00 PM ET | none found | not processed | Create immediate/completion pass if postgame evidence is now available. |
| 49ers at Chargers | Thu Aug 20, 10:00 PM ET | `20260821T191126Z` SF synthesis only | partially processed | Decide whether LAC side needs BOLT-scoped pass; SF has open Stribling follow-up. |
| Jets at Steelers | Fri Aug 21, 7:00 PM ET | none found | not processed | Create immediate/completion pass if evidence is available. |
| Panthers at Jaguars | Fri Aug 21, 7:30 PM ET | `20260822T232931Z` CAR/JAX | processed with source gaps | CAR has three open review rows; JAX had zero compliant observations and needs completion if source freshness improves. |
| Packers at Broncos | Fri Aug 21, 9:00 PM ET | `20260822T232931Z` GB/DEN | processed with source gaps | DEN has three open review rows; GB had zero compliant observations and needs completion if source freshness improves. |
| Commanders at Lions | Sat Aug 22, 12:00 PM ET | `20260822T232931Z` WAS/DET | processed with deferred rows | WAS and DET each have one open defensive review row. |
| Bills at Browns | Sat Aug 22, 1:00 PM ET | `20260824T022813Z` BUF/CLE | processed | Reserve-context log; Cleveland starter decision remains an official-announcement trigger. |
| Falcons at Colts | Sat Aug 22, 1:00 PM ET | `20260824T022813Z` ATL/IND | processed | Both teams rested starters; no canonical role promotion. |
| Ravens at Vikings | Sat Aug 22, 1:00 PM ET | `20260824T022813Z` BAL/MIN | processed with MIN source gap | Baltimore log-only reserve evidence; retry Minnesota only if a compliant postgame source appears. |
| Saints at Rams | Sat Aug 22, 4:00 PM ET | `20260822T232931Z` NO/LAR | processed with deferred rows | NO older rows remain open; LAR had log-only reserve evidence. |
| Giants at Dolphins | Sat Aug 22, 4:00 PM ET | `20260824T023547Z` NYG/MIA | processed with MIA source gap | NYG log-only bounded usage; retry Miami only if compliant postgame participation appears. |
| Bears at Bengals | Sat Aug 22, 7:00 PM ET | `20260824T023547Z` CHI/CIN | processed with CIN source gap | CHI one-drive log; retry Cincinnati only if compliant postgame participation appears. |
| Eagles at Patriots | Sat Aug 22, 7:00 PM ET | `20260824T023547Z` PHI/NE | processed | PHI injury follow-up requires a diagnosis; NE starters rested. |
| Chiefs at Buccaneers | Sat Aug 22, 7:30 PM ET | none found | not processed | Create immediate/completion pass if evidence is available. |
| Cowboys at Cardinals | Sat Aug 22, 10:00 PM ET | ARI pregame/follow-up only; no Cowboys/Cardinals game synthesis | not processed as game | Create completion pass if Cardinals availability or Cowboys role evidence is available. |
| Seahawks at Titans | Sun Aug 23, 8:00 PM ET | `20260823T034234Z` preflight only | not yet played at preflight | Freeze assignments after postgame evidence exists. |

## Processed Runs

- `20260821T191126Z`: SF/NO/ARI pilot. Useful for SF side of 49ers-Chargers and pregame/follow-up
  context for NO and ARI, but not a full Week 2 game coverage run for all opponents.
- `20260821T205355Z`: trigger follow-up for SF/NO/ARI open rows.
- `20260821T212335Z`: MIN Jefferson-specific intake. This does not count as Ravens-Vikings game
  coverage.
- `20260822T232931Z`: four-game pilot for NO/LAR, GB/DEN, WAS/DET, and CAR/JAX.
- `20260823T034234Z`: SEA/TEN preflight only; assignments intentionally not frozen.
- `20260824T022813Z`: immediate pass for BUF/CLE, ATL/IND, and BAL/MIN; SEA/TEN remained live at
  assignment freeze and stayed queued.
- `20260824T023547Z`: immediate pass for NYG/MIA, CHI/CIN, and PHI/NE; Miami and Cincinnati had
  valid zero-observation source gaps.

## Immediate Gaps

Highest-priority uncovered completed games:

1. Raiders at Texans
2. Jets at Steelers
3. Chiefs at Buccaneers
4. Cowboys at Cardinals
5. Seahawks at Titans

Partial coverage gaps:

1. Chargers side of 49ers at Chargers.
2. Cardinals game-side evidence from Cowboys at Cardinals, separate from earlier ARI availability
   monitoring.
3. Miami and Cincinnati postgame team-side participation, if compliant sources appear.

## Recommended Next Batch

Do not attempt all gaps in one run. Use the preseason runbook and batch by fantasy relevance plus
source availability:

1. **Open-ledger completion batch:** DEN, CAR, WAS, DET, GB, JAX, NO, ARI, SF.
2. **Completed Saturday batch A:** Bills/Browns, Falcons/Colts, Ravens/Vikings.
3. **Remaining Saturday batch:** Chiefs/Buccaneers and Cowboys/Cardinals.
4. **Thursday/Friday uncovered batch:** Raiders/Texans, Jets/Steelers, and Chargers side of
   49ers/Chargers.
5. **SEA/TEN immediate pass:** run only after official or timestamped postgame evidence exists.

For every new batch, start with `templates/preseason-game-preflight.txt`, freeze assignments only
when evidence is ready, and preserve zero-observation outcomes when source freshness is the real
finding.
