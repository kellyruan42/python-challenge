# Dependencies and Setup
import os
import csv
import statistics

# Open the csv
with open('../Resources/election_data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    
    # Skip the header
    next(reader)
    
    # Create empty lists and empty variables
    rowcount = 0
    votes_charles = 0
    votes_diana = 0
    votes_raymon = 0

    # Create for loop to calculate
    for row in reader:
        rowcount += 1
        if str(row[2]) == "Charles Casper Stockham":
            votes_charles += 1
        elif str(row[2]) == "Diana DeGette":
            votes_diana += 1
        elif str(row[2]) == "Raymon Anthony Doane":
            votes_raymon += 1

    # Put the round values in variables
    percentage_charles = round((votes_charles / rowcount * 100), 3)
    percentage_diana = round((votes_diana / rowcount * 100), 3)
    percentage_raymon = round((votes_raymon / rowcount * 100), 3)

    # Create the two lists    
    votes = [votes_charles, votes_diana, votes_raymon]
    name = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
    df = list(zip(votes, name))

    # Create for loop to find the winner
    for row in df:
        if row[0] == max(votes):
            winner = row[1]

# Print the result
print("Election Results")
print("-----------------------------------------")
print("Total Votes: " + str(rowcount))
print("-----------------------------------------")
print("Charles Casper Stockham: " + str(percentage_charles) + "% (" + str(votes_charles) + ")")
print("Diana DeGette: " + str(percentage_diana) + "% (" + str(votes_diana) + ")")
print("Raymon Anthony Doane: " + str(percentage_raymon) + "% (" + str(votes_raymon) + ")")
print("-----------------------------------------")
print("Winner: " + winner)
print("-----------------------------------------")

# Export the output in txt
f = open('./analysis/Analysis and Output.txt', 'w')
f.write("\nElection Results\n")
f.write("\n---------------------------------------------------\n")
f.write(f'\nTotal Votes: {str(rowcount)}\n')
f.write("\n---------------------------------------------------\n")
f.write(f'\nCharles Casper Stockham: {str(percentage_charles)}% ({str(votes_charles)})\n')
f.write(f'\nDiana DeGette: {str(percentage_diana)}% ({str(votes_diana)})\n')
f.write(f'\nRaymon Anthony Doane: {str(percentage_raymon)}% ({str(votes_raymon)})\n')
f.write("\n---------------------------------------------------\n")
f.write(f'\nWinner: {winner}\n')
f.write("\n---------------------------------------------------\n")
f.close()