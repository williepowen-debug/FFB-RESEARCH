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

Templates are valid drafts: IDs and dates may remain `null`. Before a record becomes `active`, it must have a stable `record_id`, `valid_as_of`, and `last_verified`.

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
