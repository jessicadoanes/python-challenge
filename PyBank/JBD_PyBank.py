# Import csv 
import os 
import csv 

# Path to collect and read data from source
budget_data_csv = os.path.join ("Resources","budget_data.csv")


#Lists
dates = []
increase_profit = ["",0]
decrease_profit = ["",0]

#Variables
count = 0 
average = 0.0
total_months = 1
monthly_change = 0.0
average_profit = 0
total_profit = 0 
previous_profit = 0 
monthly_profit_change = 0
total_month_change = 0


#Open and read
with open (budget_data_csv, 'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    header = next(budget_data)
    first_row = next(budget_data)
    previous_profit = int(first_row[1])
    total_profit = int(first_row[1])
 
# The total number of months in dataset 
    for row in budget_data:
       total_months = total_months + 1
       total_profit = total_profit + int(row[1])
       monthly_profit_change= int(row[1]) - previous_profit
       total_month_change = total_month_change + monthly_profit_change 
       average = total_month_change/ total_months 
       
       if monthly_profit_change > increase_profit[1]: 
            increase_profit[0] = row[0]
            increase_profit[1] = monthly_profit_change
       if monthly_profit_change < decrease_profit[1]: 
            decrease_profit[0] = row[0]
            decrease_profit[1] = monthly_profit_change


# # Print Finanical Analysis  

output=(
f"TOTAL MONTHS: {total_months}\n"
f"TOTAL PROFIT: ${total_profit}\n"
f"AVERAGE CHANGE: ${average}\n"
f"GREATEST INCREASE: {increase_profit[0]} {increase_profit[1]}\n"
f"GREATEST DECREASE: {decrease_profit[0]} {decrease_profit[1]}\n")

print(output)

# Open the file using "write" mode. Specify the variable to hold the contents
output_path = os.path.join("output", "budget_results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(output)
