# Agent Operating Guide

This file is the repository-level operating contract for human and LLM contributors.

## Read first

1. Read this file, `README.md`, and `SOURCE_POLICY.md`.
2. Read `schemas/README.md` before creating or changing a research record.
3. Use `league/teams.csv` for canonical team names, abbreviations, and paths.
4. Use `league/schedule/2026.csv` as the canonical schedule. Team-local `schedule.md` files are generated views.
5. Read the closest template in `templates/` before creating a record.

## Canonical sources

| Subject | Canonical location | Notes |
|---|---|---|
| Team identity and path | `league/teams.csv` | Never invent an abbreviation or alternate path. |
| 2026 schedule | `league/schedule/2026.csv` | Team schedules are synchronized views. |
| Player history | `players/<player>/` | Do not duplicate enduring profiles under multiple teams. |
| Durable team research | `teams/<conference>/<division>/<team>/<season>/` | Scheme, coaching, personnel, and source registries. |
| Weekly state | `weekly/<season>/week-<NN>/` | Injuries, weather, roles, matchups, projections, and decisions. |
| Record metadata rules | `schemas/` | JSON Schemas and controlled vocabularies. |
| Search index | `catalog.jsonl` | Generated; never edit manually. |

## Research-record rules

- Start all substantive research records with YAML front matter matching a schema in `schemas/`.
- Copy the nearest template; do not compose a new metadata shape ad hoc.
- Assign `record_id` once and never change or reuse it, even if the file moves or its title changes.
- Use team abbreviations from `league/teams.csv` in `team_ids`.
- Use JSON-style inline arrays in front matter, for example `team_ids: ["MIA"]`.
- Use ISO dates (`YYYY-MM-DD`) and integer weeks (`1` through `18`).
- Keep facts, inference, and fantasy implications visibly separate.
- Cite the original source, publication date, and link. Record when the claim was last verified.
- Set replaced records to `superseded` and link their IDs through `supersedes`; do not erase history.
- Use `invalidated` when evidence disproves a prior conclusion, and explain why in the body.

## Time boundary

- `durable`: traits or findings expected to survive team-week changes.
- `seasonal`: current-season coaching, roster, role, or schedule context.
- `weekly`: injuries, designations, weather, matchups, projections, and lineup decisions.

If a record mixes durable and weekly material, split it and link the records.

## Generated files

Do not manually edit:

- `catalog.jsonl`
- Weekly matchup files created by `scripts/generate_week.py` before their first human research edit

Regenerate the catalog after record changes:

```bash
python scripts/generate_catalog.py
```

## Required checks

Run before committing:

```bash
python scripts/validate_schedule.py
python scripts/generate_catalog.py
python scripts/validate_repository.py
python scripts/generate_catalog.py --check
```

Do not weaken validation to make a failing record pass. Fix the record, schema, controlled vocabulary, or canonical registry deliberately.
