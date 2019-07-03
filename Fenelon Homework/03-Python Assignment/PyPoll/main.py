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
Summary = "Election Results"
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
    print(candidate_name)
    
    for n in candidate_name:
        if(candidate_name[n] > Winning_votes):
            Winning_votes = candidate_name[n]
            Winner = n
   
    print(Summary)
    print(Blank)
    print("Total votes:" + " " + str(total_votes))
    print(Blank)
    print("List of candidates:"+ " " + str(Candidates_unique))
    print("Votes per candidate:" + " " + str(candidate_name))
    print("Percentage vote per candidate:" + " " + str(percentage_votes))
    print(Blank)
    print(f'Winner: {Winner}')
    print(Blank)
   
    print(f'{Candidates_unique[1]}: {percentage_votes["Khan"]}% {candidate_name["Khan"]}')
#    print(f'{Candidates_unique[0]}: {percentage_votes["O\'Tooley"]}% {candidate_name["O\'Tooley"]}')
    print(f'{Candidates_unique[2]}: {percentage_votes["Li"]}% {candidate_name["Li"]}')
    print(f'{Candidates_unique[3]}: {percentage_votes["Correy"]}% {candidate_name["Correy"]}')


for y in Candidates_unique:
    for z in percentage_votes:
        for t in candidate_name:
            print(y,z,t)






#polloutput_file = os.path.join("election_summary.txt")
#
#with open(polloutput_file, "w", newline="") as textfile:
#    writer = textfile.write()
#
#
#
#  
#for soda in candidate_name.keys():
#    print(soda)
    

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
    
