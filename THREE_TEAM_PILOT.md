# Three-team intelligence pilot

This pilot tests the reader-to-synthesis workflow manually before it is expanded or automated.
The teams intentionally represent different source environments:

- San Francisco 49ers (`SF`): dense reporting with substantial overlap;
- New Orleans Saints (`NO`): meaningful subscription and access constraints;
- Arizona Cardinals (`ARI`): thinner, more team-controlled coverage.

## Success question

Can a bounded reader assignment produce traceable, low-noise evidence that a synthesizer can
reconcile into useful routing decisions without losing conflicts or mistaking repetition for
confirmation?

## Frozen run design

ARCHITECT creates one UTC `run_id` and one exact 24–48 hour `window_start` and `window_end` shared
by all three teams. Each team receives one reader, only registered active sources, explicit lanes,
an output directory, and a maximum of 20 observations. Ten to twenty observations is a useful
target when meaningful news exists, but zero is acceptable. Volume is never a success measure.

Record the frozen assignments in `templates/reader-assignment.csv`. Put assignment-specific caps
or access notes in its `notes` field.

## Stage 1: reader intake and quality pause

Each reader creates an immutable observation batch and a run report copied from
`templates/reader-run-report.csv`. The report accounts for every assigned source with one outcome:

- `checked`: accessible and yielded one or more candidate items;
- `no_new_material`: accessible but nothing meaningful fell inside the window;
- `inaccessible`: blocked by subscription, authentication, or permissions;
- `failed_endpoint`: expected endpoint did not function.

After `python3 scripts/validate_intelligence.py` passes, stop before synthesis. ARCHITECT manually
checks three observations per team against their linked sources, sampling different evidence kinds
when possible. Verify atomicity, paraphrase fidelity, timestamp accuracy, registered `source_id`,
origin tracing, and `dedup_key`. Record failures in the run report and correct intake before moving
on.

The three checks should include one official or measured item, one independent reported or
firsthand item, and one relationship/provenance-sensitive item when the batch contains them. If a
sample exposes a systematic defect, inspect and correct every affected row or evidence cluster.

## Stage 2: synthesis and routing

Assign one synthesizer per team only after the intake quality pause passes. Each synthesizer counts
unique evidence clusters, not headlines or raw rows; preserves independent confirmation and
conflicts; and completes the excluded-noise section in the team synthesis.

Use these routing bars:

- `log`: worth preserving, but no current conclusion changes;
- `review`: could change a hypothesis or requires specific follow-up;
- `escalate`: official evidence, measured usage, or strong independent reporting indicates a
  material and time-sensitive fantasy decision change.

Generic praise, syndicated repetition, recycled quotes, unsupported speculation, and unchanged
status are false positives. Record them under excluded noise instead of allowing them to inflate
the priority board.

ARCHITECT reviews all syntheses and decides whether anything is promoted into canonical team,
player, or weekly research. Before promotion, ARCHITECT records every `review` or `escalate`
signal in the affected team's `intelligence-ledger.csv` with a `promoted`, `deferred`, or
`no_change` disposition. No reader or synthesizer edits the team ledger or promotes evidence
independently.

## Pilot measurements

Capture for each team:

- sources assigned and each access outcome;
- reader elapsed time and raw observation count;
- unique evidence clusters and repeats removed;
- conflicts and independent confirmations;
- `log`, `review`, and `escalate` counts;
- false positives excluded;
- spot-check failures and corrections;
- synthesizer and ARCHITECT review time.

These metrics compare workload and information quality across source environments. They are not
productivity targets.

## Retrospective and decision

Copy `templates/pilot-retrospective.csv` after all three teams are reviewed. Summarize qualitative
findings in the run handoff and choose one outcome:

- `pass`: contracts are clear enough for another bounded batch;
- `revise`: fix the contracts or templates, then repeat the three-team test;
- `partial_pass`: expand only the source environments that performed reliably.

Keep automation out of this pilot. The retrospective may nominate small deterministic checks for
later implementation, but it should not authorize automated retrieval, scheduling, synthesis, or
promotion by default.
