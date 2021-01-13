# Import os module
import os

# Module for reading data file
import csv
csvpath = os.path.join('.','Resources', 'election_data.csv')

# Set variable output file
text_path = os.path.join("Poll analysis.txt")

# Declare variables
total_votes = []
candidate_votes = []


# Reading using csv module
with open(csvpath) as csvfile:
  #specify delimiter and variable holding contents
  csvreader = csv.reader(csvfile, delimiter=",")
 
  # Skip header
  header = next(csvreader)





#  Open the output file
#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)