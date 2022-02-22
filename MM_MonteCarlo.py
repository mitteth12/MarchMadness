#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 21:33:05 2022

@author: ethanmitten
"""

#https://www.youtube.com/watch?v=irjTWNV0eAY&list=WL&index=1

import pandas as pd
import random as rnd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/March Madness/Data/TeamCurrent2022_Season.csv')

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
    Yscore = (rnd.gauss(ymeanpts,ysdpts) + rnd.gauss(xmeanopp, xsdopp))/2
    if int(round(Xscore)) > int(round(Yscore)):
        return 1
    elif int(round(Xscore)) < int(round(Yscore)):
        return -1
    else: return 0

    
def gamesSim(team1,team2,ns):
    gamesout = []
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

gamesSim('Missouri', 'Nebraska',100)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    