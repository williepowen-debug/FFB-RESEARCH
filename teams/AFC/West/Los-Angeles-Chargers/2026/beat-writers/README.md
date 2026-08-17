# Los Angeles Chargers source-monitoring guide

This directory tracks the official records, independent reporting, team analysis, and data sources used to monitor the 2026 Chargers. Its primary jobs are to support dated conclusions about injuries, participation, personnel order, player usage, coaching, scheme, transactions, and contract context.

## Files

- [`registry.md`](registry.md) is the human-readable, schema-validated seasonal record.
- [`sources.csv`](sources.csv) contains one normalized row per person, outlet, or official source.
- [`endpoints.csv`](endpoints.csv) contains the pages used in the monitoring workflow.

The registry is the editorial view. The CSV files are the machine-readable source of truth for source identity, status, function, priority, and endpoints.

## Signal hierarchy

1. Official transactions, injury reports, gamebooks, participation records, and roster status.
2. Measured game usage: snaps, routes, carries, targets, alignments, and special-teams work.
3. Direct practice observations from credentialed reporters.
4. Consistent observations from multiple independent reporters.
5. On-record coach and player comments, interpreted with context.
6. Film and scheme interpretation tied to observable evidence.
7. Uncorroborated camp praise, aggregation, and unsupported opinion.

## Monitoring workflow

1. Check Chargers transactions, roster, depth chart, and injury pages.
2. Record material observations in [`../preseason/evidence-log.csv`](../preseason/evidence-log.csv).
3. Compare independent reporting before changing a consequential role projection.
4. Use team-employed analysis for access, quotations, and practice detail while labeling the lack of organizational independence.
5. After games, prefer NFL gamebooks and measured usage over depth-chart labels.
6. Move fast-changing regular-season conclusions to `weekly/2026/`.

## Source-handling rules

- Attribute individual reports rather than citing only the outlet.
- Keep observation, interpretation, and fantasy implication separate.
- A team-issued unofficial depth chart establishes the published ordering, not actual snap, route, or touch shares.
- Daniel Popper's seven-season Chargers beat history remains useful context, but his July 2026 move to a national NFL role makes him inactive for daily team monitoring until a replacement is verified.
- Do not reproduce paywalled text, paid data exports, or substantial copyrighted material.
- Reverify active roles before camp, after newsroom changes, and during the regular season.

