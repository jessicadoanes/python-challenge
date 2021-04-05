# Import csv 
import os 
import csv 

# Path to collect and read data from source
election_data_csv = os.path.join ('..', 'Documents', 'GT Bootcamp Assignments_Local', '3', "python-challenge", "PyPoll", "Analysis")

with open (election_data_csv, 'r') as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')

    print(election_data_csv)

    csv_header = next (election_data_csv)
    print (f"CSV Header: {csv_header}")

    for row in budget_data_csv:
       print(row)

#Define the function
def print_percentages(budget_data):
    # Lists to store data 
    

# Variables

# The total number of votes cast

# List of candidates who recieved votes

# Percentage of votes each candidate won

# Total number of votes each canidate won

# Winner of the election based on popular vote           