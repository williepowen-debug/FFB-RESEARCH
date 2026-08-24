# Preseason Game Preflight

## Run Scope

- Run ID: `20260824T024317Z`
- Games: Chiefs at Buccaneers; Cowboys at Cardinals; Seahawks at Titans
- Teams: `KC`; `TB`; `DAL`; `ARI`; `SEA`; `TEN`
- Season: 2026
- Planned pass: `immediate`
- Planned retrieval window: `2026-08-22T16:00:00Z` through `2026-08-24T02:43:17Z`
- Assignment owner: ARCHITECT

## Source Readiness

| Check | Status | Evidence or link | Notes |
|---|---|---|---|
| Official team recap is timestamped and inside window | `ready` | KC, TB, and DAL official recaps | Arizona did not expose a compliant team-side recap. |
| Official inactive or held-out-starter context is available | `partial` | Tampa Bay and Dallas postgame coverage | Complete participation remains unavailable. |
| NFL game center or official gamebook is available | `partial` | Final KC/TB and DAL/ARI records | SEA/TEN was still live at assignment freeze. |
| Participation, snap, route, carry, or target data is available | `not_ready` |  | Do not resolve stable shares from recap statistics. |
| Independent postgame notebook is timestamped | `not_ready` |  | This pass uses official or team-controlled sources only. |
| SEA/TEN final postgame evidence is available | `not_ready` | NFL game center | The game remained live at 10:43 PM ET and was excluded from frozen assignments. |

## Pass Decision

- Proceed / wait: Proceed for KC/TB and DAL/ARI; wait for SEA/TEN.
- Reason: The two Saturday games have final official coverage sufficient for bounded unit and
  availability logging. A live Sunday game cannot enter the same immutable postgame batch.
- Observation cap: 20 per team.
- Sources to include: registered official team sources and final official game records.
- Sources to exclude: live social reaction, unsupported snap estimates, and opponent reporting as
  substitute team provenance.
- Questions explicitly in scope: starter exposure, backup-quarterback allocation, reserve skill
  production, first-unit pressure, and material injuries.
- Questions explicitly out of scope: stable role promotion without measured participation.

## Timing Rules

- SEA/TEN remains queued for a separate run after a final recap exists.
- Arizona remains eligible for completion only if a timestamped team-side postgame item or official
  participation record appears.
