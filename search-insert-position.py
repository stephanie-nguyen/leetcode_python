'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Example: 
  Input: nums = [1,3,5,6], target = 5
  Output: 2
'''
def searchInsert(nums, target):
  for i in range(len(nums)):
    if nums[i] == target:
      return i
    elif nums[i] > target:
      return i
  return i+1
        
nums=[1,3,5,6]
target=5
print(searchInsert(nums, target))
