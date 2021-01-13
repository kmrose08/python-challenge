# Import os module
import os

# Module for reading data file
import csv
csvpath = os.path.join('.','Resources', 'budget_data.csv')

# Set output file
text_path = "Analysis.txt" 

# Declare variables
months = 0
total = 0
total_ch = 0
prev_rev = 0
inc = ['',0]

# Reading using csv module
with open(csvpath) as csvfile:
  #specify delimiter and variable holding contents
  csvreader = csv.reader(csvfile, delimiter=",")
 
  # Skip header
  header = next(csvreader)

  # Loop through to find total months
  for i,row in enumerate(csvreader):
    rev = int(row[1])
    months += 1
    total += rev

    change = rev - prev_rev
    if i == 0:
      change = 0
    total_ch += change
    prev_rev = rev

    if change > inc[1]:
      inc[0] = row[0]
      inc[1] = change

  # Loop through profits 

  # Calculate profit difference and add to profit change

  # max_increase = max(profit_change)
  # max_decrease = min(profit_change)


  # Find greatest increase in profits
  # greatest_increase_profits = profit_change.index(max(profit_change))

  # print(greatest_increase_profits)
  
  # Find greatest decrease in losses
  # greatest_decrease_losses = profit_change.index(min(profit_change))
  
  # print(greatest_decrease_losses)

 # profit_average = float(profit_change) / float(total_months)
# Set variable for output file
#output_file = os.path.join("Analysis.txt")

#  Open the output file
#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)

#total_profit = int(total_profit)
#greatest_increase_profits = int(greatest_increase_profits)



print("Financial Analysis")
print("-------------")
print(f"Total Months: {months}")
print(f"Total: ${total:,}")
print(f"Average Change: {total_ch/(months-1):,.2f}")
print(f"Greatest Increase in Profits: {inc[0]} (${inc[1]:,})")
#print(f"Greatest Decrease in Profits: Sep-2013 ($-2196167)")


# Output file
#output_file = Path(")

#with open(output_file,"w") as file:
    