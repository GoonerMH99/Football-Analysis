from statsbombpy import sb
import pandas as pd
import matplotlib.pyplot as plt
import mplsoccer

def getEkongStat(event_type):
    dataframe = pd.DataFrame()
    for i in range(len(nigeria_matches_ids)):
        events = sb.events(nigeria_matches_ids[i])
        ekong_events = events[events['player_id'] == 5455]
        stat = ekong_events[ekong_events['type'] == event_type]
        dataframe = dataframe._append(stat)

    return dataframe['location']

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

# -------------------Calculating average xG per shot of all Ekong shots-------------------------------------------------

shots_df = pd.DataFrame()
for i in range(len(nigeria_matches_ids)):
    events = sb.events(nigeria_matches_ids[i])
    ekong_events = events[events['player_id'] == 5455]
    shots = ekong_events[ekong_events['type'] == 'Shot']
    shots_df = shots_df._append(shots)

xG_List = [shots_df['shot_statsbomb_xg'].values][0]
print(sum(xG_List) / len(xG_List))

# ------------------Retrieving the number of times William Troost-Ekong received a ball---------------------------------
receipt_loc_df = getEkongStat('Ball Receipt*')
x_loc = []
y_loc = []
for i in range(len(receipt_loc_df)):
    x_loc.append(receipt_loc_df.iloc[i][0])
    y_loc.append(receipt_loc_df.iloc[i][1])

# Plotting a heat map highlighting the positions in which he received the ball the most
pitch = mplsoccer.Pitch(pitch_color='grass', line_color='white', line_zorder=2)
fig, ax = pitch.draw(figsize=(8, 16))
# customcmap = matplotlib.colors.LinearSegmentedColormap.from_list('custom cmap', ['black', 'red'])
pitch.kdeplot(x_loc, y_loc, ax=ax, cmap='Reds', fill=True, n_levels=100)
plt.show()