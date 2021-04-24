'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''
import pdb
def fourSum(nums,target):
    n = len(nums)
    nums.sort()
    pdb.set_trace()
    res = set()
    for a in range(n-3): #what gives the 4 values for sum
        for b in range(a+1, n-2):
            j = b + 1
            k = n - 1
            while j < k:
                total = nums[a] + nums[b] + nums[k] + nums[j]
                if total == target:
                    res.add(tuple(sorted([nums[a],nums[b],nums[k],nums[j]])))
                    j += 1
                    k -= 1
                elif total > target:
                    k -= 1
                else:
                    j += 1
    return res

nums=[1,1,0,-1,-2,-3]
target=4
print(fourSum(nums,target))