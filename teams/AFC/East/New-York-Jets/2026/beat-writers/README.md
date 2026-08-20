# New York Jets source-monitoring guide

This directory tracks official records and independent reporting used to monitor the 2026 Jets.
Its focus is availability, practice participation, roster status, personnel order, player usage,
coaching, and scheme.

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

1. Whether Breece Hall retains three-down and goal-line work (`nyj-2026-off-q05`,
   `nyj-2026-off-q06`).
2. Which receiver becomes the stable complement to Garrett Wilson (`nyj-2026-off-q03`).
3. Whether Kenyon Sadiq earns an immediate receiving role (`nyj-2026-off-q04`).
4. Whether the rebuilt interior offensive line stabilizes (`nyj-2026-off-q07`).

Last verified: 2026-08-20.
