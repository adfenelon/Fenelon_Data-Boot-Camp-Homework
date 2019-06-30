# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:07:09 2019

@author: fenel
"""

import csv
import os

bankcsvfile = "bank_data.csv"

monthly_tally=0
profit_loss=0
previous_profit=0
profit_list=[]
month_list=[]

with open(bankcsvpath, "r") as datafile:
    bankreader = csv.bankreader(datafile)
    
    header = next(bankreader)
    
    for row in bankreader:
        month_tally +=1
        profit_loss += float(row[1])
        current_profit= float(row[1])
        if previous_profit !=0:
            change_profit= float(current_profit) - float(previous_profit)
            profit_list.append(row[0])
        previous_profit = current_profit

    average_change = sum(profit_list)/85
    max_profit = max(profit_list)
    max_month = month_list