# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:07:09 2019

@author: fenel
"""
import os
import csv

budget_csvpath = os.path.join("Resources", "budget_data.csv")

monthly_tally=0
profit_loss=0
previous_profit=0
profit_list=[]
month_list=[]
Blank = "------------------------------"

with open(budget_csvpath,"r") as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=",")
    
    header = next(budgetreader)
    
    for row in budgetreader:
        monthly_tally +=1
        profit_loss += float(row[1])
        current_profit= float(row[1])
        if previous_profit !=0:
            change_profit= float(current_profit) - float(previous_profit)
            profit_list.append(change_profit)
            month_list.append(row[0])
        previous_profit = current_profit

    average_change = round(sum(profit_list)/monthly_tally,0)
    max_profit = max(profit_list)
    max_month = month_list[profit_list.index(max_profit)]
    min_profit = min(profit_list)
    min_month = month_list[profit_list.index(min_profit)]

Summary =(f'Financial Analysis\n'
    f'{Blank}\n'      
    f'Total Months: {monthly_tally}\n'
    f'Total: ${profit_loss}\n'
    f'Average change:${average_change}\n'
    f'Greatest Increase in Profits: {max_month} (${max_profit})\n'
    f'Greatest decrease in Profits: {min_month} (${min_profit})\n')
print(Summary)
    

bankoutput_file = os.path.join("Resources","bank_summary.txt")

with open(bankoutput_file, "w", newline="") as textfile:
    writer = textfile.write(Summary)

    
