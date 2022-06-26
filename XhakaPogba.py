# Make a shot map and a pass map using Statsbomb data
# Set match id in match_id_required.

# Function to draw the pitch
import math

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

# Load in the data
# I took this from https://znstrider.github.io/2018-11-11-Getting-Started-with-StatsBomb-Data/
FranceMatches = ['3788751', '3788763', '3788773']
SuissMatches = ['3788744', '3788754', '3788765']
i = 0
Xhaka_Total_Passes = 0
Xhaka_Forward_Passes = 0
Xhaka_Succesful_Passes = 0
while i < 3:
    match_id_required = SuissMatches[i]
    file_name = str(match_id_required) + '.json'

    with open('E:/FootballAnalysis/open-data-master/data/events/' + file_name, encoding='utf-8') as data_file:
        data = json.load(data_file)

    df = pd.json_normalize(data, sep="_").assign(match_id=file_name[:-5])
    for j, event in df.iterrows():
        away = event['index'] == 2 and event['team_name'] == 'Switzerland'
        if event['type_name'] == 'Pass':
            if event['player_name'] == 'Granit Xhaka':
                Xhaka_Total_Passes += 1
                if math.isnan(event['pass_outcome_id']):
                    Xhaka_Succesful_Passes += 1
                if away:
                    if event['pass_end_location'][0] > event['location'][0] + 10 and math.isnan(event['pass_outcome_id']):
                        Xhaka_Forward_Passes += 1
                else:
                    if event['pass_end_location'][0] < event['location'][0] - 10 and math.isnan(event['pass_outcome_id']):
                        Xhaka_Forward_Passes += 1
    i += 1
print(Xhaka_Forward_Passes)
print(Xhaka_Succesful_Passes)
print(Xhaka_Total_Passes)
Xhaka_Pass_Completion_Percentage = (Xhaka_Succesful_Passes/Xhaka_Total_Passes) * 100
Xhaka_Progressive_Passes_Percentage = (Xhaka_Forward_Passes/Xhaka_Total_Passes) * 100
print(Xhaka_Pass_Completion_Percentage)
print(Xhaka_Progressive_Passes_Percentage)
i = 0
Pogba_Total_Passes = 0
Pogba_Forward_Passes = 0
Pogba_Succesful_Passes = 0
while i < 3:
    match_id_required = FranceMatches[i]
    file_name = str(match_id_required) + '.json'

    with open('E:/FootballAnalysis/open-data-master/data/events/' + file_name, encoding='utf-8') as data_file:
        data = json.load(data_file)

    df = pd.json_normalize(data, sep="_").assign(match_id=file_name[:-5])
    for j, event in df.iterrows():
        away = event['index'] == 2 and event['team_name'] == 'France'
        if event['type_name'] == 'Pass':
            if event['player_name'] == 'Paul Pogba':
                Pogba_Total_Passes += 1
                if math.isnan(event['pass_outcome_id']):
                    Pogba_Succesful_Passes += 1
                if away:
                    if event['pass_end_location'][0] > event['location'][0] + 10 and math.isnan(event['pass_outcome_id']):
                        Pogba_Forward_Passes += 1
                else:
                    if event['pass_end_location'][0] < event['location'][0] - 10 and math.isnan(event['pass_outcome_id']):
                        Pogba_Forward_Passes += 1
    i += 1

print(Pogba_Forward_Passes)
print(Pogba_Succesful_Passes)
print(Pogba_Total_Passes)
Pogba_Pass_Completion_Percentage = (Pogba_Succesful_Passes/Pogba_Total_Passes) * 100
Pogba_Progressive_Passes_Percentage = (Pogba_Forward_Passes/Pogba_Total_Passes) * 100
print(Pogba_Pass_Completion_Percentage)
print(Pogba_Progressive_Passes_Percentage)


# fig.set_size_inches(10, 7)
# fig.savefig('Output/shots.pdf', dpi=100)


x = [Xhaka_Pass_Completion_Percentage, Pogba_Pass_Completion_Percentage]
y = [Xhaka_Progressive_Passes_Percentage, Pogba_Progressive_Passes_Percentage]

plt.scatter(x, y, color="green", s=30)

plt.xlabel('Succesful Passes')
plt.ylabel('Progressive Passes')

plt.xlim([74, 96])
plt.ylim([0, 20])

annotations = ["Granit Xhaka", "Paul Pogba"]
for k, label in enumerate(annotations):
    plt.annotate(label, (x[k], y[k]))
plt.show()
