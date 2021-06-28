# Bootcamp homework PyPoll

# Analyse votes for local election

import os
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')

count_votes = 0
candidates = []
votes =[]
candidate_count = []
percent_votes = []

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    print(f"csvheader: {csv_header}")

    # read in data and count the total number of votes
    for row in csvreader:
        count_votes +=1
        # for each row, check if the candidate has been identified previously
        # if not, add them to the list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        # store the vote, as the candidate name, in a list called "votes"
        votes.append(row[2])


# for each candidate, count number of votes they received
# add the result to a list of candidate vote counts
for person in candidates:
    c_count = 0
    for i in range(count_votes):
        if votes[i] == person:
            c_count +=1
    candidate_count.append(c_count)

# calculate percentage votes and add to list of percent_votes
for j in range(len(candidates)):
    percent_votes.append(round((candidate_count[j]/count_votes *100),3))
        
winner = candidates[candidate_count.index(max(candidate_count))]


print("")
print("Election Results")
print("------------------------------")
print(f"Total Votes: {count_votes}") 
print("------------------------------")
for j in range(len(candidates)):
    print(f"{candidates[j]} : {percent_votes[j]}% ({candidate_count[j]})")
print("------------------------------")   
print(f"Winner: {winner}")  
print("------------------------------")

# Specify the file to write to
output_path = os.path.join("analysis", "election_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text:

    
    
    text.write("Election Results \n")
    text.write("------------------------------ \n")
    text.write(f"Total Votes: {count_votes} \n") 
    text.write("------------------------------ \n")
    for j in range(len(candidates)):
        text.write(f"{candidates[j]} : {percent_votes[j]}% ({candidate_count[j]}) \n")

    text.write("------------------------------ \n")   
    text.write(f"Winner: {winner} \n")  
    text.write("------------------------------ \n")