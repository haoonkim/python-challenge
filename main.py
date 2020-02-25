#import csv dependencies
import os
import csv

#read csv and make the path for file
data_output = os.path.join('/Users/haoonkim/Desktop/election_data.csv')

#variables to count votes
total_vote = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0

#read data
with open(data_output, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #read the header first row
    csv_header = next(csvreader)
    
    #calculate total vote
    #candidates' votes, so we can know who wins
    for row in csvreader:
        total_vote += 1
        if row[2] == "Khan":
            khan_vote += 1
        elif row[2] == "Correy":
            correy_vote += 1
        elif row[2] == "Li":
            li_vote += 1
        else:
            otooley_vote += 1
    
    #candidate's vote percentage
    khan_per = khan_vote / total_vote
    correy_per = correy_vote / total_vote
    li_per = li_vote / total_vote
    otooley_per = otooley_vote / total_vote
    
    #calculate winner
    if khan_vote > correy_vote and khan_vote > li_vote and khan_vote > otooley_vote:
        win = "Khan"
    elif correy_vote > khan_vote and correy_vote > li_vote and correy_vote > otooley_vote:
        win = "Correy"
    elif li_vote > khan_vote and li_vote > correy_vote and li_vote > otooley_vote:
        win = "Li"
    else:
        win = "O'tooley"



    #print analysis
    printout = (f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_vote}\n"
        f"-------------------------\n"
        f"Khan: {khan_per:.3%} ({khan_vote})\n"
        f"Correy: {correy_per:.3%} ({correy_vote})\n"
        f"Li: {li_per:.3%} ({li_vote})\n"
        f"O'Tooley: {otooley_per:.3%} ({otooley_vote})\n"
        f"-------------------------\n"
        f"Winner: {win}\n"
        f"-------------------------")
print(printout)
