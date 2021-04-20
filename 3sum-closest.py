'''
Given an array nums of n integers and an integer target, find three integers in 
nums such that the sum is closest to target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
import pdb
def threeSumClosest(num, target):
    num.sort()
    result = num[0]+num[1]+num[2]
    for i in range(len(num)-2):
        j=i+1
        k=len(num)-1
        while j<k:
            sum = num[i]+num[j]+num[k]
            if sum ==target:
                return sum
            if abs(sum-target)<abs(result-target):
                result=sum
                    
            if sum<target:
                j+=1
            elif sum>target:
                k-=1
    return result

num = [1,2,-1,2,5,6]
target = 12
print(threeSumClosest(num,target))