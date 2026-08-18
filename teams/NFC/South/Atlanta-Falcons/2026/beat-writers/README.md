# Atlanta Falcons source-monitoring guide

This directory tracks the people, outlets, official records, analysis, and data sources used to monitor the 2026 Atlanta Falcons for performance and fantasy-football research: injuries, availability, practice participation, depth-chart movement, player usage, coaching and scheme, transactions, and contract context.

## Files

- `registry.md` is the human-readable, schema-validated seasonal record.
- `sources.csv` contains one normalized row per person, collective, outlet, or official source.
- `endpoints.csv` contains websites, social accounts, feeds, and other monitoring endpoints.

The registry is the editorial view. The CSV files are the machine-readable source of truth for source identity, status, function, priority, and endpoints.

## Classification model

Do not treat priority and function as the same field.

| Dimension | Values | Meaning |
|---|---|---|
| `source_class` | `official`, `reporting`, `team_analysis`, `film_analysis`, `commentary`, `data`, `aggregation`, `fantasy_analysis`, `contract_data` | What the source primarily contributes |
| `priority` | `essential`, `valuable`, `supplemental` | How frequently the monitoring workflow should check it |
| `status` | `active`, `inactive` | Whether the person or source currently belongs in the monitoring rotation |

A team-employed reporter and an independent beat writer can both be essential without being interchangeable: the team source may break a transaction first, but it is not organizationally independent.

## Signal hierarchy

When reports conflict, weight evidence in this order:

1. Official injury reports, transactions, gamebooks, and participation records.
2. Direct observations of attendance, participation level, first-team repetitions, position, and drill work.
3. Measured regular-season usage: snaps, routes, carries, targets, alignments, and special-teams work.
4. Consistent observations from multiple independent credentialed reporters.
5. On-record player and coach comments, interpreted with incentives and context in mind.
6. Film or scheme interpretation tied to observable evidence.
7. Uncorroborated camp praise, anonymous aggregation, and opinion without supporting evidence.

Pro Football Reference snap counts are a convenient structured reference, not the ultimate source of record. Treat PFF grades as a proprietary evaluation rather than an official fact. When an aggregator surfaces a claim, follow its link and cite the original report.

## Monitoring workflow

### Training camp and preseason

1. Check official transactions, injury designations, and PUP/suspension status (e.g., the Pearce suspension, the Penix ACL return, the Taylor PUP activation).
2. Record absences, participation, first-team repetitions, and position experiments from credentialed observations.
3. Compare at least two independent reporters when a claim could materially change a player projection.
4. Use film and scheme analysts to interpret meaning only after the observed facts are captured.
5. Downgrade unsupported praise unless it is paired with role evidence.

### Regular season

1. Start with the official injury report and final game designation.
2. Use the NFL gamebook and participation data after each game.
3. Track snaps, routes, targets, carries, goal-line work, two-minute work, and special-teams usage.
4. Use press conferences and beat reporting to explain changes, not to overwrite measured usage.
5. Put fast-changing conclusions in `weekly/2026/`; keep only durable or seasonal source information here.

## Source-handling rules

- Separate reported facts, interpretation, and fantasy implications in every downstream record.
- Attribute a claim to the individual reporter, not merely the outlet.
- Label team-employed analysis (McFadden, Conway, McElhaney). It can carry strong practice and film detail, but it is not organizationally independent.
- Record role changes instead of silently deleting stale affiliations. Use `former_role`, `ended_on`, and `replacement_if_known` in `sources.csv` (as done for the Ledbetter-to-Flick and Rothstein-to-Raimondi beat transitions).
- Do not reproduce paywalled text, paid data exports, or substantial copyrighted material. Store links and original summaries.
- Reverify active roles and endpoints before camp, after major newsroom changes, and at least once during the regular season.

## Maintenance

Update `last_verified` whenever a role or endpoint is checked. Set a departed source to `inactive` rather than deleting the row. Add a new row only after confirming the person's current role from the outlet or the person's own current profile.
