# Chargers Desk Operating Contract

This file applies to the Los Angeles Chargers directory and every descendant. BOLT is the primary
maintainer persona, but these rules apply to any contributor or agent working in this tree.

## Ownership boundary

The desk owns durable and seasonal Chargers research under this directory. It may read other team
trees for schemas, layout, and coverage comparisons, but it must not transplant team-specific
claims or edit those trees without explicit instruction.

Keep these boundaries intact:

| Subject | Canonical location |
|---|---|
| Chargers team and season research | `teams/AFC/West/Los-Angeles-Chargers/<season>/` |
| Enduring player profiles | `players/<player>/` |
| Week-specific state and decisions | `weekly/<season>/week-<NN>/` |
| Canonical schedule | `league/schedule/2026.csv` |
| Generated research index | `catalog.jsonl` |

## Read order

Before editing, read:

1. the root operating documents required by root `AGENTS.md`;
2. `2026/overview.md`;
3. the relevant module's `README.md` and substantive records;
4. `2026/beat-writers/README.md` and its registries when finding or evaluating sources;
5. `2026/preseason/README.md`, `monitoring-priorities.csv`, `priority-status.csv`, and
   `evidence-log.csv` when a conclusion depends on camp or preseason evidence;
6. the current working-tree status and relevant diff.

## File roles

| Location | Role |
|---|---|
| `2026/overview.md` | Seasonal team map and links to the desk's completed modules |
| `2026/beat-writers/` | Source identities, beats, access status, and usable endpoints |
| `2026/preseason/monitoring-priorities.csv` | Questions the desk is actively trying to answer |
| `2026/preseason/priority-status.csv` | Current answer, confidence, and next evidence needed |
| `2026/preseason/evidence-log.csv` | Append-only dated observations with source and boundary |
| `2026/preseason/depth-charts/` | Dated snapshots; never a silently overwritten current chart |
| `2026/offense/`, `defense/`, `coaching/`, `roster/` | Durable and seasonal research modules |

## Evidence rules

- Separate observed fact, interpretation, and fantasy implication.
- Cite the original source, its publication date, and a durable link when one is available.
- Record the evidence boundary: starters or reserves, padded or unpadded, practice or game,
  preseason or regular season, direct report or inference.
- Treat team-issued depth charts as official publications, not guaranteed usage forecasts.
- Treat a player's success against reserves as evidence about that competition, not proof that the
  result transfers to NFL starters.
- Prefer official transaction and participation records for roster facts. Prefer registered local
  reporters for practice observations. Use independent analysis for interpretation.
- Keep negative and disconfirming evidence. Update the conclusion and confidence; do not erase the
  path that produced the earlier state.
- Mark a question open when support is inadequate. Never convert absence of reporting into evidence
  of absence.

## Maintenance queue

Unless a material team change or explicit user request reprioritizes the desk, work through:

1. dedicated tight-end research;
2. dedicated backfield research;
3. dedicated wide-receiver research;
4. defensive fantasy-impact research and role monitoring;
5. coaching influence map and scheme watchlist;
6. canonical player profiles where the team modules establish enduring research value;
7. special-teams coverage where it affects roster survival, field position, or fantasy decisions.

The beat-writer registry, preseason workspace, UDFA ledger, offensive-line module, and overview are
maintained foundations, not one-time deliverables. Revisit them whenever new evidence changes their
accuracy or usefulness.

## Change discipline

- Preserve unrelated and concurrent work in a dirty worktree.
- Use the closest repository template and a schema-valid front matter block for every substantive
  research record.
- Never reuse or silently change a stable `record_id`.
- Do not hand-edit `catalog.jsonl`; regenerate it.
- Keep module README and overview links aligned with the records that actually exist.
- Do not commit, push, open a pull request, or modify GitHub authentication without explicit user
  authorization.

## Completion gate

From the repository root, run:

```bash
python3 scripts/validate_schedule.py
python3 scripts/generate_catalog.py
python3 scripts/validate_repository.py
python3 scripts/generate_catalog.py --check
git diff --check
```

Report what changed, the evidence boundary, remaining open questions, and all validation results.
