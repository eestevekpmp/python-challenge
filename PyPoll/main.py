# Import os module
import os

# Import csv module for reading csv files
import csv

election_data = os.path.join('Resources', 'election_data.csv')

candidateNamesList = []
stockhamName = str("Charles Casper Stockham")
degetteName = str("Diana DeGette")
doaneName = str("Raymon Anthony Doane")
voteCount = 0
candidateVotes_count = 0
stockhamVotes_count = 0
degetteVotes_count = 0
doaneVotes_count = 0

#analysis = zip(data, profitLoss)
with open(election_data) as csvfile:
    
# csvreader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
# read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    

    for row in csvreader:
        voteCount += 1
        candidateName = row[2]
        
        if stockhamName == candidateName:
            
            stockhamVotes_count += 1

        if degetteName == candidateName:

            degetteVotes_count += 1

        if doaneName == candidateName:

            doaneVotes_count += 1

stockham_percent_votes = round(((stockhamVotes_count / voteCount)*100),3)
degette_percent_votes = round(((degetteVotes_count / voteCount)*100),3)
doane_percent_votes = round(((doaneVotes_count / voteCount)*100),3)  

if stockhamVotes_count > degetteVotes_count and doaneVotes_count:
   winner = stockhamName  
   winner_votes = stockhamVotes_count

if degetteVotes_count > stockhamVotes_count and doaneVotes_count:
   winner = degetteName  
   winner_votes = degetteVotes_count

if doaneVotes_count > degetteVotes_count and stockhamVotes_count:
   winner = degetteName  
   winner_votes = degetteVotes_count

print("Election Results\n\n")
print("---------------------\n\n")
print(f"Total Votes: {voteCount} \n")
print(f"Charles Casper Stockham: {stockham_percent_votes}% ({stockhamVotes_count})\n")
print(f"Diana DeGette: {degette_percent_votes}% ({degetteVotes_count})\n")
print(f"Raymon Anthony Doane: {doane_percent_votes}% ({doaneVotes_count})\n")
print("---------------------\n\n")
print(f"Winner: {winner}\n\n")
print("---------------------\n")

output_path = os.path.join("analysis", "election_data_output.txt")
with open(output_path, 'w') as textfile:

    textfile.write("Election Results\n\n")
    textfile.write("---------------------\n\n")
    textfile.write(f"Total Votes: {voteCount} \n")
    textfile.write(f"Charles Casper Stockham: {stockham_percent_votes}% ({stockhamVotes_count})\n")
    textfile.write(f"Diana DeGette: {degette_percent_votes}% ({degetteVotes_count})\n")
    textfile.write(f"Raymon Anthony Doane: {doane_percent_votes}% ({doaneVotes_count})\n")
    textfile.write("---------------------\n\n")
    textfile.write(f"Winner: {winner}\n\n")
    textfile.write("---------------------\n")
