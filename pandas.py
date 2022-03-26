# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:06:28 2021

@author: Manoj
"""
import pandas as pd
file = "C:/Users/Manoj/Documents/pandas/a and b.xlsx"
newData = pd.read_excel(file)
print("mean=", newData.mean())
print("median=", newData.median())
print('mode=', newData.mode())
print("std="newData.std())
print("var"newData.var())'
print("KURT"newdata.kurt())
