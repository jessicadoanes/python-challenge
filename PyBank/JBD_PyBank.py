# Import csv 
import os 
import csv 

# Path to collect and read data from source
budget_data_csv = os.path.join ('Resources','budget_data.csv')

with open (budget_data_csv, 'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    csv_header = next(budget_data)

# Define the function 
def print_percentages(budget_data):
    # Lists to store data
    count = str(budget_data[0])
    profit = int(budget_data [1])
    months = str(budget_data[2])
   
    # Variables 
    count = 0 
    total_months = 0
    average_profit = 0
    total_profit = 0 
    total_change_profit = 0
    increase_profit = 0
    decrease_profit = 0
    initial_profit = 0 

# The total number of months in dataset 
    for row in budget_data:
       total_months = count + 1
print(f"total_months: {total_months}") 


# The net total amount of Profit/Losses over entire period
date.append(row[0]) 
total_profit = total_profit + int(row[1])
    
# Monthly change in profits
for i in range(len(total_profit)-1):

    #Difference between two months to append monthly change 
    monthly_profit_change = (total_profit[i+1]-total_profit[i])


# Calculate the changes in profit/Losses over entire period
total_change_profit = int(row[1])

# Calculate average over entire period
average_profit = sum(Profit/Losses) / len(Date)

# Calculate change in profits 
change_profit = monthly_profit_change - int(row[1])
average_change_profit = (total_change_profit/count)

# Greatest increase and decrease in losses (date and amount) over entire period
increase_profit = max(monthly_profit_change)
decrease_profit = min (monthly_profit_change)

# Print Finanical Analysis 
print(f"COUNT: {count}")
print(f"AVERAGE: ${average}")
print(f"NET TOTAL AMOUNT: ${total_profit}")
print(f"TOTAL CHANGE AMOUNT: ${total_change_profit}")
print(f"GREATEST INCREASE: ${increase_profit}")
print(f"GREATEST DECREASE: ${decrease_profit}")

# Open the file using "write" mode. Specify the variable to hold the contents
output_path = os.path.join("output", "budget_data_new.csv")
with open(output_path, 'w', newline='') as csvfile:

# Initailze csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')