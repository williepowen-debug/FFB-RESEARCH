# Buffalo Bills source-monitoring guide

This directory tracks the official records, independent reporting, team analysis, and
data sources used to monitor the 2026 Bills. Its primary job is to support dated
conclusions about injuries, participation, personnel order, player usage, coaching,
scheme, and transactions.

## Files

- [`registry.md`](registry.md) is the human-readable, schema-validated seasonal record.
- [`sources.csv`](sources.csv) contains one normalized row per person, outlet, or official source.
- [`endpoints.csv`](endpoints.csv) contains the pages used in the monitoring workflow.

The registry is the editorial view. The CSV files are the machine-readable source of
truth for source identity, status, function, priority, and endpoints.

## Signal hierarchy

1. Official transactions, injury reports, gamebooks, participation records, and roster status.
2. Measured game usage: snaps, routes, carries, targets, alignments, and special-teams work.
3. Direct practice observations from credentialed reporters.
4. Consistent observations from multiple independent reporters.
5. On-record coach and player comments, interpreted with context.
6. Film and scheme interpretation tied to observable evidence.

## Open monitoring questions

These are the Bills questions currently worth a source check, in priority order. Each
maps to a row in [`../offense/hypotheses.csv`](../offense/hypotheses.csv).

1. Connor McGovern's return from a lower-body injury and the Week 1 interior line (`buf-2026-off-q11`).
2. The left-guard job between Alec Anderson and Austin Corbett (`buf-2026-off-q11`).
3. James Cook's route participation and target rate against a two-year 32-33 reception baseline (`buf-2026-off-q09`).
4. Red-zone and goal-line distribution between Josh Allen and Cook (`buf-2026-off-q10`).
5. Whether DJ Moore concentrates target share in a historically distributed offense (`buf-2026-off-q03`, `buf-2026-off-q04`).

Last verified: 2026-08-20.
