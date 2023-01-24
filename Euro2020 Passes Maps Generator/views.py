import matplotlib.pyplot as plt
import numpy as np
import json
from FCPython import createPitch
from io import StringIO
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import pandas as pd
from pandas.io.json import json_normalize
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import io
from io import StringIO


# Create your views here.


def home(request):

    return render(request, 'home.html')


def get_players(request, match_id):
    file_name = str(match_id) + '.json'

    with open('E:/FootballAnalysis/django_projects/firstproject/json/' + file_name) as data_file:
        data = json.load(data_file)

    # Read Json File as DataFrame
    df = pd.json_normalize(data, sep="_").assign(match_id=file_name[:-5])

    # Create List of Player Names
    lineup_df = df.loc[df['type_name'] == 'Starting XI']
    team1_players = []
    for i in range(11):
        name = lineup_df['tactics_lineup'][0][i]['player']['name']
        name = name.encode('cp1252').decode('utf8')
        team1_players.append(name)
    team2_players = []
    for i in range(11):
        name = lineup_df['tactics_lineup'][1][i]['player']['name']
        name = name.encode('cp1252').decode('utf8')
        team2_players.append(name)

    return render(request, 'match.html', {'team1_players': team1_players, 'team2_players': team2_players, 'match_id': match_id})


def load_passes_df(match_id):

    file_name = str(match_id) + '.json'

    with open('E:/FootballAnalysis/django_projects/firstproject/json/' + file_name) as data_file:
        data = json.load(data_file)

    # Read Json File as DataFrame
    df = pd.json_normalize(data, sep="_").assign(match_id=file_name[:-5])

    # A dataframe of passes
    passes_df = df.loc[df['type_name'] == 'Pass']

    return passes_df


def createPassMap(playername, pass_df):
    # Size of the pitch in yards
    pitchLengthX = 120
    pitchWidthY = 80
    # Draw the pitch
    (fig, ax) = createPitch(pitchLengthX, pitchWidthY, 'yards', 'gray')
    for j, passa in pass_df.iterrows():
        x = passa['location'][0]
        y = passa['location'][1]
        dx = passa['pass_end_location'][0]
        dy = passa['pass_end_location'][1]
        if passa['player_name'] == playername:
            circleSize = 0.75
            passStart = plt.Circle((x, pitchWidthY - y), circleSize, color="red")
            arr = plt.Arrow(x=x, y=pitchWidthY-y, dx=dx-x, dy=dy-y, width=2.5)
            ax.add_patch(passStart)
            ax.add_patch(arr)
    plt.savefig("E:/FootballAnalysis/django_projects/firstproject/app1/static/imgs/newimg.jpg")


def create_players_lists(match_id):
    file_name = str(match_id) + '.json'

    with open('E:/FootballAnalysis/django_projects/firstproject/json/' + file_name) as data_file:
        data = json.load(data_file)

    # Read Json File as DataFrame
    df = pd.json_normalize(data, sep="_").assign(match_id=file_name[:-5])

    lineup_df = df.loc[df['type_name'] == 'Starting XI']
    team1_players = []
    for i in range(11):
        team1_players.append(lineup_df['tactics_lineup'][0][i]['player']['name'])
    team2_players = []
    for i in range(11):
        team2_players.append(lineup_df['tactics_lineup'][1][i]['player']['name'])

    return team1_players, team2_players


def selectHomeTeamPlayer(num):
    createPassMap(team1_players[num], passes_df)


def selectAwayTeamPlayer(num):
    createPassMap(team2_players[num], passes_df)


def get_stats(request, match_id, player_id, ha):
    team1, team2 = create_players_lists(match_id)
    pass_df = load_passes_df(match_id)
    if ha == 'h':
        createPassMap(team1[player_id - 1], pass_df)
    elif ha == 'a':
        createPassMap(team2[player_id - 1], pass_df)
    return render(request, 'stats.html')
