# Houston Texans 2026 Preseason Intelligence

This directory is the working layer for training camp and the preseason. It converts dated observations into current conclusions without erasing how those conclusions changed.

## Files

- [monitoring-priorities.csv](monitoring-priorities.csv): operational questions distilled from the offense and defense hypothesis files.
- [evidence-log.csv](evidence-log.csv): append-only, source-attributed observations tied to a priority.
- [priority-status.csv](priority-status.csv): the current answer, confidence, and next test for each priority.
- [depth-charts/](depth-charts/): dated projected or unofficial personnel snapshots.

Current depth chart: [2026-08-18-projected.md](depth-charts/2026-08-18-projected.md)

## Workflow

1. Add a row to `evidence-log.csv` for a material practice, injury, transaction, coach statement, depth-chart publication, or preseason usage observation.
2. Prefer participation, first-unit repetitions, alignment, routes, protection responsibility, touch type, and special-teams work over praise.
3. Update `priority-status.csv` only when evidence changes the current answer, confidence, or next test.
4. Create a new dated depth-chart snapshot when ordering changes materially. Mark the prior Markdown record `superseded`; do not overwrite its historical state.
5. Move conclusions expected to remain useful after camp into `offense/`, `defense/`, or `special-teams/`.
6. Freeze this directory after preseason reconciliation. Regular-season state belongs under `weekly/2026/`.

## Evidence Rules

- `reported_observation`: a credentialed reporter's firsthand practice observation.
- `official_statement`: a team or league announcement, published depth chart, transcript, or game record.
- `roster_status`: an official roster, reserve-list, or transaction state.
- `roster_projection`: an explicitly labeled projection; never treat it as observed fact.
- `game_usage`: preseason or regular-season game usage, participation, or deployment.
- `independent_corroboration`: `yes` only when a separate source independently supports the same material claim.

Projected depth charts synthesize available reporting and roster information. They do not establish snap share, routes, touches, subpackage usage, or equal competition unless a source explicitly says so.
