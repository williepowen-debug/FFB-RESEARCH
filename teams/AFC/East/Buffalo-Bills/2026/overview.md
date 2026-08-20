---
schema_version: 1
record_id: to-2026-buf-overview-001
record_type: team_overview
title: "Buffalo Bills — 2026 Coaching Succession and Skill-Group Upgrade"
team_ids: ["BUF"]
player_ids: ["local-player-james-cook-2022"]
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-20
last_verified: 2026-08-20
confidence: high
source_ids: ["local-source-buffalo-bills", "local-source-cbs-sports", "local-source-espn", "local-source-si-bills-central"]
supersedes: []
---

# Buffalo Bills — 2026 Coaching Succession and Skill-Group Upgrade

- Conference/division: AFC East
- Last verified: 2026-08-20
- Scope: changes from the 2025 team to the 2026 preseason roster and staff, through the 2026-08-15 preseason opener
- Build tier: Core, deepened with a preseason depth chart, a beat-writer registry, and a canonical player profile

Buffalo made a coaching change without a roster reset. Head coach Sean McDermott was dismissed after nine seasons and offensive coordinator Joe Brady was promoted to head coach, while general manager Brandon Beane and quarterback Josh Allen stayed in place. The Bills then upgraded the skill group — trading for wide receiver DJ Moore — and reworked the defensive staff and secondary. This is continuity with a targeted upgrade, the structural opposite of the Miami Dolphins' 2026 regime-and-roster reset in the same division.

The supporting machine-readable files are:

- [Leadership transition](coaching-staff/leadership-transition.csv)
- [2026 coaching staff](coaching-staff/staff.csv)
- [Coaching intelligence module](coaching-staff/README.md)
- [Offensive ecosystem module](offense/README.md)
- [Offensive hypotheses](offense/hypotheses.csv)
- [Defensive ecosystem module](defense/README.md)
- [Defensive hypotheses](defense/hypotheses.csv)
- [Veteran additions](roster/veteran-additions.csv)
- [Departures](roster/departures.csv)
- [Retentions and extensions](roster/retentions.csv)
- [2026 draft class](roster/draft-class.csv)
- [Preseason depth chart — 2026-08-20](preseason/depth-charts/2026-08-20-unofficial.md)
- [Source and beat-writer registry](beat-writers/registry.md)

## Fantasy-relevant snapshot

### Confirmed baseline

- Sean McDermott was fired after a 33-30 overtime wild-card loss to Denver; Joe Brady was promoted from offensive coordinator to head coach on 2026-01-27 (five-year deal). GM Brandon Beane remains.
- New coordinators: Pete Carmichael (offense) and Jim Leonhard (defense), both from Denver, plus special-teams coordinator Jeff Rodgers. Brady is reported to keep offensive play-calling.
- Josh Allen returns at quarterback; James Cook returns as the lead back.
- Buffalo traded for wide receiver DJ Moore (from Chicago), reuniting him with Brady from Carolina, and re-signed tight end Dawson Knox through 2028.
- The Bills added edge Bradley Chubb (from Miami), safeties C.J. Gardner-Johnson and Geno Stone, and corner Dee Alford; they traded nickel Taron Johnson and released safety Taylor Rapp.
- Interior offensive-line continuity was retained (Connor McGovern re-signed, O'Cyrus Torrence extended); 2025 left guard David Edwards departed, opening a competition.
- Buffalo made 10 draft selections, weighted toward the secondary and front seven.

### Working fantasy hypotheses

These are projections to test, not established 2026 outcomes:

- Josh Allen's environment is stable-to-improved: same play-caller, upgraded perimeter target. His floor and ceiling are the least uncertain in the division.
- DJ Moore is the clearest projected WR1, but Buffalo has distributed targets under Brady; the hierarchy below Moore is a committee to chart.
- James Cook remains the backfield anchor. Carmichael has since stated an intent to *expand* Cook's receiving usage, which is the largest open swing in his value; Allen's goal-line rushing still caps the touchdown ceiling, but less tightly than the 2023 baseline implies.
- The defense's coverage identity and rebuilt secondary roles are unestablished, creating early-season variance.

### Preseason updates through 2026-08-20

One preseason game has been played (2026-08-15, a 29-14 win over Carolina at the new
Highmark Stadium); the second is 2026-08-22 at Cleveland.

- Joe Brady is confirmed as the offensive play-caller. Pete Carmichael is testing the
  booth in one preseason game and the sideline in the other, and prepares as the backup
  caller.
- Offensive starters played two possessions and 15 snaps in the opener, scoring on both.
- Center Connor McGovern has been out since 2026-08-08 with a lower-body injury
  (reported two-to-four weeks); he is targeting Week 1 and Lloyd Cushenberry started in
  his place. Left guard is unresolved between Alec Anderson (first team) and Austin
  Corbett.
- No running back was added by trade, draft, or free agency; the room is Cook, Ray
  Davis, Ty Johnson, and Frank Gore Jr.

## Offensive identity

### Confirmed changes

The offensive system carries forward under its former designer. The additions are DJ Moore at receiver and Carmichael as coordinator; the quarterback (Allen), lead back (Cook), and interior line are largely continuous. Dawson Knox was re-signed to keep a blocking-and-red-zone tight end alongside Dalton Kincaid.

### Questions to resolve

- Whether Brady's head-coaching duties or Carmichael's influence change the 2025 offense.
- Whether Buffalo concentrates targets on Moore or keeps distributing across Shakir, Coleman, and Kincaid.
- Carmichael's effect on James Cook's passing-down usage.
- The left-guard competition after David Edwards's departure.

The durable offensive baseline, causal relationships, and fantasy translation are maintained in the [offensive ecosystem module](offense/README.md).

## Defensive matchup profile

### Confirmed changes

Buffalo changed defensive coordinators (Leonhard for Bobby Babich) and most defensive position coaches, kept its front-seven anchors (Ed Oliver, Greg Rousseau, Terrel Bernard, Matt Milano), added edge Bradley Chubb, and substantially reworked the secondary through the Taron Johnson trade, the Rapp release, veteran safety and corner signings, and three drafted defensive backs.

### Questions to resolve

- Leonhard's coverage and pressure identity.
- The nickel job vacated by Taron Johnson.
- The safety roles among Gardner-Johnson, Stone, and Cole Bishop.
- Whether Chubb produces healthy edge snaps opposite Rousseau.

These items affect opponent passing-game and pressure matchups, but no final schematic profile should be assigned before preseason and early-season evidence. The durable defensive baseline is maintained in the [defensive ecosystem module](defense/README.md).

## Coaching and scheme

Buffalo dismissed Sean McDermott and promoted Joe Brady to head coach on 2026-01-27. The coordinator changes were:

| Unit | 2025 | 2026 |
|---|---|---|
| Offense | Joe Brady | Pete Carmichael |
| Defense | Bobby Babich | Jim Leonhard |
| Special teams | Matthew Smiley | Jeff Rodgers |

Brady's promotion preserves offensive continuity because he was the incumbent designer and is reported to keep play-calling. The genuine variables are his expanded head-coaching workload, Carmichael's practical influence on the passing game and situational menus, and Leonhard's installation of a new defensive identity. The complete role-level staff and retention flags are in [staff.csv](coaching-staff/staff.csv); authority and coach profiles are in the [coaching intelligence module](coaching-staff/README.md).

### Analytical projection

The reasonable prior is a 2026 offense broadly continuous with 2025 and a defense whose identity is to-be-charted. Verify through preseason personnel groupings, target distribution, coverage shells, and pressure rates rather than offseason narratives.

## Special teams

Buffalo hired special-teams coordinator Jeff Rodgers and signed punter Mitch Wishnowsky, then drafted punter Tommy Doman Jr., setting up a punter competition. Safety Damar Hamlin was re-signed and contributes on special teams. Track the punter battle, return roles, and kicker operation through the preseason.

## Current depth chart

An offense-focused unofficial depth chart is maintained at
[preseason/depth-charts/2026-08-20-unofficial.md](preseason/depth-charts/2026-08-20-unofficial.md),
established after the preseason opener. Defensive and special-teams order are
deliberately uncharted in that record pending a verified two-deep.

## Canonical player profiles

- [James Cook](../../../../../players/james-cook/profile.md) — `local-player-james-cook-2022`

Do not duplicate full player biographies in this overview; link them here after stable
player IDs are verified.

## Open questions

As of 2026-08-20 the highest-leverage unknowns are:

1. Whether Cook's route participation and target rate actually rise, against a two-year
   32-33 reception baseline, now that Carmichael has stated the intent.
2. Whether McGovern returns for Week 1 and who holds left guard — the run game's
   blocking variable into the league's hardest early RB schedule.
3. The DJ Moore target share in a historically distributed offense.
4. Leonhard's defensive identity and the rebuilt secondary's roles.
5. Red-zone distribution between Allen and Cook, which moves before touchdown totals do.

Brady's retained play-calling and Cook's lead role are no longer open questions.

## Sources

- CBS Sports — [Bills promote Joe Brady to head coach, replacing Sean McDermott](https://www.cbssports.com/nfl/news/bills-joe-brady-head-coach-sean-mcdermott/) — published 2026-01-27.
- Buffalo Bills — [Buffalo Bills announce 2026 assistant coaching staff additions](https://www.buffalobills.com/news/buffalo-bills-announce-2026-assistant-coaching-staff-additions) — published 2026-02-17.
- Buffalo Bills — [Buffalo Bills free agency tracker 2026](https://www.buffalobills.com/news/buffalo-bills-free-agency-tracker-2026) — verified 2026-08-13.
- Buffalo Bills — [All 10 picks in the Buffalo Bills 2026 NFL Draft class](https://www.buffalobills.com/news/full-list-of-buffalo-bills-2026-nfl-draft-picks) — published 2026-04-25.
- ESPN — [Bills 2026 free agency tracker: offseason moves, signings](https://www.espn.com/nfl/story/_/id/48015515/bills-2026-free-agency-tracker-offseason-moves-signings-contract-trades) — verified 2026-08-13.
- Audacy / WGR 550 — [Bills announce 2026 coaching staff](https://www.audacy.com/wgr550/sports/bills/bills-announce-2026-coaching-staff) — verified 2026-08-13.
- ESPN — [Bills 29-14 Panthers (Aug 15, 2026) game recap](https://www.espn.com/nfl/recap/_/gameId/401873282) — published 2026-08-15, verified 2026-08-20.
- Sports Illustrated / Bills Central — [Everything preseason opener snap counts taught us about Joe Brady's Buffalo Bills](https://www.si.com/nfl/bills/onsi/preseason-everything-opener-snap-counts-taught-us-about-joe-brady-buffalo-bills-vs-panthers) — verified 2026-08-20.
- Two Bills Drive — [Buffalo Bills center Connor McGovern reveals goal return date from lower body injury](https://www.twobillsdrive.com/2026/08/17/buffalo-bills-center-connor-mcgovern-reveals-goal-return-date-from-lower-body-injury/) — published 2026-08-17, verified 2026-08-20.
