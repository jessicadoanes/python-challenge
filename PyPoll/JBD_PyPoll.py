# Import csv 
import os 
import csv 

# Path to collect and read data from source
election_data_csv = os.path.join ('.','PyPoll','Resources','election_data.csv')

with open (election_data_csv, 'r') as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')

    print(election_data_csv)

    csv_header = next(election_data_csv)
    print(f"CSV Header: {csv_header}")

    for column in election_data_csv:
       votes.append(column[0])
       county.append(column[1])
       candidates.append(column[2])

# Define the function 
def print_results(election_data):

# Lists to store data
    voterid = str(election_data[0])
    county = str(election_data[1])
    candidates = str(election_data[2])

# Variables 
votes = 0 
total_votes = 0
candidates = 0
Khan_percentage = 0 
Correy_percentage= 0
Li_percentage = 0
O_Tooley_percentage = 0

# The total number of votes cast
total_votes = (len(votes))
print(f"total votes: {Total_votes}")

# Create list called 'candidates' that holds a string
candidates_list = ["Correy", "Khan", "Li", "O'Tooley"]

# Print candidate names 
for names in candidates_list:
    print(f'[{str(candidates_list.index(names))}]')

# Total number of votes each candidate won
Correy = int(candiates.count("Correy"))
Khan = int(candiates.count("Khan"))
Li = int(candiates.count("Li"))
O_Tooley = int(candiates.count("O'Tooley"))

# Percentage of votes each candidate won
Correy_percentage = (Correy/total_votes) * 100
Khan_percentage = (Khan/total_votes) * 100
Li_percentage = (Li/total_votes) * 100
O_Tooley_percentage = (O_Tooley/total_votes) * 100

#Print candidate's percentage
print(f"Correy: {Correy_percentage}% ({Correy})")
print(f"Khan: {Khan_percentage}% ({Khan})")
print(f"Li: {Li_percentage}% ({Li})")
print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})")

# Find winner of the election based on popular vote           
if Correy > Khan > Li > O_Tooley:
    winner = "Correy"
elif Khan > Li > O_Tooley > Correy:
    winner = "Khan"
elif Li > O_Tooley > Correy > Khan:
    winner = "Li"
elif O_Tooley > Correy > Khan > Li:
    winner = "O'Tooley"
print(f"winner: {winner}")