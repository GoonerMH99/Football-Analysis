"""Import Statements"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import seaborn as sns

"""Read Dataset"""
epl_df = pd.read_csv("EPL_20_21.csv", encoding_errors='ignore', error_bad_lines=False)

"""Add Columns"""
epl_df['MinsPerMatch'] = (epl_df['Mins'] / epl_df['Matches']).astype(int)
epl_df['GoalsPerMatch'] = (epl_df['Goals'] / epl_df['Matches']).astype(float)

"""Create Descriptive Variables"""
tot_goals = epl_df['Goals'].sum()
positions = epl_df['Position'].unique()

"""Plotting"""
# plt.figure(figsize=(13, 6))
# miss_pens = epl_df['Penalty_Attempted'].sum() - epl_df['Penalty_Goals'].sum()
# data = [miss_pens, epl_df['Penalty_Goals'].sum()]
# lebels = ["Missed Penalties", "Scored Penalties"]
# plt.pie(data, labels=lebels, autopct='%.0f%%')
# plt.show()

"""Select Subsets"""
forwards = epl_df.loc[epl_df['Position'] == 'FW', 'Name']
under20 = epl_df[epl_df['Age'] < 20]

"""Nationalities of Players Count"""
nations = epl_df.groupby('Nationality').size().sort_values(ascending=False)
# nations.head().plot(kind='bar', figsize=(10, 10))

# similar to 2 previous lines
# nations = epl_df['Nationality'].value_counts().nsmallest(5).plot(kind='bar', figsize=(10, 10))


"""Average age of each club"""
avg_age = epl_df.groupby('Club')['Age'].sum() / epl_df.groupby('Club')['Age'].size()
# print(avg_age)


"""Total assists of each club"""
# tot_ass = pd.DataFrame(epl_df.groupby('Club', as_index=False)['Assists'].sum())
# tot_ass = tot_ass.sort_values(by="Assists")
#
# sns.set_theme(style="whitegrid", color_codes=True)
# ax = sns.barplot(x=tot_ass['Club'], y=tot_ass['Assists'], data=tot_ass, palette='Set2')
# ax.set_xlabel("Club", fontsize=30)
# ax.set_ylabel("Assists", fontsize=20)
# plt.xticks(rotation=75)
# plt.ylim([0, 60])
#
# ax.yaxis.set_major_locator(MultipleLocator(10))
# ax.yaxis.set_minor_locator(AutoMinorLocator(4))
# ax.grid(which='minor', color='#CCCCCC', linestyle=':')
#
# plt.rcParams["figure.figsize"] = (25, 10)
# plt.show()


"""Top 10 Players in Assists"""
# top_ass = epl_df.sort_values(by="Assists").tail(10)
#
# sns.set_theme(style="whitegrid", color_codes=True)
# ax = sns.barplot(x=top_ass['Name'], y=top_ass['Assists'], data=top_ass, palette='Set2')
# ax.set_xlabel("Club", fontsize=30)
# ax.set_ylabel("Assists", fontsize=20)
# plt.xticks(rotation=75)
# plt.ylim([0, 25])
#
# ax.yaxis.set_major_locator(MultipleLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
# ax.grid(which='minor', color='#CCCCCC', linestyle=':')
#
# plt.rcParams["figure.figsize"] = (25, 10)
# plt.show()
#
# print(top_ass[['Name', 'Club', 'Assists', 'Matches']])


"""Top 10 GoalScorers"""
top_goals = epl_df[['Name', 'Club', 'Goals', 'Matches']].nlargest(n=10, columns='Goals')
print(top_goals)


# print(epl_df.head())
# print(epl_df.info())
# print(epl_df.describe())
