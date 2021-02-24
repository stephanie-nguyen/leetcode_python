'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

'''
# one liner solution

def runningSum(nums):
	return [sum(nums[:i]) for i, e in enumerate(nums, 1)]
'''

def runningSum(nums):  
    result = []   
    currentSum = 0
    for i in range(len(nums)):
        currentSum += nums[i]
        result.append(currentSum)
    return result

nums = [1,2,3,4,5,6,7]
print(runningSum(nums))