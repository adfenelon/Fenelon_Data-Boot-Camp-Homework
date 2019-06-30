# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:03:48 2019

@author: fenel
"""


## PyPoll

#![Vote-Counting](Images/Vote_counting.png)

#* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

import os
import csv

Voter_ID_Tally = 0
Summary = "Election Results"
Blank = "------------------------------"

electioncsvpath = os.path.join('Resources','election_data.csv')

with open(electioncsvpath, "r") as datafile:
    election_reader = csv.reader(datafile, delimiter=',')
    header = next(election_reader)

    Candidates = []

#* The total number of votes cast
    for row in election_reader:
        Candidates.apend(row[2])
        
    Total_Votes = len(Candidates)

print("Total Votes:" + Str(Voter_ID_Tally))

print(Blank)

print(Summary)

print(blank)

#* A complete list of candidates who received votes
candidates_unique = list(set(Candidates)


#* The percentage of votes each candidate won
percent = round(int(row[3]) / int(row[5]), 2)
        review_percent.append(percent)
#* The total number of votes each candidate won
#* The winner of the election based on popular vote.

print(Summary)
print(Blank)
print(":" + Str(Voter_ID_Tally))
print(Blank)
Print(":" + Str() +)
Print(":" + Str() +)
Print(":" + Str() +)
Print(":" + Str() +)
Print(Blank)
Print("Winner: ")
Print(Blank)


polloutput_file = os.path.join("election_summary.csv")

with open(polloutput_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)





#Expected Output :#* As an example, your analysis should look similar to the one below:

    #  ```text
    #  Election Results
    #  -------------------------
    #  Total Votes: 3521001
    #  -------------------------
    #  Khan: 63.000% (2218231)
    #  Correy: 20.000% (704200)
    #  Li: 14.000% (492940)
    #  O'Tooley: 3.000% (105630)
    #  -------------------------
    #  Winner: Khan
    #  -------------------------