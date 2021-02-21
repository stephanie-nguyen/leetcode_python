'''
Given the array candies and the integer extraCandies, where candies[i] represents the number of 
candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or 
she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
'''

import pdb

def kidsWithCandies(candies, extracandies):
    maxCandies = max(candies)
    result = []
    #pdb.set_trace()
    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxCandies:
            result.append(True)
        else:
            result.append(False)
    return result

candies = [3,6,2,2,1]
extraCandies = 3
print(kidsWithCandies(candies,extraCandies))

