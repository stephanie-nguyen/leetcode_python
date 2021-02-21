'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique 
triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
'''

import pdb

def threeSum(nums):
    res = []
    nums.sort()
    if len(nums) < 3:
        return res

    for i in range(len(nums)-2): # why -2?
        #pdb.set_trace()
        if i > 0 and nums[i] == nums[i-1]: continue
        l, r = i + 1, len(nums) - 1
        while l < r :
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i] ,nums[l] ,nums[r]])
                l += 1; r -= 1
                while l < r and nums[l] == nums[l - 1]: l += 1
                while l < r and nums[r] == nums[r + 1]: r -= 1
            elif s < 0 :
                l += 1
            else:
                r -= 1
    return res  

nums=[0,1,2,3,-1,2,-1,4,1]
print(threeSum(nums))
