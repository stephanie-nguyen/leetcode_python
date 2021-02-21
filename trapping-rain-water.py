'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
'''

def maxWater(container, n): 
    res = 0 # To store the maximum water that can be stored
    for i in range(1, n - 1):  # For every element of the array
        left = container[i]  # Find the maximum element on its left 
        for j in range(i): 
            left = max(left, container[j]) 
        right = container[i]  # Find the max element on its right
        for j in range(i + 1 , n):  
            right = max(right, container[j]) 
        res = res + (min(left, right) - container[i])  # Update the max water 
    return res

container = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(container) 
print(maxWater(container, n))
