# Preseason Game Preflight

## Run Scope

- Run ID: `20260823T035847Z`
- Game: open-ledger preseason Week 2 completion batch
- Teams: `DEN`; `CAR`; `WAS`; `DET`; `GB`; `JAX`; `NO`; `ARI`; `SF`
- Season: 2026
- Planned pass: `completion`
- Planned retrieval window: wait to freeze until gamebook, participation, snap/route, or
  independent postgame evidence is available for the target triggers
- Assignment owner: ARCHITECT

## Source Readiness

| Check | Status | Evidence or link | Notes |
|---|---|---|---|
| Official team recap is timestamped and inside window | `mixed` | Existing syntheses have official recaps for DEN, WAS, DET, CAR, NO, LAR, and SF-side 49ers/Chargers. | GB and JAX had stale or noncompliant official surfaces in the prior run. |
| Official inactive or held-out-starter list is available | `mixed` | WAS and CAR had held-out/inactive context in prior syntheses. | Other teams require recheck before assignment freeze. |
| NFL game center or official gamebook is available | `not_ready` | Prior run reports repeatedly found no exposed gamebook or participation report. | This is the key completion-pass gate. |
| Participation, snap, route, carry, or target data is available | `not_ready` |  | No measured snap/route data has been admitted into current repo evidence for these triggers. |
| Independent postgame notebook or beat report is timestamped | `mixed` | SF had NBC/Maiocco coverage; several 20260822 teams lacked attributable independent in-window items. | Recheck team-by-team before freezing assignments. |
| Film or charting source is available for role/pressure questions | `not_ready` |  | Required for WAS/DET pressure-front and many role conclusions. |

## Open Ledger Triggers

| Team | Ledger ID | Trigger | Ready now? | Assignment impact |
|---|---|---|---|---|
| DEN | `til-2026-den-20260822-001` | Next practice/game availability plus designed movement, scramble behavior, and full first-team operation for Bo Nix. | `no` | Need later practice/game or charting evidence. |
| DEN | `til-2026-den-20260822-002` | First-team routes, targets, alignments, and first-read charting for Jaylen Waddle relative to Sutton, Mims, and Engram. | `no` | Completion pass should include measured routes/targets if available. |
| DEN | `til-2026-den-20260822-003` | First-team early-down, passing-down, two-minute, and goal-line work for Dobbins, Harvey, and Coleman. | `no` | Completion pass should include backfield snap/route/carry charting. |
| CAR | `til-2026-car-20260822-001` | Next healthy-backfield opening drive, inside-5 work, routes, and two-minute snaps. | `no` | Hubbard absence made prior sample incomplete; wait for healthy-unit evidence. |
| CAR | `til-2026-car-20260822-002` | First-unit routes, target order, and red-zone usage with Coker and Legette available. | `no` | Need full receiving-room context. |
| CAR | `til-2026-car-20260822-003` | Waller first practice, final roster status, and early regular-season routes/red-zone/third-down usage. | `partial` | Availability check may be ready before route evidence; keep scope narrow. |
| WAS | `til-2026-was-20260822-001` | Gamebook or film pressure chart, first-team edge snaps, and four-man-versus-blitz results. | `no` | Do not rerun until pressure charting or participation is available. |
| DET | `til-2026-det-20260822-001` | Edge snaps, third-down rush packages, alignments, and pressures alongside Hutchinson. | `no` | Do not rerun until rush-package or pressure evidence is available. |
| NO | `til-2026-no-20260821-001` | Final preseason personnel grouping, routes, and targets for Bryce Lance. | `no` | Needs final-preseason route/personnel evidence. |
| NO | `til-2026-no-20260821-002` | Official Cesar Ruiz status and next first-team right guard rotation. | `partial` | Status check may be ready before rotation evidence. |
| NO | `til-2026-no-20260821-003` | Healthy-backfield snaps, routes, two-minute work, and goal-line usage. | `no` | Requires measured usage or clear first-team reporting. |
| ARI | `til-2026-ari-20260821-001` | Josh Sweat official activation, practice participation, and Week 1 status. | `no` | Primarily Week 1/roster-status trigger, not a completed game trigger yet. |
| ARI | `til-2026-ari-20260821-002` | Tip Reiman first Week 1 injury report and official game status. | `no` | Week 1 injury report not expected yet. |
| ARI | `til-2026-ari-20260821-003` | Jeremiyah Love return to practice, final depth chart, and Week 1 status. | `partial` | Practice/status check may be ready; final depth chart and Week 1 status likely not. |
| SF | `til-2026-sf-20260821-001` | De'Zhaun Stribling route participation, snaps by quarterback unit, and red-zone usage. | `no` | Need charted route/QB-unit usage, not more box-score production. |
| GB | source gap | Prior GB synthesis produced zero compliant Packers observations. | `no` | Include only if official recap/gamebook/participation data is now fresh and timestamped. |
| JAX | source gap | Prior JAX synthesis produced zero compliant Jaguars observations. | `no` | Include only if timestamped recap, participation report, or snap split is now available. |

## Pass Decision

- Proceed / wait: `wait`
- Reason: The open items mostly require completion-pass evidence that the existing validated runs
  explicitly lacked: gamebook/participation records, snap or route data, first-team unit context,
  pressure charting, or later practice/Week 1 status. Freezing assignments now would likely
  reproduce the same no-new-material reports.
- Observation cap: 20 per team when assignments are frozen.
- Sources to include: official team communications, NFL gamebooks, free-access beat reporting,
  and data/film sources from each team source registry that can directly answer the listed trigger.
- Sources to exclude: generic game recaps, highlights, or opponent-side reports that do not expose
  the target team's role, availability, snap, route, pressure, or participation evidence.
- Questions explicitly in scope:
  - `den-off-qb-001`; `den-off-wr-001`; `den-off-rb-001`
  - `car-2026-off-q03`; `car-2026-off-q04`; `car-2026-off-q05`
  - `was-def-001`
  - `det-def-001`
  - `no-2026-off-q03`; `no-2026-off-q04`; `no-2026-off-q05`; `no-2026-off-q07`
  - `ari-def-003`; `rf-2026-ari-backfield-target-hierarchy-001`; `ari-off-001`
  - `sf-off-rookie-001`; `sf-off-wr-001`
  - GB/JAX active P1 triggers only if source freshness resolves the prior zero-observation gap
- Questions explicitly out of scope: new broad game coverage for unrelated teams; stable role
  promotion from isolated highlights; duplicate checks of already captured observations.

## Timing Rules

- Immediate status checks can be run for CAR/Waller, NO/Ruiz, and ARI/Love if official status
  changes appear.
- Full completion assignments should wait for gamebook/participation, snap/route data, or
  timestamped independent notebooks.
- If a trigger has not occurred, leave the existing ledger row open and do not create a duplicate
  ledger target.

## Recommended Assignment Order

1. **Status-only mini-check:** CAR/Waller, NO/Ruiz, ARI/Love.
2. **Measured-usage batch:** DEN, CAR, NO, SF after routes/snaps/carries become available.
3. **Pressure/defense batch:** WAS and DET after pressure charting or participation evidence is
   available.
4. **Source-gap retry:** GB and JAX only after official recap/gamebook freshness is confirmed.
