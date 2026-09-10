"""Historical NE/SEA contextual tables. Local inputs only; see README.md.

Usage: python3 compute_context.py PBP.csv.gz FTN.csv PFR_SEASON.csv PFR_WEEK.csv NGS.csv.gz OUTPUT
FTN-derived outputs: attribution to FTN Data via nflverse; CC BY-SA 4.0.
"""
import csv
import gzip
import hashlib
import importlib.util
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

spec = importlib.util.spec_from_file_location('baseline', Path(__file__).parents[1] / 'compute_baseline.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def read(path):
    opener = gzip.open if path.suffix == '.gz' else open
    with opener(path, 'rt') as handle:
        return list(csv.DictReader(handle))


def write(path, rows):
    with path.open('w') as handle:
        out = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator='\n')
        out.writeheader()
        out.writerows(rows)


def avg(rows):
    return sum(float(r['epa']) for r in rows) / len(rows)


def fnum(row, key):
    return b.number(row, key)


def boolean(row, key):
    value = row.get(key, '').upper()
    return {'TRUE': True, 'FALSE': False}.get(value)


def main():
    pbp_file, ftn_file, pfr_file, week_file, ngs_file, out = map(Path, sys.argv[1:])
    raw, ftn, pfr, weeks, ngs = map(read, [pbp_file, ftn_file, pfr_file, week_file, ngs_file])
    assert {r['season'] for r in raw} == {'2025'}
    assert {r['season'] for r in ftn} == {'2025'}
    assert max(r['game_date'] for r in raw) == '2026-02-08'
    index = {(r['nflverse_game_id'], r['nflverse_play_id']): r for r in ftn}
    assert len(index) == len(ftn), 'Duplicate FTN play keys'
    plays = [r for r in raw if b.eligible(r)]
    assert len({r['game_id'] for r in raw if r['season_type'] == 'REG'}) == 272
    out.mkdir(parents=True, exist_ok=True)
    summaries, rushes, rz = [], [], []
    for team in ['NE', 'SEA']:
        for phase in ['REG', 'POST', 'SB']:
            def in_phase(r):
                return r['game_id'] == '2025_22_SEA_NE' if phase == 'SB' else r['season_type'] == phase
            for unit, side in [('offense', 'posteam'), ('defense', 'defteam')]:
                selected = [r for r in plays if r[side] == team and in_phase(r)]
                pairs = [(r, index.get((r['game_id'], r['play_id']))) for r in selected]
                joined = [(r, f) for r, f in pairs if f is not None]
                # Complete row matching does not imply every field is known.
                assert len(joined) == len(selected), (team, phase, unit, 'unmatched FTN plays')
                drops = [(r, f) for r, f in joined if b.flag(r, 'qb_dropback')]
                uc = [(r, f) for r, f in joined if f['qb_location'] in ['U', 'S', 'P']]
                motion = [(r, f) for r, f in joined if boolean(f, 'is_motion') is not None]
                pa = [(r, f) for r, f in drops if boolean(f, 'is_play_action') is not None]
                parows = [r for r, f in pa if boolean(f, 'is_play_action')]
                noparows = [r for r, f in pa if not boolean(f, 'is_play_action')]
                record = dict(team=team, phase=phase, unit=unit, eligible_plays=len(selected), joined_plays=len(joined),
                    qb_location_known=len(uc), under_center=sum(f['qb_location'] == 'U' for r, f in uc),
                    motion_known=len(motion), motion_plays=sum(boolean(f, 'is_motion') for r, f in motion),
                    dropbacks=len(drops), play_action_known=len(pa), play_action_dropbacks=len(parows),
                    play_action_epa=round(avg(parows), 6) if parows else '',
                    non_play_action_epa=round(avg(noparows), 6) if noparows else '')
                summaries.append(record)
                for group in ['0_or_unknown', '1_to_3', '4', '5_plus']:
                    subset=[]
                    for r,f in drops:
                        n=fnum(f,'n_pass_rushers')
                        label='0_or_unknown' if n is None or n == 0 else '1_to_3' if n < 4 else '4' if n == 4 else '5_plus'
                        if label == group:subset.append((r,f))
                    sacks=[(r,f) for r,f in subset if b.flag(r,'sack')]
                    rushes.append(dict(team=team,phase=phase,unit=unit,rusher_group=group,dropbacks=len(subset),
                        sacks=len(sacks),sack_rate=round(len(sacks)/len(subset),6) if subset else '',
                        epa_per_dropback=round(avg([r for r,f in subset]),6) if subset else '',
                        qb_fault_sack_known=sum(boolean(f,'is_qb_fault_sack') is not None for r,f in sacks),
                        qb_fault_sacks=sum(boolean(f,'is_qb_fault_sack') is True for r,f in sacks)))
            # PBP opportunity history; no routes inferred from targets.
            own=[r for r in plays if r['posteam']==team and in_phase(r)]
            for area, boundary in [('inside_20',20),('inside_5',5)]:
                subset=[r for r in own if fnum(r,'yardline_100') is not None and 0 < fnum(r,'yardline_100') <= boundary]
                counts=defaultdict(lambda: [0,0])
                for r in subset:
                    if r['play_type']=='run' and not b.flag(r,'qb_scramble') and r['rusher_player_name']:
                        counts[r['rusher_player_name']][0]+=1
                    if b.flag(r,'pass_attempt') and not b.flag(r,'sack') and r['receiver_player_id']:
                        counts[r['receiver_player_name']][1]+=1
                for player, (carries,targets) in sorted(counts.items()):
                    rz.append(dict(team=team,phase=phase,area=area,player=player,designed_carries=carries,assigned_targets=targets))
    write(out/'ftn-tendencies.csv', summaries)
    write(out/'ftn-rusher-splits.csv', rushes)
    write(out/'historical-scoring-opportunities.csv', rz)
    # Box-score reconciliation uses a different sample from EPA: retain kneels and
    # spikes, exclude two-point attempts. Stevenson played all four NE playoff games.
    postseason = [r for r in raw if r['season_type'] == 'POST' and r['posteam'] == 'NE'
                  and r['play_type'] in ['run', 'pass', 'qb_kneel', 'qb_spike']
                  and not b.flag(r, 'two_point_attempt')]
    carries = [r for r in postseason if r['rusher_player_name'] == 'R.Stevenson' and b.flag(r, 'rush_attempt')]
    catches = [r for r in postseason if r['receiver_player_name'] == 'R.Stevenson' and b.flag(r, 'complete_pass')]
    box = dict(player='Rhamondre Stevenson', phase='POST_including_SB', games=len({r['game_id'] for r in postseason}),
               carries=len(carries), rush_yards=sum(float(r['rushing_yards']) for r in carries),
               rush_td=sum(b.flag(r, 'rush_touchdown') for r in carries), receptions=len(catches),
               rec_yards=sum(float(r['receiving_yards']) for r in catches),
               rec_td=sum(b.flag(r, 'pass_touchdown') for r in catches))
    assert (box['games'], box['carries'], box['rush_yards'], box['receptions'], box['rec_yards'], box['rec_td']) == (4, 58, 217, 12, 126, 1)
    write(out/'stevenson-postseason.csv', [box])
    # One-step opponent normalization, excluding all focal-team matchups from each opponent baseline.
    reg=[r for r in plays if r['season_type']=='REG'];league_mean=avg(reg)
    adjusted=[];opponent_details=[]
    for team in ['NE','SEA']:
        for unit,side,opponent_side in [('offense','posteam','defteam'),('defense','defteam','posteam')]:
            selected=[r for r in reg if r[side]==team]
            opponents=defaultdict(list)
            for r in selected:opponents[r[opponent_side]].append(r)
            weighted=0
            for opponent, observed in sorted(opponents.items()):
                reference=[r for r in reg if r[opponent_side]==opponent and r[side]!=team]
                assert reference
                rate=avg(reference);weighted+=len(observed)*rate
                opponent_details.append(dict(team=team,unit=unit,opponent=opponent,focal_plays=len(observed),
                    other_opponent_plays=len(reference),opponent_epa_elsewhere=round(rate,6)))
            strength=weighted/len(selected)
            adjusted.append(dict(team=team,unit=unit,plays=len(selected),raw_epa=round(avg(selected),6),
                league_epa=round(league_mean,6),weighted_opponent_epa_elsewhere=round(strength,6),
                schedule_component=round(strength-league_mean,6),normalized_epa=round(avg(selected)-(strength-league_mean),6)))
    write(out/'opponent-context.csv',adjusted);write(out/'opponent-detail.csv',opponent_details)
    # Preserve PFR definitions; never derive PFR pressure rate using the FTN/PBP denominator.
    pressure=[]
    reconciliations=[]
    for player,team,sacks in [('Drake Maye','NE',47),('Sam Darnold','SEA',27)]:
        rows=[r for r in pfr if r['player']==player and r['team']==team and r['season']=='2025'];assert len(rows)==1
        r=rows[0]
        weekly=[w for w in weeks if w['pfr_player_name']==player and w['game_type']=='REG']
        assert sum(int(w['times_sacked']) for w in weekly)==sacks
        assert len(weekly)==len({w['game_id'] for w in weekly})==17
        weekly_pressure=sum(int(w['times_pressured']) for w in weekly)
        # The downloaded Maye season and weekly snapshots differ by one hurry.
        # Preserve both definitions/snapshots; do not silently force agreement.
        assert int(r['times_hurried'])+int(r['times_hit'])+sacks==int(r['times_pressured'])
        assert all(int(w['times_hurried'])+int(w['times_hit'])+int(w['times_sacked'])==int(w['times_pressured']) for w in weekly)
        reconciliations.append(dict(player=player,season_pressures=int(r['times_pressured']),weekly_pressures=weekly_pressure,
            difference=weekly_pressure-int(r['times_pressured']),
            status='matched' if weekly_pressure==int(r['times_pressured']) else 'source_snapshot_conflict'))
        pressure.append(dict(player=player,team=team,phase='REG',sacks=sacks,hurries=r['times_hurried'],hits=r['times_hit'],
            pressures=r['times_pressured'],published_pressure_percent=r['pressure_pct'],pocket_time_seconds=r['pocket_time'],
            sacks_per_pressure=round(sacks/int(r['times_pressured']),6)))
        sb=[w for w in weeks if w['pfr_player_name']==player and w['game_type']=='SB'];assert len(sb)==1;w=sb[0]
        pressure.append(dict(player=player,team=team,phase='SB',sacks=w['times_sacked'],hurries=w['times_hurried'],hits=w['times_hit'],
            pressures=w['times_pressured'],published_pressure_percent=100*float(w['times_pressured_pct']),pocket_time_seconds='',
            sacks_per_pressure=round(int(w['times_sacked'])/int(w['times_pressured']),6)))
    write(out/'pfr-pressure.csv',pressure)
    write(out/'pfr-reconciliation.csv',reconciliations)
    ngs_rows=[r for r in ngs if r['season']=='2025' and r['season_type']=='REG' and r['week']=='0'
              and r['player_display_name'] in ['Drake Maye','Sam Darnold']]
    assert len(ngs_rows)==2
    write(out/'ngs-passing.csv',ngs_rows)
    source_urls=[
        'https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_2025.csv.gz',
        'https://github.com/nflverse/nflverse-data/releases/download/ftn_charting/ftn_charting_2025.csv',
        'https://github.com/nflverse/nflverse-data/releases/download/pfr_advstats/advstats_season_pass.csv',
        'https://github.com/nflverse/nflverse-data/releases/download/pfr_advstats/advstats_week_pass_2025.csv',
        'https://github.com/nflverse/nflverse-data/releases/download/nextgen_stats/ngs_passing.csv.gz']
    manifest={'computed_at_utc':datetime.now(timezone.utc).isoformat(),'season':2025,
        'ftn_attribution':'FTN Data via nflverse','ftn_license':'https://creativecommons.org/licenses/by-sa/4.0/',
        'inputs':[{'url':url,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
                  for url,path in zip(source_urls,[pbp_file,ftn_file,pfr_file,week_file,ngs_file])],
        'validation':'272 REG games; unique FTN keys; all NE/SEA eligible plays matched; PFR sacks cross-checked and within-source pressure components reconcile',
        'pfr_snapshot_reconciliation':reconciliations}
    (out/'context-provenance.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'tendencies':summaries,'opponent_context':adjusted,'pressure':pressure,'ngs':ngs_rows},indent=2))


if __name__=='__main__':main()
