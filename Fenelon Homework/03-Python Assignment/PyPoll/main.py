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
            percentage_votes[name] = round((candidate_name[name]/total_votes)*100)

    print(Summary)
    print(Blank)
    print("Total votes:"+ " " + str(total_votes))
    print(Blank)
    print("List of candidates:"+ " " + str(Candidates_unique))
    print("Votes per candidate:" + " " + str(candidate_name))
    print("Percentage vote per candidate:"+" " + str(percentage_votes) + )
    print(Blank)
    #print("Winner: ")
    print(Blank)

Election_Results = {'khan:': [percentage vote




#polloutput_file = os.path.join("election_summary.csv")
#
#with open(polloutput_file, "w", newline="") as datafile:
#    writer = csv.writer(datafile)
#




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