# Miami Dolphins 2026 Preseason Intelligence

This directory is the working layer for training camp and the preseason. It converts dated observations into current conclusions without erasing how those conclusions changed.

## Files

- [`monitoring-priorities.csv`](monitoring-priorities.csv): the ten questions established before camp.
- [`evidence-log.csv`](evidence-log.csv): append-only, source-attributed observations tied to a priority.
- [`priority-status.csv`](priority-status.csv): the current answer, confidence, and next test for each priority.
- [`depth-charts/`](depth-charts/): dated projected or unofficial personnel snapshots.

Current depth chart: [`2026-08-05-projected.md`](depth-charts/2026-08-05-projected.md)

## Workflow

1. Add a row to `evidence-log.csv` for a material practice, injury, transaction, coach statement, or preseason usage observation.
2. Prefer repetitions, alignments, participation, injury status, and game usage over praise or broad evaluation.
3. Update `priority-status.csv` only when the evidence changes the current answer, confidence, or next test.
4. Create a new dated depth-chart snapshot when personnel ordering changes materially. Mark the prior Markdown record `superseded`; never overwrite its historical state.
5. Move conclusions expected to remain useful after camp into `offense/`, `defense/`, or `special-teams/`.
6. Freeze this directory after the preseason reconciliation. Regular-season state belongs under `weekly/2026/`.

## Evidence rules

- `reported_observation`: a credentialed reporter's firsthand practice observation.
- `official_statement`: a team announcement, transcript, or coach statement.
- `roster_status`: an official roster, reserve-list, or transaction state.
- `projection`: an explicitly labeled synthesis; never treat it as observed fact.
- `independent_corroboration`: `yes` only when a separate source independently supports the same material claim.

Fantasy implications are hypotheses. They should be updated from measured preseason or regular-season usage, not treated as established because a player had one strong practice.
