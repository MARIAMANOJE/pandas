# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:27:30 2022

@author: Mano
"""


import pandas as pd
file = "C:/Users/Mano/Documents/pandas/a and b.xlsx"#choosefilepathwhereyousave
newData = pd.read_excel(file)
print("mean", newData.mean())
print("median", newData.median())
print('mode', newData.mode())
print("std",newData.std())
print("var",newData.var())
print("KURT",newData.kurt())
