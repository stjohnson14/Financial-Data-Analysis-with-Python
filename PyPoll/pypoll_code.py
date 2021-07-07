import os
import csv

candidates = {}

election_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')
election_csv_output = os.path.join('PyPoll', 'Analysis', 'Election_results.txt')
with open(election_csv, 'r') as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    header= next(csvreader)

    for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]]+= 1
        else:
            candidates[row[2]] = 1
        
        total = candidates.values()
        total_votes = sum(total)

        list_candidates = candidates.keys()

        votes_per = [f'{(x/total_votes)*100:.2f}%' for x in candidates.values()]

        winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        
print("Election Results")

print("--------------------------")

print(f"Total votes: {int(total_votes)}")

print("--------------------------")

candidate = []
vote = []

i = 0 
for candidate, vote in candidates.items():
    print(f"{candidate}, {vote}, {votes_per[i]}")
    i+=1

print(f"The winner is: {winner}")

with open(election_csv_output, "w") as output_file:
    
    output_file.write("\n Election Results \n")
    output_file.write("---------------------\n")
    output_file.write(f"Total votes: {int(total_votes)}\n")  
    output_file.write("---------------------\n")
    i = 0 
    for candidate, vote in candidates.items():
        output_file.write(f"{candidate}, {vote}, {votes_per[i]}\n")
        i+=1    
    output_file.write("---------------------\n")
    output_file.write(f"The winner is: {winner}\n")
    