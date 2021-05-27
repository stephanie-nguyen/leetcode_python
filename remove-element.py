'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.
'''
def removeElement(nums,val):
  i=0
  for n in nums:
    if n!= val:
      nums[i] = n
      i+=1
  return i

nums = [1,2,3,2,1]
val = 3
print(removeElement(nums,val))
