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

Winning_votes = 0
total_votes = 0
Results = "Election Summary"
Blank = "------------------------------"

electioncsvpath = os.path.join('Resources','election_data.csv')

with open(electioncsvpath, "r") as datafile:
    election_reader = csv.reader(datafile)
    header = next(election_reader)
    election_data = csv.reader(datafile, delimiter=',')
   
    Candidates = []
    for row in election_reader:
        Candidates.append(row[2])
        total_votes = len(Candidates)
        
    Candidates_unique=list(set(Candidates))
    candidate_name = {}
    percentage_votes ={}
    
    for name in Candidates_unique:
        count=Candidates.count(name)
        candidate_name[name]=count
        percentage_votes[name] = round((candidate_name[name]/total_votes)*100,2)
    
    for z in candidate_name:
        if(candidate_name[z] > Winning_votes):
            Winning_votes = candidate_name[z]
            Winner = z

Tooley_P = percentage_votes["O'Tooley"]
Tooley_Total = candidate_name["O'Tooley"]

#print(Results)
#print(Blank)
#print("Total votes:" + " " + str(total_votes))
#print(Blank)
#print(f'{Candidates_unique[1]}: {percentage_votes["Khan"]}% ({candidate_name["Khan"]})')
#print(f'{Candidates_unique[3]}: {Tooley_P}% ({Tooley_Total})')
#print(f'{Candidates_unique[0]}: {percentage_votes["Li"]}% ({candidate_name["Li"]})')
#print(f'{Candidates_unique[2]}: {percentage_votes["Correy"]}% ({candidate_name["Correy"]})')
#print(Blank)
#print(f'Winner: {Winner}')
#print(Blank)

Summary = (f'{Results}\n'
           f'{Blank}\n'
           f'{"Total votes:" + " " + str(total_votes)}\n'
           f'{Blank}\n'
           f'{Candidates_unique[1]}: {percentage_votes["Khan"]}% ({candidate_name["Khan"]})\n'
           f'{Candidates_unique[3]}: {Tooley_P}% ({Tooley_Total})\n'
           f'{Candidates_unique[0]}: {percentage_votes["Li"]}% ({candidate_name["Li"]})\n'
           f'{Candidates_unique[2]}: {percentage_votes["Correy"]}% ({candidate_name["Correy"]})\n'
           f'{Blank}\n'
           f'Winner: {Winner}\n'
           f'{Blank}\n')
print(Summary)

polloutput_file = os.path.join("election_summary.txt")
with open(polloutput_file, "w", newline="") as textfile:
    writer = textfile.write(Summary)
 

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
    
