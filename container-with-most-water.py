'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the 
line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''

def maxArea(height):
    water = []
    right = 0
    left = len(height) - 1
    while (right < left):
        water.append(min(height[right], height[left]) * (left - right))
        if (height[right] < height[left]):
            right += 1
        else:
            left -= 1
    return max(water)
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
