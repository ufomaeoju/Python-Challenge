import os
import csv

Pypoll = os.path.join('..', 'Pypoll', 'election_data.csv')

# variables
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0

# open csv file
with open(Pypoll, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:

        # calculate total votes
        total_votes += 1

        # calculate number of votes for each of the candidates
        if (row[2] == "Khan"):
            Khan_votes += 1
        elif (row[2] == "Correy"):
            Correy_votes += 1
        elif (row[2] == "Li"):
            Li_votes += 1
        else:
            Otooley_votes += 1

        # calculate the percentage of times each candidate has won
        khan_percent = Khan_votes / total_votes
        correy_percent = Correy_votes / total_votes
        li_percent = Li_votes / total_votes
        otooley_percent = Otooley_votes / total_votes

    # calculate the winner based off of popular votes
    winner = max(Khan_votes, Correy_votes, Li_votes, Otooley_votes)

    if winner == Khan_votes:
        winner_name = "Khan"
    elif winner == Correy_votes:
        winner_name = "Correy"
    elif winner == Li_votes:
        winner_name = "Li"
    else:
        winner_name = "Otooley"

# Print result
print(f"Election Results")
print(f"_________________")
print(f"Total Votes: {total_votes}")
print(f"_________________")
print(f"Kahn: {khan_percent:.3%}({Khan_votes})")
print(f"Correy: {correy_percent:.3%}({Correy_votes})")
print(f"Li: {li_percent:.3%}({Li_votes})")
print(f"Otooley: {otooley_percent:.3%}({Otooley_votes})")
print(f"___________________")
print(f"Winner: {winner_name}")
print(f"____________________")

# Specify File To Write To
election_results = os.path.join('..', 'Pypoll', 'election_results.txt')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(election_results, 'w') as txtfile:
    # Write New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {khan_percent:.3%}({Khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({Correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({Li_votes})\n")
    txtfile.write(f"Otooley: {otooley_percent:.3%}({Otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")