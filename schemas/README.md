# Record Schemas

Substantive Markdown research records begin with YAML front matter and validate against the JSON Schema matching `record_type`.

## Metadata envelope

All record types use the same core fields:

| Field | Meaning |
|---|---|
| `schema_version` | Metadata contract version; currently `1`. |
| `record_id` | Immutable record identifier from `ID_CONVENTIONS.md`. |
| `record_type` | One controlled record type. |
| `title` | Human-readable title. |
| `team_ids` | Team abbreviations from `league/teams.csv`. |
| `player_ids` | Stable player IDs; empty until resolved. |
| `season` / `week` | Applicable NFL season and week; use `null` when not applicable. |
| `status` | Lifecycle state: `draft`, `active`, `superseded`, or `invalidated`. |
| `time_horizon` | `durable`, `seasonal`, or `weekly`. |
| `valid_as_of` | Date the described state became applicable. |
| `last_verified` | Most recent evidence check. |
| `confidence` | `low`, `medium`, `high`, or `null` when not yet assessed. |
| `source_ids` | Stable source IDs, when a source registry exists. |
| `supersedes` | Record IDs directly replaced by this record. |

Some record types extend the envelope: `league_format` adds `fantasy_formats`,
`platform`, `league_size`, `draft_slot`, and `draft_date`.
`team_intelligence` adds `observation_ids` and `run_ids` so every synthesis remains traceable to
immutable reader batches.

Templates are valid drafts: IDs and dates may remain `null`. Before a record becomes `active`, it must have a stable `record_id`, `valid_as_of`, and `last_verified`.

## Choosing a time horizon

Choose the horizon based on how often the claim can become stale, not on where the file lives:

| Horizon | Use for | Examples | Normal review trigger |
|---|---|---|---|
| `durable` | Traits or historical findings expected to survive roster and week changes | Player skill traits, a coach's established philosophy, multi-season methodology | New multi-game evidence or a major role/system change |
| `seasonal` | State tied to the current league year | Coaching assignments, roster construction, projected roles, preseason depth charts | Transaction, depth-chart change, or new season |
| `weekly` | Short-lived decision context | Injuries, weather, matchup analysis, projections, start/sit decisions | Each practice report, forecast update, or completed game |

A record should use the shortest horizon needed by any material claim it contains. If durable
analysis and weekly state are both important, split them into linked records rather than labeling
the combined record `seasonal`. Changing a horizon is a metadata correction; it does not justify
changing the record's stable ID.

## Supersession integrity

`supersedes` relationships must reference existing stable IDs. A record may not supersede itself,
and supersession chains may not contain cycles. The repository validator enforces these rules.

Use JSON-style inline arrays because the standard-library parser intentionally supports a small, deterministic YAML subset:

```yaml
team_ids: ["MIA"]
player_ids: ["nfl-00-0039999"]
source_ids: []
```

## Files

- `controlled-values.json`: permitted shared vocabulary.
- `*.schema.json`: one formal JSON Schema per record type.
- `ID_CONVENTIONS.md`: immutable identifier rules and examples.

The repository validator implements the schema features used here without external packages. The schemas remain standard JSON Schema Draft 2020-12 documents for other tooling.
