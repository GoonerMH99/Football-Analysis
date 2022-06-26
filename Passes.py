# Make a shot map and a pass map using Statsbomb data
# Set match id in match_id_required.

# Function to draw the pitch
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Load in all match events
import json
from pandas.io.json import json_normalize
# Draw the pitch
from FCPython import createPitch

# Size of the pitch in yards (!!!)
pitchLengthX = 120
pitchWidthY = 80

# ID for England vs Sweden Womens World Cup
match_id_required = 69301
home_team_required = "England Women's"
away_team_required = "Sweden Women's"

# Load in the data
# I took this from https://znstrider.github.io/2018-11-11-Getting-Started-with-StatsBomb-Data/
file_name = str(match_id_required) + '.json'


with open('E:/FootballAnalysis/open-data-master/data/events/' + file_name) as data_file:
    # print (mypath+'events/'+file)
    data = json.load(data_file)

# get the nested structure into a dataframe
# store the dataframe in a dictionary with the match id as key (remove '.json' from string)
df = pd.json_normalize(data, sep="_").assign(match_id=file_name[:-5])
# A dataframe of shots
shots = df.loc[df['type_name'] == 'Shot'].set_index('id')
passes_df = df.loc[df['type_name'] == 'Pass']
# Draw the pitch
(fig, ax) = createPitch(pitchLengthX, pitchWidthY, 'yards', 'gray')

# Plot the shots
for i, passa in passes_df.iterrows():
    team_name = passa['team_name']
    x = passa['location'][0]
    y = passa['location'][1]
    dx = passa['pass_end_location'][0]
    dy = passa['pass_end_location'][1]
    if team_name == away_team_required and passa['player_name'] == 'Sara Caroline Seger' and x < dx:
        circleSize = 0.75
        passStart = plt.Circle((x, pitchWidthY - y), circleSize, color="red")
        arr = plt.Arrow(x=x, y=pitchWidthY-y, dx=dx-x, dy=dy-y, width=2.5)
        ax.add_patch(passStart)
        ax.add_patch(arr)

# fig.set_size_inches(10, 7)
# fig.savefig('Output/shots.pdf', dpi=100)
plt.show()

# Exercise:
# 1, Create a dataframe of passes which contains all the passes in the match
# 2, Plot the start point of every Sweden pass. Attacking left to right.
# 3, Plot only passes made by Caroline Seger (she is Sara Caroline Seger in the database)
# 4, Plot arrows to show where the passes we
