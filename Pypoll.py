
#load the modules
import csv
import os

#total number of votes
#number of candidates
# Total votes for each candidate
# percentage of votes each candiadate got
# Winner of the election

#Read the election_results.csv from the Resources folder in Asynch
#Read file using direct method with WITH statement or indirectly with the open()
#file_to_load = 'Resources/Election_results.csv'
#using the os method to load a file from indirect path
file_to_load = os.path.join("Resources","Election_results.csv")
#convert to txt file
file_to_save = os.path.join("analysis","Election_analysis.txt")

#initialize the total vote count
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_count = 0
winning_percentage = 0
winning_candidate = 0

with open(file_to_load) as election_data:
#election_data = open(file_to_load,'r')

    #print(election_data)
#election_data.close()


#with open(file_to_save, "w") as txtfile:
#outfile.write("Hello")
#outfile.close()
#txtfile.write

#Read and analyze the data
    file_reader = csv.reader(election_data)
#print header row
    headers=next(file_reader)
    print(headers)

    for row in file_reader:
        total_votes  += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:
     # Print the final vote count to the terminal.
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        votes_percentage = float(votes)/float(total_votes) * 100
         #print(f"{candidate_name}: received {round(votes_percentage,2)}% of the votes. ")
         #print(f"{candidate_name}: {votes_percentage:.1f}%({votes:,})\n")

        if (votes > winning_count) and (votes_percentage > winning_percentage):
            winning_votes = votes
            winning_percentage = round(votes_percentage,2)
            winning_candidate = candidate_name   

    winning_candidate_summary = (
        f"----------------------\n"
        f"winner: {winning_candidate}\n"
        f"winning vote_count : {winning_votes:,}\n"
        f"winning percentage : {winning_percentage:,}\n"
        f"----------------------\n")

    print(winning_candidate_summary)



    #print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)
    txt_file.write(winning_candidate_summary)




