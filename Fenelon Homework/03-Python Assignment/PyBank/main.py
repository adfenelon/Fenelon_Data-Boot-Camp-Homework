# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:15:01 2019

@author: fenel
"""

# Your task is to create a Python script that analyzes the records to calculate each of the following:

#import module
import os
import csv

csvpath ="Resources\budget_data.csv"
month_tally = 0
profit_loss = 0
previous_profit = 0
profit_list=[]
month_list=[]

with open(csvpath,"r") as datafile:
    reader = csv.reader(datafile)

#os.path("")   
    header = next(reader)
 
#print profit list    
    for row in reader:
        month_tally += 1
        profit_loss +=float(row[1])
        current_profit = float(row[1])
        if previous_profit !=0:
            change_profit= float(current_profit) - float(previous_profit )
            month_list.apend(row[0])
        previous_profit = current_profit

    #print profit list
    average_change = sum(profit_list)/85
    max_profit = max(profit_list)
    max_month = month_list[profit_list.index(max_profit)]
    min_profit = min(profit_list)
    min_month = month_list[profit_list.index(min_profit)]



# * The total number of months included in the dataset  
print("Total Months:" + str(month_tally))

#* The net total amount of "Profit/Losses" over the entire period
print("total:" + "$" +str(profit_loss))

#* The average of the changes in "Profit/Losses" over the entire period
print("Average Change:" +str(average_change))

#* The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits:" +str(max_month) + "$" +str(max_profit))

#* The greatest decrease in losses (date and amount) over the entire period
print("Greatest Decrease in Profits:" +str(min_month) + "$" +str(min_profit))






#Expected Results:
    #Total Months: 86
    #Total: $38382578
    #Average  Change: $-2315.12
    #Greatest Increase in Profits: Feb-2012 ($1926159)
    #Greatest Decrease in Profits: Sep-2013 ($-2196167)