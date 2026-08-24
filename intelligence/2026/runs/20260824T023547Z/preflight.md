# Preseason Game Preflight

## Run Scope

- Run ID: `20260824T023547Z`
- Games: Giants at Dolphins; Bears at Bengals; Eagles at Patriots
- Teams: `NYG`; `MIA`; `CHI`; `CIN`; `PHI`; `NE`
- Season: 2026
- Planned pass: `immediate`
- Planned retrieval window: `2026-08-22T16:00:00Z` through `2026-08-24T02:35:47Z`
- Assignment owner: ARCHITECT

## Source Readiness

| Check | Status | Evidence or link | Notes |
|---|---|---|---|
| Official team recap is timestamped and inside window | `ready` | NYG, CHI, PHI, and NE official postgame coverage | Miami and Cincinnati did not expose compliant team-side postgame recaps. |
| Official inactive or held-out-starter context is available | `ready` | Team postgame reports | Dart sat; Chicago starters played limited action; New England rested starters. |
| NFL game center or official gamebook is available | `ready` | NFL game centers and NE gamebook | Final scores and basic game context are available. |
| Participation, snap, route, carry, or target data is available | `not_ready` |  | Do not resolve role shares from the box score or drive summaries. |
| Independent postgame notebook is timestamped | `not_ready` |  | This bounded pass uses official or team-controlled sources only. |

## Pass Decision

- Proceed / wait: Proceed with all three games and preserve source-gap outcomes for MIA and CIN.
- Reason: Four team sources contain sufficient official availability or bounded unit context. The
  missing Miami and Cincinnati surfaces are themselves valid intake results.
- Observation cap: 20 per team.
- Sources to include: registered official team sources and game-specific official records.
- Sources to exclude: live social reactions, unsupported snap estimates, and opponent reporting as
  substitute team provenance.
- Questions explicitly in scope: starter participation, quarterback allocation, material injury
  status, and bounded reserve-unit production.
- Questions explicitly out of scope: stable role promotion without measured participation and
  first-team conclusions from reserve-on-reserve results.

## Timing Rules

- Ja'Quinden Jackson's hospital evaluation is logged as official same-night availability evidence;
  a diagnosis or roster consequence requires a new source.
- Miami and Cincinnati remain eligible for completion only if a timestamped notebook or official
  participation record adds material context.
