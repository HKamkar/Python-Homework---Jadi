#Written by Hossein Kamkar
from typing import OrderedDict


voteNunmber = int(input())
votes = list()

#Creating a list with all the votes
for i in range(0,voteNunmber):
    votes.append(input())

votes.sort()
#print(votes)    
#creating a dict variable for counting vote
counter = OrderedDict()
for vote in votes:
    counter[vote] = counter.get(vote, 0) + 1


#Display output
for keys in counter:
    print(keys, counter[keys])