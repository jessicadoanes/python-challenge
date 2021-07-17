# Import csv 
import os 
import csv 

# Round percentage results
def roundPercent(num):
    num = "{:.2%}".format(num)
    return num

# Path to collect and read data from source
inputfile = os.path.join("Resources","election_data.csv")
outputfile = os.path.join("Analysis", "PyPoll_results.txt")

# Lists and Variables 
total_votes = 0
winner_count = 0
candidates = []
uniquecandidates = []
vote_counts = []
num_votes = []
percent_votes  = [] 

#Open and read csv
with open (inputfile, 'r') as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    
    # Read the headers 
    csv_header = next(election_data)
    
    # Read the header of each row 
    # Loop counting names and votes in file
    for row in election_data:
       total_votes += 1

       if row[2] not in uniquecandidates: 
           uniquecandidates.append(row[2])
           vote_counts.append(1)   
    
    else:
            candidate_index = uniquecandidates.index(row[2])
            vote_counts[candidate_index] + 1

# Percentage of vites for each candidate
for i in range(len(vote_counts)):
    percent_votes.append(vote_counts[i] / total_votes)

# Winner based on most votes
for i in range(len(vote_counts)):

    if vote_counts[i] > winner_count:
        winner_count = vote_counts[i]
        winner = uniquecandidates[i]

outputfile = os.path.join("Analysis", "PyPoll_results.txt")

# fingers crossed for results 
with open(outputfile, 'w') as textfile:
    textfile.write(f"Election Results\n"
                   f"----------------\n"
                   f"Total Votes: {total_votes}\n"
                   f"-----------------\n"
                   )

for i in range(len(uniquecandidates)):
    textfile.write(f"{uniquecandidates[i]}: {roundPercent(percent_votes[i])} ({vote_counts[i]})\n")

textfile.write(f"--------------------\n"
                f"Winner: {winner}\n"
                f"--------------------\n"
                )

with open (outputfile, 'r') as analysis: 
    contents = analysis.read()
    print(contents)