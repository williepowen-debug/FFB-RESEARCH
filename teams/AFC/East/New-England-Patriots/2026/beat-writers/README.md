# New England Patriots source-monitoring guide

This directory tracks official records and independent reporting used to monitor the 2026
Patriots. Its focus is availability, practice participation, roster status, personnel order,
player usage, coaching, and scheme.

## Files

- [`registry.md`](registry.md) is the human-readable, schema-validated seasonal record.
- [`sources.csv`](sources.csv) contains normalized source identities and monitoring roles.
- [`endpoints.csv`](endpoints.csv) contains the pages used in the monitoring workflow.

The CSV files are the machine-readable source of truth. The registry explains how to weight and
combine them.

## Signal hierarchy

1. Official transactions, injury reports, gamebooks, participation records, and roster status.
2. Measured game usage: snaps, routes, targets, carries, alignments, and special-teams work.
3. Direct practice observations from credentialed reporters.
4. Consistent observations from multiple independent reporters.
5. On-record coach and player comments interpreted in context.
6. Film and scheme interpretation tied to observable evidence.

## Open monitoring questions

1. Whether Rhamondre Stevenson or TreVeyon Henderson controls passing downs and goal-line work
   (`ne-2026-off-q06`, `ne-2026-off-q07`).
2. Whether A.J. Brown creates a concentrated target structure (`ne-2026-off-q01`,
   `ne-2026-off-q02`).
3. Whether the reworked offensive line settles on a stable first unit (`ne-2026-off-q09`).
4. Whether Hunter Henry retains a meaningful route and red-zone role (`ne-2026-off-q05`).

Last verified: 2026-08-20.
