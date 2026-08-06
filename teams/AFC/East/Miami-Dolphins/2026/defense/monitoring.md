---
schema_version: 1
record_id: rf-2026-mia-defense-monitoring-001
record_type: research_finding
title: "Miami Dolphins 2026 defensive monitoring framework"
team_ids: ["MIA"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-08-05
last_verified: 2026-08-05
confidence: medium
source_ids: ["local-source-miami-dolphins"]
supersedes: []
---

# Defensive monitoring framework

## Finding

Miami's defense must be updated from deployment and play-level evidence rather than labels, camp takeaways, or headline sack totals. The charting system should connect personnel, front, pressure, coverage, responsibility, and result.

## Evidence

The known personnel turnover, documented authority, multiple scheme menu, and open competitions identify the necessary fields below. They do not resolve the outcomes.

## Priority questions

| Priority | Question | Review trigger |
|---:|---|---|
| 1 | Where does Chris Johnson align in base and nickel? | every first-unit series |
| 1 | Can Miami pressure with four? | every opponent dropback |
| 1 | Who joins Robinson by down and package? | every edge substitution |
| 1 | Who plays the post, box, and nickel? | every defensive-back rotation |
| 2 | Can the front defend the run without routine safety support? | every first-unit run |
| 2 | Does Rodriguez earn nickel and two-minute work? | every linebacker package |
| 2 | Which coverage families lead by situation? | every chartable pass |
| 2 | Do simulated pressures create free rushers without coverage busts? | every pressure presentation |
| 3 | Which reserves earn stable rotational roles? | every substitution and special-teams phase |
| 3 | Are takeaways supported by repeatable disruption? | every turnover and near-turnover |

## Minimum chart fields

### Every snap

- date/game, quarter, down, distance, score, and offensive personnel;
- Miami personnel and substitutions;
- front family and box count;
- corner leverage and safety shell;
- motion response;
- play family and result.

### Pass plays

- rush count and pressure type;
- rusher alignments and games;
- coverage family when identifiable;
- first pressure, time to pressure, and finishing player;
- target area, primary coverage defender, separation, and result;
- explosive, pass breakup, turnover-worthy opportunity, and actual takeaway.

### Run plays

- concept, direction, intended gap, and quarterback read;
- initial fit defender and support player;
- edge-set and interior-control result;
- first contact and yards before contact;
- missed tackle, explosive, and situational success.

## Evidence hierarchy

1. Regular-season all-22 or clear broadcast evidence against starters.
2. Preseason first-unit snaps with identifiable assignments.
3. Repeated, independently corroborated practice deployment.
4. Coach and player statements about roles and rules.
5. Isolated camp wins, takeaways, and team-produced highlights.

## Update rules

- Move a hypothesis only with repeated evidence and record the sample.
- Do not call a role settled from a nominal depth-chart label.
- Do not call pressure effective from sacks alone.
- Do not call coverage strong from interceptions alone.
- Treat package concentration and raw snap share separately.
- Preserve dated preseason observations in [`../preseason/evidence-log.csv`](../preseason/evidence-log.csv).

## Fantasy implication

The framework should translate defensive evidence into D/ST streaming decisions, IDP snap projections, and opponent position adjustments without converting volatile turnovers into permanent skill assumptions.

## Sources

- Miami Dolphins — [DC Sean Duggan press conference](https://www.miamidolphins.com/news/transcript-dc-sean-duggan-press-conference-jun-4) — published 2026-06-04.
- Miami Dolphins — [HC Jeff Hafley press conference](https://www.miamidolphins.com/news/transcript-hc-jeff-hafley-press-conference-august-2) — published 2026-08-02.

## Assessment

- Confidence: medium that these are the correct measurements; defensive conclusions remain open.
- Fact/inference boundary: current questions follow from documented roles and turnover. Thresholds require game evidence.
- What would invalidate this: a major authority, roster, or reporting-access change that requires different fields.
- Next review: immediately after the first preseason game.
