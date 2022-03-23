# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:06:28 2021

@author: Manoj
"""
import pandas as pd
import pandas as ph
file = "C:/Users/Manoj/Documents/pandas/a and b.xlsx"
newData = ph.read_excel(file)
newData
print("mean", newData.mean())
print("median", newData.median())
print('mode', newData.mode())
print(newData.std())
print(newData.var())

import pandas as pd
ipl = pd.read_csv("C:/Users/Manoj/Downloads/ipl/IPL Matches 2008-2020.csv")
ipl.head()
ipl.tail()
ipl.head(10)
ipl.tail(10)
ipl.info()
ipl.result_margin.mean()
ipl.result_margin.mode()
ipl.result_margin.median()
ipl.result_margin.std()
ipl.result_margin.var()
ipl.result_margin.skew()
ipl.result_margin.kurt()
ipl.result_margin.hist()

ipl.winner.mode()
ipl.winner.value_counts()

ipl.venue.value_counts()
ipl.shape
ipl.size
ipl.columns
ipl.team1.mode()
ipl.team2.mode()
ipl.team1.value_counts()
ipl.team2.value_counts()
ipl.drop(['neutral_venue'],axis=1)
ipl1=ipl.drop(['neutral_venue'],axis=1)
ipl1.columns
ipl=ipl.drop(['neutral_venue'],axis=1)
ipl.drop("method",axis=1, inplace=True)
ipl.winner
ipl.winner.unique()
ipl.winner.nunique()
list1=["rise","sugar","salt","masala"]
list1[2]
ipl.iloc[0,:]
ipl.iloc[10,:]
ipl.loc[:,'team1']
ipl['team1']
ipl.loc[2:10,'city']
ipl.loc[2:11]
wickets=ipl[ipl.result=="wickets"]
runs=ipl[ipl.result=="runs"]
tie=ipl[ipl.result=="tie"]
ipl.result.unique()
runs.result_margin.max()
runs[runs.result_margin==146]
runs.winner[runs.result_margin==runs.result_margin.max()]
runs.winner[runs.result_margin==runs.result_margin.min()]
wickets[wickets.result_margin==10]
runs.wickets[runs.result_margin==runs.result_margin.max()]
wickets.winner[wickets.result_margin==wickets.result_margin.max()]
wickets.winner[wickets.result_margin==wickets.result_margin.max()]
wickets.winner[wickets.result_margin==wickets.result_margin.max()].value_counts()
