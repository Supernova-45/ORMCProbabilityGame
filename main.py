# Author: Alexandra Kim, 4-3-2021

# The game is a probability exercse:
# Source: ORMC, edited for clarity
# You are on a game show where you receive 10,000 if you win and nothing if you lose. 
# The game is played on a simple board: a track with sequential spaces numbered from 0 to 1,000.
# The zero space is marked ”start,” and you piece is placed on it. 
# You are handed a fair six-sided die and three coins. You are allowed to place the tokens on three di↵erent non-zero spaces. 
# Once placed, the tokens may not be moved. After placing the three coins, you roll the die and mvoe your token forward the appropriate number of spaces. 
# If, after moving the token, it lands on a space with a coin on it, you win. 
# If not, roll again and continue moving forward. 
# If you token passes all three coins without landing on one, you lose. 
# On which three spaces should you place the coins to maximize your chances of winning?

# This program simulates the game and plots the results.
# --

# using the random and plotting modules
import random
import matplotlib.pyplot as plt
import numpy as np

n = 50 # spaces are labeled 0 through n inclusive
e = 5 # number of times to simulate the entire game (looping through each token number several times)

probabilities = [0]*n # a list of how many times each token was hit after n rounds
rollSum = 0 # which space the coin is on 
distributions = [] # a list of e nested probability lists
xpointsList = [c for c in range(1,n+1)] # for graphing; token numbers 1 to n inclusive
averageHits = [0]*n # a list that stores the average of the probability lists for each index

for a in range(e): # iterates e times 
    for x in range(1,n+1): # x is the token number
        for j in range(100): # the game is run, trying to hit the xth token, 100 times
            while True: # as long as rollSum is less than the token number, continue 
                roll = random.randrange(1,7)
                rollSum += roll
                if rollSum == x: 
                    probabilities[x-1] += 1
                    rollSum = 0
                    break
                if rollSum > x:
                    rollSum = 0
                    break
    distributions.append(probabilities)
    probabilities = [0]*n

def averageLists(list):
    '''
    input: list, output: list
    takes in a list with nested lists all of the same length
    outputs a single list where each index is the average of the values of the nested lists at that index
    '''
    averageList = []
    totalSum = 0 
    for m in range(len(list[0])): # for each value in the nested lists
        for n in range(len(list)):
            totalSum += list[n][m]
        averageList.append(round(totalSum / len(list),1))
        totalSum = 0
    return averageList

averageList = averageLists(distributions) # list of the average hits per token

# prints the distributions
print("The list of distributions is:")
for elem in distributions:
    print(elem)

# prints averageList, one element per line
for p in range(len(averageList)):
    print("Average hits on token " + str(p+1) + ": " + str(averageList[p]))

# plotting the dataset in distributions
for b in range(e):
    xpoints = xpointsList
    ypoints = distributions[b]
    plt.scatter(xpoints, ypoints, marker='.')

# plotting the average probability
xpoints = xpointsList
ypoints = averageList
plt.plot(xpoints, ypoints, marker='o')

plt.xlabel("Token Number")
plt.ylabel("Times/100 that the token is hit")

plt.show()
plt.close('all')