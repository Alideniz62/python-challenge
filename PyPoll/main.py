
# ______________PyPoll challenge_________________

# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.



#import the os module and csv module
import os
import csv
from decimal import Decimal
pypoll_csv = os.path.join("Resources", "election_data.csv")

with open(pypoll_csv) as csvfile:
    importedCSV = csv.reader(csvfile, delimiter=',')
    
    voter_list = []
    county_list = []
    candidates = []
    

    for row in importedCSV:
        voter_id = row[0]
        county = row[1]
        cand = row[2]

#append the data
        voter_list.append(voter_id)
        county_list.append(county)
        candidates.append(cand)

#removing headers from list data.
voterID = voter_list[1:len(voter_list)]
county = county_list[1:len(county_list)]
candidate = candidates[1:len(candidates)]

#calulating total votes
t_Votes = len(candidate)

print("Election Results")
print("------------------------------")
print("Total Votes: {num}".format(num=t_Votes))


#start working on the lists
candidate_List=list(set(candidate))


#keep tally for four candidates
#each value for each candidate
Votes0=candidate.count(candidate_List[0])
Votes1=candidate.count(candidate_List[1])
Votes2=candidate.count(candidate_List[2])
Votes3=candidate.count(candidate_List[3])

#creating vote percentages
Per0 = Decimal(Votes0/t_Votes*100)
Per1 = Decimal(Votes1/t_Votes*100)
Per2 = Decimal(Votes2/t_Votes*100)
Per3 = Decimal(Votes3/t_Votes*100)
PerDes0 = round(Per0,3)
PerDes1 = round(Per1,3)
PerDes2 = round(Per2,3)
PerDes3 = round(Per3,3)

print("------------------------------")
print("{one}: {two}% ({three})".format(one=candidate_List[0], two=PerDes0, three=Votes0))
print("{one}: {two}% ({three})".format(one=candidate_List[1], two=PerDes1, three=Votes1))
print("{one}: {two}% ({three})".format(one=candidate_List[2], two=PerDes2, three=Votes2))
print("{one}: {two}% ({three})".format(one=candidate_List[3], two=PerDes3, three=Votes3))

#determe winner
wlist = []
wlist.append(Votes0)
wlist.append(Votes1)
wlist.append(Votes2)
wlist.append(Votes3)
BW= wlist.index(int(max(wlist)))
winner_cand= candidate_List[BW]

print("------------------------------")
print("Winner: {str}".format(str=winner_cand))
print("------------------------------")

text_file = open("pyboll.txt", "w")
text_file.write("Election Results")
text_file.write("\n")
text_file.write("------------------------------")
text_file.write("\n")
text_file.write("Total Votes: {num}".format(num=t_Votes))
text_file.write("\n")
text_file.write("\n")
text_file.write("------------------------------")
text_file.write("\n")
text_file.write("{one}: {two}% ({three})".format(one=candidate_List[0], two=PerDes0, three=Votes0))
text_file.write("\n")
text_file.write("{one}: {two}% ({three})".format(one=candidate_List[1], two=PerDes1, three=Votes1))
text_file.write("\n")
text_file.write("{one}: {two}% ({three})".format(one=candidate_List[2], two=PerDes2, three=Votes2))
text_file.write("\n")
text_file.write("{one}: {two}% ({three})".format(one=candidate_List[3], two=PerDes3, three=Votes3))
text_file.write("\n")
text_file.write("------------------------------")
text_file.write("\n")
text_file.write("Winner: {str}".format(str=winner_cand))
text_file.write("\n")
text_file.write("------------------------------")
text_file.close()
