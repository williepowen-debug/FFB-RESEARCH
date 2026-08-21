# Reader and Synthesis Pipeline

This pipeline turns the source registries into a bounded evidence intake system. Readers collect
small observations; team synthesizers reconcile them; only material signals reach the league
priority board or update durable research.

```text
source registries
  -> immutable reader batches
  -> team synthesis snapshots
  -> league priority board
  -> existing team, player, and weekly records
```

## Operating principles

1. Readers collect evidence, not conclusions. Preserve the originating source, timestamps, and a
   concise original-language paraphrase.
2. One observation represents one atomic claim. Split unrelated injury, role, and transaction
   claims even when they appear in one article.
3. Repetition is not corroboration. Use `dedup_key` and `origin_url` to collapse syndication,
   aggregation, quote recirculation, and multiple posts derived from the same report.
4. Conflicts remain visible. A later or competing observation may `confirm`, `contradict`,
   `update`, or `repeat` another claim; it must not silently overwrite it.
5. Team synthesis is the first judgment layer. Readers never change hypotheses, player profiles,
   rankings, projections, or lineup decisions directly.
6. Promotion preserves traceability: priority item -> team synthesis -> observation IDs -> original
   URLs and source IDs.

## Directory layout

Reader output is date- and run-scoped so concurrent readers do not append to the same file.

```text
intelligence/<season>/
├── runs/<run-id>/<reader-id>/observations.csv
├── syntheses/<YYYY-MM-DD>/<team-abbr>.md
└── priority/<YYYY-MM-DD>/priority-board.csv
```

`run-id` should be an ordered UTC stamp such as `20260821T180000Z`. Reader batches are immutable
after synthesis begins. Corrections arrive in a new run and relate back to the prior observation.

## Reader assignment

Each reader receives a bounded team set, source IDs from that team's registry, a retrieval window,
and one or more lanes:

- `official_record`: transactions, injuries, depth charts, press conferences, gamebooks;
- `beat_reporting`: practice participation, reps, rotations, roles, locker-room reporting;
- `analysis`: film, scheme, alignment, and evidence-based role interpretation;
- `data`: snaps, routes, targets, carries, alignments, contracts, and roster mechanics.

Readers may report outside their assigned lane only when the finding is time-sensitive; mark that
fact in `notes` for synthesis review.

Use [templates/reader-assignment.csv](templates/reader-assignment.csv) to freeze assignments.
Spawn-ready role contracts live in `.claude/agents/reader.md` and
`.claude/agents/synthesizer.md`.

Use the same exact retrieval window for every team in a comparative pilot. A completed reader run
may contain zero observations: `no meaningful update` is a valid result when the reader documents
which sources were checked and what could not be accessed. Pilot assignments should normally cap
output at 20 observations per team, with 10–20 as a useful target when the window contains real
news. The cap is a noise control, not a quota; never manufacture rows to reach it.

## Observation contract

Copy [templates/reader-observations.csv](templates/reader-observations.csv). Required fields are
validated by `scripts/validate_intelligence.py`.

- `observation_id`: immutable `obs-<season>-<team>-<run>-<sequence>` ID.
- `team_id`: canonical abbreviation from `league/teams.csv`.
- `player_ids`: semicolon-separated canonical IDs; blank when unresolved or team-wide.
- `source_id`: exact ID from the team's `beat-writers/sources.csv`.
- `source_url`: page actually supporting the claim.
- `origin_url`: earliest known originating report; equal to `source_url` for original work.
- `published_at` / `retrieved_at`: ISO 8601 timestamps with timezone.
- `evidence_lane`: controlled factual subject.
- `evidence_kind`: official fact, reported fact, firsthand observation, analysis, or measured data.
- `claim_summary`: concise paraphrase of one claim; no copied article passages.
- `relationship`: `new`, `confirm`, `contradict`, `update`, or `repeat`.
- `related_observation_ids`: semicolon-separated IDs when relationship is not `new`.
- `dedup_key`: normalized event key shared by claims with the same origin and meaning.
- `confidence`: confidence that the observation faithfully represents its source, not confidence in
  a fantasy conclusion.
- `time_sensitivity` and `fantasy_impact`: reader triage inputs, subject to synthesis review.

## Deduplication and corroboration

The synthesizer groups first by `dedup_key`, then inspects `origin_url`, quoted speaker, event time,
and source relationships.

- Same originating report repeated by five outlets: one evidence cluster.
- Two reporters independently observing the same first-team rotation: two supporting observations.
- Team announcement plus reporter interpretation: one official fact and one interpretation, not
  two confirmations of the interpretation.
- Updated injury status: retain both observations and mark the newer one `update`.
- Conflicting practice accounts: retain both, mark `contradict`, and lower conclusion confidence.

## Team synthesis

Copy [templates/team-intelligence.md](templates/team-intelligence.md). A team synthesizer must:

1. reconcile duplicate, confirming, updating, and conflicting observations;
2. separate established facts from interpretation;
3. state what changed relative to existing repo knowledge;
4. decide whether a hypothesis or research record needs review;
5. assign one routing level to each material signal.

Routing levels:

- `log`: preserve evidence; no current conclusion changes.
- `review`: a hypothesis may change or needs corroboration/follow-up.
- `escalate`: material, time-sensitive change to availability, role, projection, ranking, waiver,
  trade, draft, or lineup decisions.

Escalation should be intentionally difficult. It normally requires official evidence, measured
usage, or strong independent reporting plus an immediate fantasy decision consequence. Generic
praise, repeated commentary, unsupported speculation, and unchanged status remain `log` or are
excluded as false positives.

## League priority board

Copy [templates/intelligence-priority-board.csv](templates/intelligence-priority-board.csv). The
board is a work queue, not a news digest. Every row must reference a synthesis record and one or
more observation IDs. Suggested ordering is:

```text
priority_score = fantasy_impact * evidence_confidence * novelty * time_sensitivity
```

Use ordinal values only as a sorting aid; the documented `escalation_level`, evidence, and next
action remain authoritative. Repeated commentary and unchanged status do not belong on the board.

## Promotion rules

- Injury or designation changes -> `weekly/<season>/week-<NN>/` injury/matchup records when a week
  applies; preseason changes remain in dated syntheses until they alter a seasonal role.
- Stable role or scheme changes -> team findings and `hypotheses.csv`.
- Enduring player-trait evidence -> canonical `players/<player>/` profile.
- Immediate decisions -> league rankings/watchlists or weekly decision records.
- No promotion -> keep as `log`; do not create permanent research noise.

Promotion updates the target record's verification date and sources. It does not delete the
underlying observation or synthesis snapshot.

## Run sequence

1. Freeze reader assignments, source IDs, lanes, and retrieval window.
2. Readers write separate immutable batches.
3. Validate intake with `python3 scripts/validate_intelligence.py`.
4. Synthesize by team and date.
5. Validate again, including synthesis and priority references.
6. Promote approved changes to existing records.
7. Run the standard repository validation gate.

Pilot the system on one dense ecosystem, one subscription-heavy ecosystem, and one thinner or
team-controlled ecosystem before scheduling all 32 teams. Use
[THREE_TEAM_PILOT.md](THREE_TEAM_PILOT.md) for the initial 49ers, Saints, and Cardinals manual
pilot. Do not automate scheduling, retrieval, synthesis, or promotion until the retrospective
identifies a stable repeated step worth automating.
