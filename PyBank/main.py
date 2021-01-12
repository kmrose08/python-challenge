# Import os module
import os

# Module for reading data file
import csv
csvpath = os.path.join('.','Resources', 'budget_data.csv')

# Set output file
text_path = "Analysis.txt" 

# Declare variables
total_months = []
total_profit = []
profit_change = []

# Reading using csv module
with open(csvpath) as csvfile:
  #specify delimiter and variable holding contents
  csvreader = csv.reader(csvfile, delimiter=",")
 
  # Skip header
  header = next(csvreader)

  # Loop through to find total months
  for row in csvreader:
    total_months.append(row[0])
    total_profit.append(row[1])

  # Loop through profits 
  for i in range(len(total_profit)-1):

  # Calculate profit difference and add to profit change
    profit_change.append(int((total_profit[i+1]))-(int(total_profit[i])))


  # Find greatest increase in profits
  greatest_increase_profits = profit_change.index(max(profit_change))

  print(greatest_increase_profits)
  
  # Find greatest decrease in losses
  greatest_decrease_losses = profit_change.index(min(profit_change))
  
  print(greatest_decrease_losses)

 # profit_average = float(profit_change) / float(total_months)
# Set variable for output file
#output_file = os.path.join("Analysis.txt")

#  Open the output file
#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)

print("Financial Analysis")
print("-------------")
#print('Total Months: ' + total_months)
#print('Total: ' + profit_change)
# print('Average Change' + profit_average)
#print('Greatest Increase in Profits: ' + greatest_increase_profits)
#print('Greatest Decrease in Profits: ' + greatest_decrease_losses)