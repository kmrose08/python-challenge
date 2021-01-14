# Import os module
import os

# Module for reading data file
import csv
csvpath = os.path.join('.','Resources', 'election_data.csv')

# Set variable output file
text_path = os.path.join('.','Analysis',"Poll analysis.txt")

# Declare variables
votes = 0
total_candidates = 0
candidate = {}
candidate_votes = {}
percentage_candidate_votes = 0
number_candidate_votes = 0
most_votes = 0
candidate = ''
greatest_votes = ["", 0]
winner = ''
votes_cast = 0


# Reading using csv module
with open(csvpath) as csvfile:
  #specify delimiter and variable holding contents
  csvreader = csv.reader(csvfile)
 
  # Skip header
  header = next(csvreader)

# Loop 
  for row in csvreader:
   votes_cast = votes_cast + 1
   candidate = row[2]
  if candidate in candidate_votes: 
     candidate_votes[candidate] = candidate_votes[candidate] +1
  else:
      candidate_votes[candidate] = 1
    

  
print("Election Results")
print('---------------------')
print(f"Total Votes: {votes_cast:,}")
print('---------------------')
print(candidate_votes)
print('---------------------')
print(f"Winner: {winner}")

with open(text_path,"w") as csvfile:
  csvfile.write("Election Results\n")
  csvfile.write('---------------------\n')
  csvfile.write(f"Total Votes: {votes_cast:,}\n")
  csvfile.write('---------------------\n')
  csvfile.write(f"{candidate_votes}\n")
  csvfile.write('---------------------\n')
  csvfile.write(f"Winner: {winner}")
  