# NE–SEA historical baseline: reproduction and limits

This is the calculation companion to the [September 9 research supplement](../../games/NE-at-SEA-research-supplement.md). It contains historical 2025 data only, through Super Bowl LX on February 8, 2026. Computation began before the September 9, 2026 opener; documentation was completed after scheduled kickoff. No Week 1 results enter these files.

## Inputs and reproduction

Source: [nflverse 2025 play-by-play CSV.gz](https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_2025.csv.gz), retrieved September 9, 2026 ET. This is an external analytical dataset, not an NFL official statistic or a registered monitoring-feed observation. The [manifest](provenance.json) retains the exact downloaded file's SHA-256 and computation time. Upstream files may be revised; a later download with a different hash is a different snapshot.

Download the public source separately, then run from this directory:

```bash
python3 compute_baseline.py /path/to/play_by_play_2025.csv.gz /path/to/output-directory
```

The script uses Python's standard library and makes no network requests. The large source download is excluded from the repository. [baseline-2025.csv](baseline-2025.csv) contains each denominator; [assigned-targets-2025.csv](assigned-targets-2025.csv) contains receiver counts. The script checks the season, final game date, 272 regular-season games, and selected sack totals against official club/gamebook totals. These are consistency checks, not an independent audit of the EPA model or every play label.

## Definitions

- Separate `REG` (17 games per team), `POST` (NE four games, SEA three), and `SB` (one game). POST includes SB; do not add or treat them as independent samples.
- Eligible plays have type run/pass and finite EPA; exclude deleted plays, kneels and spikes. Penalty-only/no-play rows are excluded. This can differ from other providers' scrimmage filters.
- EPA is the dataset's expected-points-added value, averaged without opponent adjustment. Success means EPA greater than zero. Defense values remain the opposing offense's EPA: lower is better on defense. These are descriptive 2025 baselines, not calibrated 2026 predictions.
- Dropbacks use `qb_dropback`, including sacks and scrambles. Designed runs exclude scrambles and include designed QB runs. Sack rates use dropbacks, not attempts plus sacks; do not compare to another denominator without converting.
- Explosive passes are completions gaining at least 20 yards per dropback; explosive runs gain at least 10 per designed run. These denominators are different by design.
- Early downs are first and second downs. Our neutral situation is Q1 or Q3 with absolute pre-play score margin at most seven. It deliberately excludes second/fourth-quarter clock management, but is a chosen proxy rather than a universal neutral definition.
- Neutral no-huddle rate is **not tempo**. Seconds per snap, motion, formation and play-action are not measured here.
- Red-zone possessions group `game_id`, `posteam`, and `fixed_drive`. A possession qualifies if an eligible play starts at or inside the opponent's 20. Score it successful if that possession has an offensive rushing/passing TD. This excludes some penalty-only entries and long TDs without a qualifying red-zone snap; it need not match an official red-zone table.
- Assigned targets require an eligible pass attempt, no sack, and a receiver ID. Team totals exclude throwaways and other unassigned throws. Counts are grouped by receiver name for this bounded extract; they are not a reusable identity registry. Target share is receiver assigned targets divided by all team assigned targets, not one QB's attempts.

Official cross-checks: [Seattle 2025 regular-season statistics](https://www.seahawks.com/team/stats/2025/reg), [New England 2025 regular-season statistics](https://www.patriots.com/team/stats/2025/reg), and the [Super Bowl gamebook](https://static.clubs.nfl.com/image/upload/patriots/ixew72ey6khgsxvpquw7.pdf), all checked September 9, 2026 ET. These sources validate selected counts, not our custom rates.
