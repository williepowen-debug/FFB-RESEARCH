# Agent Operating Guide

This file is the repository-level operating contract for human and LLM contributors.

## Boot and closeout sequence

Before editing, read `BOOTSTRAP.md` and run the boot-up process. For source-of-truth work, operate
from an up-to-date `main`:

```bash
git switch main
git pull --ff-only
git status -sb
```

Create a feature branch for substantive changes. Run Standard Closeout before stopping. This
repository carries standing authorization for Publish Closeout after an in-scope task is complete
and validated: commit the intended files, push the feature branch, open a non-draft pull request,
merge it to `main` after required checks pass, delete the merged feature branch locally and
remotely, then resynchronize local `main`. The user may opt out or limit publication for any task.

Before stopping, inspect status and diff, run the relevant validation gate, and report branch/repo
state. Pause instead of publishing when validation or required GitHub checks fail, the intended
scope is unclear, unrelated changes are present, a merge conflict requires judgment, or the user
opts out. Destructive cleanup other than deleting a successfully merged task branch still requires
explicit authorization.

## Team maintainers

- `architect` is the upper-tier orchestration and build lead. Its project-agent definition is
  `.claude/agents/architect.md`.
- Invoke ARCHITECT for repo startup, GitHub source-of-truth workflow, branch planning, team-module
  build sequencing, cross-team standards, templates, schemas, scripts, validation, and routing to
  specialist desk agents.
- `bolt` is the Los Angeles Chargers desk lead. Its project-agent definition is
  `.claude/agents/bolt.md`, and its path-scoped operating contract is
  `teams/AFC/West/Los-Angeles-Chargers/AGENTS.md`.
- Invoke BOLT for Chargers research, source maintenance, module buildout, evidence
  reconciliation, and validation. BOLT may use other teams as structural comparators,
  but it does not own or edit their trees unless explicitly instructed.

## Agent hierarchy

```text
ARCHITECT — repo orchestration, build planning, standards, validation, source-of-truth workflow
└── BOLT — Los Angeles Chargers specialist desk
```

Start with ARCHITECT for broad repo/build work. Route to BOLT only after repo state and task scope
are clear and the work is Chargers-specific.

## Read first

1. Read this file, `README.md`, and `SOURCE_POLICY.md`.
2. Read `schemas/README.md` before creating or changing a research record.
3. Use `league/teams.csv` for canonical team names, abbreviations, and paths.
4. Use `league/schedule/2026.csv` as the canonical schedule. Team-local `schedule.md` files are generated views.
5. Read the closest template in `templates/` before creating a record.
6. To build out a whole team, follow `TEAM_BUILD.md` (Core-tier layout, IDs, CSV headers, validation gate).

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
python3 scripts/generate_catalog.py
```

## Required checks

Run before committing:

```bash
python3 scripts/validate_schedule.py
python3 scripts/generate_catalog.py
python3 scripts/validate_repository.py
python3 scripts/generate_catalog.py --check
```

Do not weaken validation to make a failing record pass. Fix the record, schema, controlled vocabulary, or canonical registry deliberately.
