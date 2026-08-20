# Team Module Build Guide

This guide codifies the structure first built for the Miami Dolphins so every team
module comes out consistent, validates identically, and stays comparable across the league.

Read `AGENTS.md`, `SOURCE_POLICY.md`, and `schemas/README.md` first. This guide governs
*how the pieces fit into a team folder*; the per-record templates in this directory and the
JSON Schemas in `schemas/` govern the *shape of each record*.

## Tiers

A team is built to one of two depths. Pick the tier before you start and note it in the
overview's front matter body.

- **Core tier** — the standard build. Overview, coaching intelligence, offense findings,
  defense findings, and roster CSVs. Enough to drive matchup and start/sit reasoning.
- **Full (Dolphins parity)** — Core plus position-group subfolders
  (`offense/offensive-line/`, `offense/wide-receivers/`, `offense/tight-ends/`),
  a `preseason/` workspace (dated depth charts, evidence log, monitoring/priority CSVs),
  and a `beat-writers/` source registry. Reserve for teams that justify the depth.

Both tiers use the same folder spine and the same record types. Full tier only *adds*
files; it never changes where a Core file lives. Start Core, deepen later without moving anything.

## Core-tier layout

```text
teams/<conference>/<division>/<Team-Name>/2026/
├── overview.md                     team_overview  — the module's front door
├── coaching-staff/
│   ├── README.md                   plain doc: authority model + file index
│   ├── staff.csv                   full coach directory
│   ├── leadership-transition.csv   2025→2026 leadership changes
│   ├── <head-coach>.md             coaching_profile
│   ├── <offensive-coordinator>.md  coaching_profile
│   └── <defensive-coordinator>.md  coaching_profile
├── offense/
│   ├── README.md                   plain doc: ecosystem framing + file index
│   ├── <finding>.md ...            research_finding (one per durable question)
│   └── hypotheses.csv              machine-readable questions to test
├── defense/
│   ├── README.md                   plain doc: unit framing + file index
│   ├── <finding>.md ...            research_finding
│   └── hypotheses.csv
├── roster/
│   ├── README.md                   plain doc (optional but recommended)
│   ├── departures.csv
│   ├── veteran-additions.csv
│   ├── retentions.csv
│   ├── draft-class.csv
│   └── undrafted-free-agents.csv   (optional)
├── special-teams/.gitkeep          leave scaffolded at Core tier
├── beat-writers/.gitkeep           leave scaffolded at Core tier (Full tier fills this)
└── schedule.md                     already generated — do not hand-edit
```

For new Core-tier modules, `README.md`, `*.csv`, and `.gitkeep` files carry **no** YAML front
matter. READMEs are navigation and framing documents, not research records. The validator still
checks their relative links. Only `overview.md`, coaching profiles, and dedicated finding files
are schema-governed records.

Some Full-tier modules created before this convention use unit READMEs as cataloged research
findings. Those files are supported legacy records and should remain stable until a deliberate
migration can preserve their `record_id` and inbound links. Do not copy that legacy shape into a
new module; place new findings in descriptively named Markdown files and link them from a plain
README.

## Record types and required sections

The validator (`scripts/validate_repository.py`) rejects any record missing a required
`## ` section. Copy the matching template and keep every required heading.

| File | record_type | Template | Required `##` sections |
|---|---|---|---|
| `overview.md` | `team_overview` | `templates/team-overview.md` | Fantasy-relevant snapshot · Offensive identity · Defensive matchup profile · Coaching and scheme · Sources |
| coaching profiles | `coaching_profile` | `templates/coaching-profile.md` | Responsibilities · Scheme and tendencies · Fantasy implications · Sources |
| offense/defense findings | `research_finding` | `templates/research-finding.md` | Finding · Fantasy implication · Evidence · Sources · Assessment |

Notes:
- `coaching_profile` records carry an extra `coach_id` key; no other record type may add keys
  (front matter is `additionalProperties: false`).
- `research_finding` front matter does **not** carry `fantasy_formats`. Per-format relevance
  lives in the `fantasy_formats` column of `hypotheses.csv` instead.
- A record with `status: active` must have a non-null `record_id`, `valid_as_of`,
  `last_verified`, and `confidence`, and a title with no `<placeholder>`.

## ID scheme

Assign IDs once and never change or reuse them (`schemas/ID_CONVENTIONS.md`). Use the team's
canonical lowercase abbreviation from `league/teams.csv` as the scope. For Buffalo (`BUF`):

| Record | Pattern | Example |
|---|---|---|
| Team overview | `to-2026-<abbr>-overview-001` | `to-2026-buf-overview-001` |
| Coaching profile | `cp-2026-<abbr>-<role-or-name>-001` | `cp-2026-buf-head-coach-001` |
| Research finding | `rf-2026-<abbr>-<slug>-001` | `rf-2026-buf-receiving-hierarchy-001` |

Coach entity IDs use `local-coach-<name-slug>` until a canonical registry exists.
Player IDs stay empty (`player_ids: []`) until a verified profile exists in `players/`.

## Canonical CSV headers

Reuse these exact headers so columns stay comparable across teams. Copy from the Miami files
if in doubt.

- `roster/departures.csv`
  `player,position,2025_role,transaction,transaction_date,destination,performance_significance,source_url,last_verified`
- `roster/veteran-additions.csv`
  `player,position,acquisition_type,transaction_date,current_status_as_of_2026_08_05,role_or_competition,source_url,last_verified`
- `roster/retentions.csv`
  `player,position,retention_type,transaction_date,through_season,reported_value,strategic_signal,source_url,last_verified`
- `roster/draft-class.csv`
  `round,overall_pick,player,position,college,position_group,immediate_monitoring_question,source_url,last_verified`
- `roster/undrafted-free-agents.csv`
  `player,position,college,initial_acquisition_date,current_status_as_of_2026_08_05,status_date,notes,source_url,last_verified`
- `coaching-staff/staff.csv`
  `coach_id,name,unit,2026_role,retained_from_2025,2025_role_if_retained,source_url,last_verified`
- `coaching-staff/leadership-transition.csv`
  `area,role,2025_leader,interim_if_any,2026_leader,effective_or_announcement_date,evidence_class,source_url,last_verified`
- `offense/hypotheses.csv` and `defense/hypotheses.csv`
  `question_id,priority_id,entity_or_unit,preseason_hypothesis,confirming_evidence,disconfirming_evidence,baseline_confidence,fantasy_formats,review_trigger,status,last_updated`

`fantasy_formats` in `hypotheses.csv` is a `;`-separated list drawn from
`schemas/controlled-values.json`. Dates are ISO (`YYYY-MM-DD`). Every row that asserts a fact
carries a `source_url` and `last_verified`.

## Build order

1. **Confirm identity.** Read the team's row in `league/teams.csv` for the exact folder path
   and abbreviation. Never invent either.
2. **Roster CSVs.** Establish the factual spine first — departures, additions, retentions,
   draft class. Findings reference these.
3. **Coaching staff.** `staff.csv` + `leadership-transition.csv`, then HC/OC/DC profiles,
   then the `README.md` authority model.
4. **Overview.** Write `overview.md` last among the "durable" set — it summarizes and links
   everything above.
5. **Offense / defense findings.** One `research_finding` per durable question, with a
   matching row family in `hypotheses.csv`. Keep facts, inference, and fantasy implications
   visibly separate.
6. **READMEs.** Each unit README is a plain doc: a short framing paragraph plus a linked
   index of the unit's files.

## Sourcing standard

Every asserted fact needs an attributable, dated source (`SOURCE_POLICY.md`). Prefer official
team and league sources for transactions, staff, and roster; attribute reporters/outlets for
analysis. Record publication and verification dates. Separate reported facts from inference and
from fantasy implications. Where 2026 evidence is thin, state a hypothesis with low confidence
and a `review_trigger` — do not manufacture certainty.

## Validation gate

A team module is not done until this passes clean:

```bash
python3 scripts/generate_catalog.py
python3 scripts/validate_repository.py
python3 scripts/validate_schedule.py
python3 scripts/generate_catalog.py --check
```

(The interpreter is `python3`.) Do not weaken validation to make a record pass — fix the
record, schema, or registry deliberately.
