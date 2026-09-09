# Seattle Seahawks source-monitoring guide

This directory tracks official records, current reporters, analysts, and data sources for fantasy-relevant Seahawks injuries, roles, usage, scheme, and roster construction. The candidate ledger preserves both discovery passes and explicit exclusions.

Start with official records and independent observations, then use film analysis to interpret them and measured usage to test conclusions. Team and radio employees are not independent confirmation. Attribute every report and follow aggregation to its origin.

## Files

- [registry.md](registry.md) — the schema-governed registry record (`bw-2026-sea-registry-001`): rotation, coverage lanes, handling rules, and `writer_ids`.
- [sources.csv](sources.csv) — one row per registered source with its stable `source_id`, class, priority, status, access, and handling note. Observations cite these IDs.
- [endpoints.csv](endpoints.csv) — retrievable URLs per source, with access level and automation suitability.
- [candidates.csv](candidates.csv) — the durable audit ledger: every candidate considered, with evidence, disposition (`include`, `exclude`, `unverified`), and verification date.

Refresh this directory using [SOURCE_REGISTRY_AUDIT.md](../../../../../../SOURCE_REGISTRY_AUDIT.md): ecosystem discovery, then a fresh adversarial omission pass, then construction and cross-file reconciliation. Never rename or delete a `source_id`; retire it with `status` and `ended_on` so historical frozen runs keep their provenance.
