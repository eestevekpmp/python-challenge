# Import os module
import os

# Import csv module for reading csv files
import csv
# Sets path for .csv data set file
election_data = os.path.join('Resources', 'election_data.csv')

candidateNamesList = []  # empty list to hold candidate names dictionary
stockhamName = str("Charles Casper Stockham") # variables for string candidate names
degetteName = str("Diana DeGette")
doaneName = str("Raymon Anthony Doane")
voteCount = 0           # set accumulators to zero
candidateVotes_count = 0
stockhamVotes_count = 0
degetteVotes_count = 0
doaneVotes_count = 0

with open(election_data) as csvfile:
    
# csvreader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
# skip the header row
    csv_header = next(csvreader)
    
# iterate through rows of election_data.csv
    for row in csvreader:
        voteCount += 1         # start counting rows to tally votes
        candidateName = row[2] # grab candidate name from third column

    # conditionals invoked to match string names and count votes   
        if stockhamName == candidateName:
            
            stockhamVotes_count += 1

        if degetteName == candidateName:

            degetteVotes_count += 1

        if doaneName == candidateName:

            doaneVotes_count += 1

# set variables to hold percent vote calculations
stockham_percent_votes = round(((stockhamVotes_count / voteCount)*100),3)
degette_percent_votes = round(((degetteVotes_count / voteCount)*100),3)
doane_percent_votes = round(((doaneVotes_count / voteCount)*100),3)  

# conditionals with logical 'and' used to identify winner by popular vote
if stockhamVotes_count > degetteVotes_count and doaneVotes_count:
   winner = stockhamName  
   winner_votes = stockhamVotes_count

if degetteVotes_count > stockhamVotes_count and doaneVotes_count:
   winner = degetteName  
   winner_votes = degetteVotes_count

if doaneVotes_count > degetteVotes_count and stockhamVotes_count:
   winner = degetteName  
   winner_votes = degetteVotes_count

# formatted output results to terminal 
print("Election Results\n\n")
print("---------------------\n\n")
print(f"Total Votes: {voteCount} \n")
print(f"Charles Casper Stockham: {stockham_percent_votes}% ({stockhamVotes_count})\n")
print(f"Diana DeGette: {degette_percent_votes}% ({degetteVotes_count})\n")
print(f"Raymon Anthony Doane: {doane_percent_votes}% ({doaneVotes_count})\n")
print("---------------------\n\n")
print(f"Winner: {winner}\n\n")
print("---------------------\n")

# set path for output text file location
output_path = os.path.join("analysis", "election_data_output.txt")
with open(output_path, 'w') as textfile:

# formatted output results to text file
    textfile.write("Election Results\n\n")
    textfile.write("---------------------\n\n")
    textfile.write(f"Total Votes: {voteCount} \n")
    textfile.write(f"Charles Casper Stockham: {stockham_percent_votes}% ({stockhamVotes_count})\n")
    textfile.write(f"Diana DeGette: {degette_percent_votes}% ({degetteVotes_count})\n")
    textfile.write(f"Raymon Anthony Doane: {doane_percent_votes}% ({doaneVotes_count})\n")
    textfile.write("---------------------\n\n")
    textfile.write(f"Winner: {winner}\n\n")
    textfile.write("---------------------\n")
