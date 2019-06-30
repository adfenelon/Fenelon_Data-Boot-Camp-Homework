# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:07:09 2019

@author: fenel
"""
import os
import csv

budget_csvpath = os.path.join("..", "Resources", "budget_data.csv")

monthly_tally=0
profit_loss=0
previous_profit=0
profit_list=[]
month_list=[]

with open(budget_csvpath, "r") as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=",")
    
    header = next(bankreader)
    
    for row in budgetreader:
        month_tally +=1
        profit_loss += float(row[1])
        current_profit= float(row[1])
        if previous_profit !=0:
            change_profit= float(current_profit) - float(previous_profit)
            profit_list.append(row[0])
        previous_profit = current_profit

    average_change = sum(profit_list)/85
    max_profit = max(profit_list)
    max_month = month_list[profit_list.index(max_profit)]
    min_profit = min(profit_list)
    min_month = month_list[profit_list.index(min_profit)]
    
Print("Total Months: " + str(month_tally))
print("Total: " + "$" + str(profit_loss))
print("Average Change:" + str(average_change))
print("Greatest Increase in Profits:" + str(max_month) + "$" + str(max_profit))
print("Greatest Deacrease in Profits:" + str(min_month) + "$" + str(min_profit))

bankoutput_file = os.path.join("bank_summary.csv")

with open(bankoutput_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
