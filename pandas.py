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

