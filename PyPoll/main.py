import csv
import os

#Creating our variables
total_votes = 0
candidate_votecount = {}
winner = ['', 0]


# Opening our csv file to be able to read
with open('/Users/trevormcdonough/Downloads/Starter_Code-4/PyPoll/Resources/election_data.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    
    #Creating a for loop to run through each line
    for line in csv_reader:
        total_votes = total_votes + 1
        candidate = line[2]
        votes = line [0]
        #Had to look up how to use the in function https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
        if candidate in candidate_votecount:
            candidate_votecount[candidate] += 1
        else:
            candidate_votecount[candidate] = 1

    #Creating a for loop that will calculate the percentages and the winner
    for candidate in candidate_votecount:
        votes = candidate_votecount[candidate]
        percentage = (votes / total_votes) * 100
        candidate_votecount[candidate] = (percentage, votes)
        if votes > winner[1]:
            winner = [candidate, votes]


#Printing our results
print("Election Results")
print("------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------")
for candidate in candidate_votecount:
    percentage, votes = candidate_votecount[candidate]
    print(f"{candidate}: {percentage: .3f}% ({votes})")
print("---------------------------------------------")
print(f"Winner: {winner[0]}")
print("-----------------------------------------------")


#Creating and printing out the results onto a separate file
output = r"/Users/trevormcdonough/Downloads/Starter_Code-4/PyPoll/analysis/text.txt"

with open(output, 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("------------------------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("------------------------------------------\n")
    for candidate in candidate_votecount:
        percentage, votes = candidate_votecount[candidate]
        textfile.write(f"{candidate}: {percentage: .3f}% ({votes})\n")
    textfile.write("---------------------------------------------\n")
    textfile.write(f"Winner: {winner[0]}\n")
    textfile.write("-----------------------------------------------\n")
