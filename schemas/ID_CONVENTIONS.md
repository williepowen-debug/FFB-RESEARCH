# Stable Identifier Conventions

Identifiers are links between records, not labels. Once published, do not rename or reuse them.

## Record IDs

Format:

```text
<type-prefix>-<season-or-all>-<scope>-<slug>-<sequence>
```

Allowed characters are lowercase letters, digits, and hyphens. Use three-digit sequences.

| Record type | Prefix | Example |
|---|---|---|
| Research finding | `rf` | `rf-2026-mia-pass-rate-001` |
| Team overview | `to` | `to-2026-mia-overview-001` |
| Player profile | `pp` | `pp-all-player-slug-001` |
| Coaching profile | `cp` | `cp-2026-mia-head-coach-001` |
| Beat-writer registry | `bw` | `bw-2026-mia-registry-001` |
| Injury update | `iu` | `iu-2026-mia-player-slug-001` |
| Weekly matchup | `wm` | `wm-2026-w01-ne-sea-001` |
| Depth chart | `dc` | `dc-2026-mia-w01-001` |

The slug aids inspection but does not become mutable. If a title, team assignment, or path changes, preserve the ID.

## Entity IDs

- Teams: use the canonical abbreviation in `league/teams.csv`, such as `MIA`.
- NFL players: prefer `nfl-<GSIS ID>` when verified.
- Players without a verified external ID: use `local-player-<name-slug>-<first-known-year>` and never later reuse it.
- Coaches: use `local-coach-<name-slug>` until a canonical registry is introduced.
- Writers: use `local-writer-<name-slug>` until a canonical registry is introduced.

Do not guess an external ID. A stable local ID is better than an incorrect canonical-looking ID.

## Game IDs

When a weekly record needs a game reference, use:

```text
<season>-W<two-digit-week>-<away-abbr>-<home-abbr>
```

Example: `2026-W01-NE-SEA`. Home/away order is part of the identity.
