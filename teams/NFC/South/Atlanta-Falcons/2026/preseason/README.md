# Atlanta Falcons 2026 preseason workspace

This directory tracks the highest-leverage preseason questions for the 2026 Falcons and the dated evidence that answers them. It is the working layer between durable team research (in the unit folders) and fast-changing in-season state (in `weekly/2026/`).

## Files

- `monitoring-priorities.csv` — the ranked list of preseason questions worth charting, why each matters, and where the answer belongs.
- `evidence-log.csv` — one row per dated observation (camp report, injury note, preseason snap), attributed to a source, with a fantasy read.
- `priority-status.csv` — the current answer and confidence for each priority, updated as evidence accumulates.
- `depth-charts/` — dated projected depth-chart snapshots (schema-validated `depth_chart` records).

## Workflow

1. Capture a dated, attributed observation in `evidence-log.csv` (separate the observed fact from interpretation).
2. Roll the observation up into the matching priority's `current_answer` and `confidence` in `priority-status.csv`.
3. When a projection becomes durable (a settled role, scheme, or depth-chart order), promote it into the relevant unit folder; when it becomes fast-changing in-season state, move it to `weekly/2026/`.

## Evidence boundary

Camp praise ("best shape," "unstoppable") is downgraded unless paired with role evidence (first-team reps, alignment, target or carry share). Weight official records and direct observations over aggregation. Attribute individual reporters, not just outlets.

Last verified: 2026-08-17.
