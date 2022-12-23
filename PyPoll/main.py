import csv

with open('/Users/kelly/Desktop/python-challenge/PyPoll/Resources/election_data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    csv_reader = next(reader)
    
    rowcount = 0
    votes_charles = 0
    votes_diana = 0
    votes_raymon = 0
    for row in reader:
        rowcount += 1
        if str(row[2]) == "Charles Casper Stockham":
            votes_charles += 1
        elif str(row[2]) == "Diana DeGette":
            votes_diana += 1
        elif str(row[2]) == "Raymon Anthony Doane":
            votes_raymon += 1

    percentage_charles = round((votes_charles / rowcount * 100), 3)
    percentage_diana = round((votes_diana / rowcount * 100), 3)
    percentage_raymon = round((votes_raymon / rowcount * 100), 3)
        
    votes = [votes_charles, votes_diana, votes_raymon]
    name = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
    df = list(zip(votes, name))
    for row in df:
        if row[0] == max(votes):
            winner = row[1]

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