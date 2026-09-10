"""Reproduce the dated NE/SEA baseline from a local nflverse 2025 CSV.gz.

Usage: python3 compute_baseline.py INPUT.csv.gz OUTPUT_DIRECTORY
No network access. See the accompanying research record for interpretation.
"""
import csv
import gzip
import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


def number(row, key):
    try:
        value = float(row[key])
        return value if math.isfinite(value) else None
    except (ValueError, KeyError):
        return None


def flag(row, key):
    return number(row, key) == 1


def eligible(row):
    return (row['play_type'] in ('run', 'pass')
            and not flag(row, 'qb_kneel') and not flag(row, 'qb_spike')
            and not flag(row, 'play_deleted')
            and number(row, 'epa') is not None)


def summarize(rows, team, phase, unit):
    side = 'posteam' if unit == 'offense' else 'defteam'
    selected = [r for r in rows if r[side] == team and
                (r['game_id'] == '2025_22_SEA_NE' if phase == 'SB'
                 else r['season_type'] == phase)]
    plays = [r for r in selected if eligible(r)]
    assert plays, (team, phase, unit)
    result = {'team': team, 'phase': phase, 'unit': unit,
              'games': len({r['game_id'] for r in selected}), 'plays': len(plays)}
    def mean(items, key):
        values = [number(r, key) for r in items if number(r, key) is not None]
        return round(sum(values) / len(values), 6) if values else ''
    def rate(count, denominator):
        return round(count / denominator, 6) if denominator else ''
    result['epa_per_play'] = mean(plays, 'epa')
    result['success_rate'] = rate(sum(number(r, 'epa') > 0 for r in plays), len(plays))
    early = [r for r in plays if number(r, 'down') in (1, 2)]
    result['early_down_plays'] = len(early)
    result['early_down_epa'] = mean(early, 'epa')
    drops = [r for r in plays if flag(r, 'qb_dropback')]
    runs = [r for r in plays if r['play_type'] == 'run' and not flag(r, 'qb_scramble')]
    result['dropbacks'] = len(drops)
    result['dropback_epa'] = mean(drops, 'epa')
    result['sacks'] = sum(flag(r, 'sack') for r in drops)
    result['sacks_per_dropback'] = rate(result['sacks'], len(drops))
    result['designed_runs'] = len(runs)
    result['designed_run_epa'] = mean(runs, 'epa')
    result['designed_run_yards_per_attempt'] = mean(runs, 'yards_gained')
    result['explosive_passes_20'] = sum(flag(r, 'complete_pass') and
        number(r, 'yards_gained') >= 20 for r in drops)
    result['explosive_runs_10'] = sum(number(r, 'yards_gained') >= 10 for r in runs)
    result['explosive_passes_per_dropback'] = rate(result['explosive_passes_20'], len(drops))
    result['explosive_runs_per_designed_run'] = rate(result['explosive_runs_10'], len(runs))
    neutral = [r for r in plays if number(r, 'qtr') in (1, 3)
               and number(r, 'score_differential') is not None
               and abs(number(r, 'score_differential')) <= 7]
    result['neutral_plays'] = len(neutral)
    result['neutral_dropback_rate'] = rate(sum(flag(r, 'qb_dropback') for r in neutral), len(neutral))
    result['neutral_no_huddle_rate'] = rate(sum(flag(r, 'no_huddle') for r in neutral), len(neutral))
    rz = defaultdict(list)
    for r in selected:
        if r['posteam'] and r['fixed_drive']:
            rz[(r['game_id'], r['posteam'], r['fixed_drive'])].append(r)
    drives = [d for d in rz.values() if any(eligible(r) and
              number(r, 'yardline_100') is not None and number(r, 'yardline_100') <= 20 for r in d)]
    result['red_zone_drives'] = len(drives)
    result['red_zone_td_drives'] = sum(any(r['td_team'] == r['posteam'] and
        (flag(r, 'pass_touchdown') or flag(r, 'rush_touchdown')) for r in d) for d in drives)
    result['red_zone_td_rate'] = rate(result['red_zone_td_drives'], len(drives))
    return result


def main():
    source, output = map(Path, sys.argv[1:])
    with gzip.open(source, 'rt') as handle:
        rows = list(csv.DictReader(handle))
    assert {r['season'] for r in rows} == {'2025'}
    assert max(r['game_date'] for r in rows) == '2026-02-08'
    assert len({r['game_id'] for r in rows if r['season_type'] == 'REG'}) == 272
    records = [summarize(rows, t, p, u) for p in ('REG', 'POST', 'SB')
               for t in ('NE', 'SEA') for u in ('offense', 'defense')]
    # External cross-check: published NFL/club season and Super Bowl sack totals.
    expected = {('NE', 'REG'): 48, ('SEA', 'REG'): 27,
                ('NE', 'SB'): 6, ('SEA', 'SB'): 1}
    for r in records:
        if r['unit'] == 'offense' and (r['team'], r['phase']) in expected:
            assert r['sacks'] == expected[(r['team'], r['phase'])]
    output.mkdir(parents=True, exist_ok=True)
    with (output / 'baseline-2025.csv').open('w') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(records)
    target_rows = []
    for team in ('NE', 'SEA'):
        counts = Counter(r['receiver_player_name'] for r in rows if
            r['posteam'] == team and r['season_type'] == 'REG' and eligible(r)
            and flag(r, 'pass_attempt') and not flag(r, 'sack') and r['receiver_player_id'])
        for player, count in counts.most_common():
            target_rows.append({'team': team, 'player': player, 'targets': count,
                                'team_assigned_targets': sum(counts.values())})
    with (output / 'assigned-targets-2025.csv').open('w') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(target_rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(target_rows)
    manifest = {'source_url': 'https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_2025.csv.gz',
                'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                'computed_at_utc': datetime.now(timezone.utc).isoformat(),
                'rows': len(rows), 'season': 2025,
                'min_game_date': min(r['game_date'] for r in rows),
                'max_game_date': max(r['game_date'] for r in rows),
                'validation': '272 regular-season games; season and Super Bowl sack counts matched official totals'}
    (output / 'provenance.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(records, indent=2))


if __name__ == '__main__':
    main()
