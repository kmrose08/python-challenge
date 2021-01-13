# Import os module
import os

# Module for reading data file
import csv
csvpath = os.path.join('.','Resources', 'budget_data.csv')

# Set output file
text_path =os.path.join('Analysis','Analysis.txt') 

# Declare variables
months = 0
total = 0
total_ch = 0
prev_rev = 0
inc = ['',0]

# Reading using csv module
with open(csvpath) as csvfile:
  #specify delimiter and variable holding contents
  csvreader = csv.reader(csvfile)
 
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

print("Financial Analysis")
print("-------------")
print(f"Total Months: {months}")
print(f"Total: ${total:,}")
print(f"Average Change: {total_ch/(months-1):,.2f}")
print(f"Greatest Increase in Profits: {inc[0]} (${inc[1]:,})")


# Output file 

with open(text_path,"w") as csvfile:
    csvfile.write("Financial Analysis\n")
    #file.write("Financial Analysis")
    csvfile.write('---------------------\n')
    csvfile.write(f"Total Months: {months}\n")
    csvfile.write(f"Total: ${total:,}\n")
    csvfile.write(f"Average Change: {total_ch/(months-1):,.2f}\n")
    csvfile.write(f"Greatest Increase in Profits: {inc[0]} (${inc[1]:,})") 