#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 21:33:05 2022

@author: ethanmitten
"""

#Structure based off of:
#https://www.youtube.com/watch?v=irjTWNV0eAY&list=WL&index=1

import pandas as pd
import random as rnd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/March Madness/Data/TeamCurrent2022_Season.csv')
df_sos_2021 = pd.read_html('https://www.warrennolan.com/basketball/2021/sos-rpi')[0]

df_sos_2021 = df_sos_2021.rename({'Team': 'School'}, axis=1)

data2 = data1.merge(df_sos_2021, on='School', how='left')

data = data2[["School", "Tm", "Opp", "SOS"]]

data.columns

data['Tm'] = data['Tm'].astype(int)
data['Opp'] = data['Opp'].astype(int)

def gameSim(team1, team2):
    x = data[data.School == team1]
    y = data[data.School == team2]
    xmeanpts = x.Tm.mean()
    ymeanpts = y.Tm.mean()
    xsdpts = x.Tm.std()
    ysdpts = y.Tm.std()
    xmeanopp = x.Opp.mean()
    ymeanopp = y.Opp.mean()
    xsdopp = x.Opp.std()
    ysdopp = y.Opp.std()
    Xscore = (rnd.gauss(xmeanpts,xsdpts) + rnd.gauss(ymeanopp, ysdopp))/2
    xscore = Xscore * data['SOS'].mean()
    Yscore = (rnd.gauss(ymeanpts,ysdpts) + rnd.gauss(xmeanopp, xsdopp))/2
    yscore = Yscore * data['SOS'].mean()
    if int(round(xscore)) > int(round(yscore)):
        return 1
    elif int(round(xscore)) < int(round(yscore)):
        return -1
    else: return 0

    
def gamesSim(team1,team2):
    gamesout = []
    ns = 1000
    team1win = 0
    team2win = 0
    tie = 0
    for i in range(ns):
        gm = gameSim(team1, team2)
        gamesout.append(gm)
        if gm == 1:
            team1win +=1
        elif gm == -1:
            team2win +=1
        else: tie +=1
    print(team1 + ' Win', team1win/(team1win+team2win+tie), '%')
    print(team2 + ' Win', team2win/(team1win+team2win+tie), '%')
    print('Tie', tie/(team1win+team2win+tie), '%')
    #return gamesout
    
    
data.School.unique()

gamesSim("Houston", "Auburn")





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    