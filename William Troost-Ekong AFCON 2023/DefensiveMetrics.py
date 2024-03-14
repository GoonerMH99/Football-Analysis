from statsbombpy import sb
import pandas as pd
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar


def getEkongStat(event_type):
    dataframe = pd.DataFrame()
    for i in range(len(nigeria_matches_ids)):
        events = sb.events(nigeria_matches_ids[i])
        ekong_events = events[events['player_id'] == 5455]
        stat = ekong_events[ekong_events['type'] == event_type]
        dataframe = dataframe._append(stat)

    return len(dataframe)


# Retrieving The Match IDs of all Nigeria Matches
i = 0
nigeria_matches_ids = []
while i < 52:
    Hteams = sb.matches(1267, 107)['home_team']
    Ateams = sb.matches(1267, 107)['away_team']
    ids = sb.matches(1267, 107)['match_id']
    if Hteams[i] == 'Nigeria' or Ateams[i] == 'Nigeria':
        nigeria_matches_ids.append(ids[i])
    i += 1
print(nigeria_matches_ids)


# ------------------------DEFENSIVE METRICS---------------------------------------


# Retrieving the number of times William Troost-Ekong got dribbled past
DrbPst = getEkongStat('Dribbled Past')


# Retrieving the number of times William Troost-Ekong got dispossessed
Dispossessed = getEkongStat('Dispossessed')


# Retrieving the number of times William Troost-Ekong made a clearance
clr = getEkongStat('Clearance')


# Retrieving the number of times William Troost-Ekong committed a foul
fouls = getEkongStat('Foul Committed')


# Retrieving the number of times William Troost-Ekong made a successful interception

succ_interceptions_df = pd.DataFrame()
for i in range(len(nigeria_matches_ids)):
    events = sb.events(nigeria_matches_ids[i])
    ekong_events = events[events['player_id'] == 5455]

    intercept_pass = ekong_events[(ekong_events['type'] == 'pass') & (ekong_events['pass_type'] == 'interception') & (ekong_events['pass_recipient'].notnull())]

    interceptions = ekong_events[ekong_events['type'] == 'Interception']
    succ_interceptions = interceptions[interceptions['interception_outcome'].isin(['Won', 'Success', 'Success In Play', 'Success Out'])]

    succ_interceptions_df = succ_interceptions_df._append(interceptions)
    succ_interceptions_df = succ_interceptions_df._append(intercept_pass)

interceptions = len(succ_interceptions_df)


# Retrieving the number of times William Troost-Ekong won an aerial duel

aerial_won_df = pd.DataFrame()
for i in range(len(nigeria_matches_ids)):
    events = sb.events(nigeria_matches_ids[i])
    ekong_events = events[events['player_id'] == 5455]

    aerial_clearance = ekong_events[(ekong_events['type'] == 'Clearance') & (ekong_events['clearance_aerial_won'].notnull())]
    #aerial_miscontrol = ekong_events[(ekong_events['type'] == 'miscontrol') & (ekong_events['miscontrol_aerial_won'].notnull())]
    aerial_shot = ekong_events[(ekong_events['type'] == 'shot') & (ekong_events['shot_aerial_won'].notnull())]
    aerial_pass = ekong_events[(ekong_events['type'] == 'pass') & (ekong_events['pass_aerial_won'].notnull())]

    aerial_won_df = aerial_won_df._append(aerial_clearance)
    # aerial_won_df = aerial_won_df._append(aerial_miscontrol)
    aerial_won_df = aerial_won_df._append(aerial_shot)
    aerial_won_df = aerial_won_df._append(aerial_pass)

aerial_duel = len(aerial_won_df)


# Retrieving the number of times William Troost-Ekong made a successful tackle

succ_tackle_df = pd.DataFrame()
for i in range(len(nigeria_matches_ids)):
    events = sb.events(nigeria_matches_ids[i])
    ekong_events = events[events['player_id'] == 5455]
    succ_tackles = ekong_events[(ekong_events['type'] == 'Duel') & (ekong_events['duel_type'] == 'Tackle') & (ekong_events['duel_outcome'].isin(['Won', 'Success', 'Success In Play', 'Success Out']))]
    succ_tackle_df = succ_tackle_df._append(succ_tackles)

succ_tackle = len(succ_tackle_df)

ranges = [(1.5, 0.0), (1.5, 0.0), (0.0, 8.0), (1.5, 0.0), (0.0, 1.5), (0.0, 1.5), (0.0, 1.5)]
params = ['DrbPst', 'Dispossessed', 'Clr', 'fouls', 'interceptions', 'aerial_won', 'succ_tackles']
values = [DrbPst / 6, Dispossessed / 6, clr/6, fouls/6, interceptions/6, aerial_duel/6, succ_tackle/6]
title = dict(
    title_name='William Troost-Ekong',
    title_color='black',
    subtitle_name='Nigeria',
    subtitle_color='green',
)
radar = Radar()
fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values, radar_color=['#B6282F', '#FFFFFF'], title=title)

plt.show()