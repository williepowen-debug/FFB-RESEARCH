# 2026 Preseason Completion Queue

This queue is the current ledger-first starting point for the next preseason completion pass. It is
derived from open `intelligence-ledger.csv` rows and source-access gaps in the latest preseason
game pilot. The 15 rows from the August 24 audit were rechecked on August 25. Carolina's Waller
first-practice checkpoint was resolved as `no_change` and replaced by a narrower usage review, so
the total remains 15 open rows. See
`intelligence/2026/preseason-to-week-1-transition-audit-2026-08-25.md` for the phase-boundary
classification and `intelligence/2026/open-ledger-readiness-audit-2026-08-24.md` for the original
team-by-team evidence.

## Highest Priority

| Team | Reason | Required evidence | Source of queue item |
|---|---|---|---|
| DEN | Three open Week 2 review signals: Bo Nix mobility/availability, Jaylen Waddle target role, and RJ Harvey backfield package pressure. | Next practice and game availability; first-team routes, targets, alignments, first-read charting; early-down, passing-down, two-minute, and goal-line backfield usage. | `teams/AFC/West/Denver-Broncos/2026/intelligence-ledger.csv` |
| CAR | Three open reviews: Brooks/Hubbard backfield, McMillan receiving role, and Waller's post-first-practice usage. | Healthy-backfield opening drive, inside-5 work, routes, two-minute snaps; first-unit routes and target order with Coker/Legette; measured August 26 joint-practice or Week 1 routes, targets, red-zone usage, and third-down work for Waller. | `teams/NFC/South/Carolina-Panthers/2026/intelligence-ledger.csv` |
| WAS | Open pressure-front review from short-sample preseason defensive production. | Gamebook or film pressure chart; first-team edge snaps; four-man-versus-blitz results. | `teams/NFC/East/Washington-Commanders/2026/intelligence-ledger.csv` |
| DET | Open complementary-edge review after Wonnum/Moore splash plays. | Edge snaps, third-down rush packages, alignments, and pressures alongside Hutchinson. | `teams/NFC/North/Detroit-Lions/2026/intelligence-ledger.csv` |

## Source-Gap Follow-Up

| Team | Reason | Required evidence | Source of queue item |
|---|---|---|---|
| GB | Zero compliant observations in the Week 2 pilot because official listing and gamebook/participation evidence were not fresh. | Timestamped official recap, gamebook, participation data, and route/backfield/pressure/defensive-alignment charting. | `intelligence/2026/syntheses/2026-08-22/GB.md` |
| JAX | Source gap repaired on 2026-08-24; official recap established that primary starters were held out, so active role questions remain untested. | First-unit participation or film-based snap split; Hunter offensive usage, backfield allocation, tight-end packages, defensive front, and linebacker role evidence. | `intelligence/2026/syntheses/2026-08-24/JAX.md` |

## Older Open Preseason Rows

| Team | Reason | Required evidence | Source of queue item |
|---|---|---|---|
| NO | Open receiver, offensive-line, and backfield rows from the 2026-08-21 pilot remained unresolved after the Rams game immediate pass. | Final preseason personnel grouping, routes, targets; official Cesar Ruiz status and right-guard rotation; healthy-backfield snaps, routes, two-minute work, and goal-line usage. | `teams/NFC/South/New-Orleans-Saints/2026/intelligence-ledger.csv` |
| ARI | Open availability rows for Josh Sweat, Tip Reiman, and Jeremiyah Love. | Official activation/practice/Week 1 status for Sweat; Week 1 injury report and game status for Reiman; Love return to practice, final depth chart, and Week 1 status. | `teams/NFC/West/Arizona-Cardinals/2026/intelligence-ledger.csv` |
| SF | Open De'Zhaun Stribling role row. | Preseason route participation, snaps by quarterback unit, and red-zone usage. | `teams/NFC/West/San-Francisco-49ers/2026/intelligence-ledger.csv` |

## Next Run Shape

Use `PRESEASON_GAME_RUNBOOK.md` before starting the next pass:

1. Copy `templates/preseason-game-preflight.txt` into the new run directory as `preflight.md`.
2. Check whether the highest-priority teams have the required evidence available.
3. Freeze assignments around ready ledger triggers first.
4. Include `GB` only if source freshness or gamebook/participation data is now available; JAX's
   postgame source gap is repaired and now requires first-unit evidence.
5. Leave rows open when the named trigger has not occurred; do not duplicate a target already open
   in a team ledger.
