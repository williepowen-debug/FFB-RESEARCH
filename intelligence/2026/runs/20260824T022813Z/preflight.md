# Preseason Game Preflight

## Run Scope

- Run ID: `20260824T022813Z`
- Games: Bills at Browns; Falcons at Colts; Ravens at Vikings; Seahawks at Titans
- Teams: `BUF`; `CLE`; `ATL`; `IND`; `BAL`; `MIN`; `SEA`; `TEN`
- Season: 2026
- Planned pass: `immediate`
- Planned retrieval window: `2026-08-22T16:00:00Z` through `2026-08-24T02:28:13Z`
- Assignment owner: ARCHITECT

## Source Readiness

| Check | Status | Evidence or link | Notes |
|---|---|---|---|
| Official team recap is timestamped and inside window | `ready` | BUF, CLE, ATL, IND, and BAL official recaps | Minnesota's official postgame surface did not expose a fresh recap. |
| Official inactive or held-out-starter context is available | `ready` | Team postgame reports | All three Saturday games rested most or all starters. |
| NFL game center or official gamebook is available | `ready` | NFL game centers | Final score and box-score context are available; downloadable participation books remain inconsistent. |
| Participation, snap, route, carry, or target data is available | `not_ready` |  | Do not resolve role shares from these games. |
| Independent postgame notebook is timestamped | `not_ready` |  | This bounded pass uses official/team-controlled sources only. |
| SEA/TEN final postgame evidence is available | `not_ready` | NFL game center | At freeze time the game center still showed Q3 10:43 and no timestamped final recap. |

## Pass Decision

- Proceed / wait: Proceed for BUF/CLE, ATL/IND, and BAL/MIN; wait for SEA/TEN.
- Reason: The three Saturday games have final official context sufficient for bounded held-out and
  reserve-unit logging. SEA/TEN was still live and cannot enter an immutable postgame batch.
- Observation cap: 20 per team.
- Sources to include: registered official team sources and game-specific official records.
- Sources to exclude: live social reactions, highlights without unit context, and unsupported snap
  or route estimates.
- Questions explicitly in scope: starter participation, quarterback allocation, reserve-unit
  performance, and material availability news.
- Questions explicitly out of scope: stable role promotion from reserve production and any
  route-share, pressure-rate, or backfield conclusion without measured participation.

## Timing Rules

- SEA/TEN remains queued for a separate postgame pass after a final recap and injury update exist.
- Saturday-game reserve production routes to `log` unless it changes an existing availability or
  roster decision.
