#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:23:49 2022

@author: ethanmitten
"""
#Notebook follow along from Ken Jee
#https://www.kaggle.com/kenjee/simple-simulation-elo-rating-approach
import numpy as np
import pandas as pd

df_seed = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/March Madness/Data/MNCAATourneySeeds.csv')
df_teams = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/March Madness/Data/MTeams.csv')

df_teams['tm_join'] = df_teams.TeamName.apply(lambda x: x.replace('St','State'))

#get 2021 data & join seed w/ team names
df_s_2021 = df_seed[df_seed['Season'] == 2021]
seed_tms = pd.merge(df_s_2021, df_teams.loc[:,['TeamID','TeamName','tm_join']], on='TeamID')

#df_elo = pd.read_html('https://www.warrennolan.com/basketball/2022/elo')[0]

#df_elo_final = df_elo.loc[:,['Team','ELO']]
#df_elo_final.head()

df_elo_2021 = pd.read_html('https://www.warrennolan.com/basketball/2020/sos')[0]

df_elo_final_2021 = df_elo_2021.loc[:,['Team','ELO']]
df_elo_final_2021.head()

#join elo data with team and seed data | fill in null values
seed_elos = pd.merge(seed_tms,df_elo_final_2021, left_on = 'tm_join',right_on = 'Team', how='left')

seed_elos.iloc[8,6] = 1597.16
seed_elos.iloc[13,6] = 1519.06
seed_elos.iloc[14,6] = 1481.20
seed_elos.iloc[16,6] = 1278.92
seed_elos.iloc[17,6] = 1395.14
seed_elos.iloc[32,6] = 1469.18

seed_elos.isnull().any()

#simple formula to get win probability from elo rating differential
def win_prob_t1(team1_elo,team2_elo):
    elo_diff_m = (team2_elo-team1_elo)/400
    t1_win_prob = 1/(1+10**elo_diff_m)
    return t1_win_prob


win_prob_t1(1901.46, 1000)


