'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume 
all four edges of the grid are all surrounded by water.

Example1 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

import pdb
def numIslands(grid):
    if not grid:
        return 0
        
    y = len(grid)
    x = len(grid[0])
    sum  = 0
    pdb.set_trace()
    for i in range(y):
        for j in range(x):
            if grid[i][j] == "0":
                continue
            else:
                #sum up only once per chance of meeting "1"
                sum += 1
                stack = list()
                stack.append([i,j])
                #visit each "1" in the adjacent area using a stack
                while len(stack) != 0:
                    [p,q] = stack.pop()
                    if p >= 1 and grid[p-1][q] == "1":
                        stack.append([p-1,q])
                    if p < y -1 and grid[p+1][q] == "1":
                        stack.append([p+1,q])
                    if q >= 1 and grid[p][q-1] == "1":
                        stack.append([p,q-1])
                    if q < x - 1 and grid[p][q + 1] == "1":
                        stack.append([p,q+1])
                    #mark as visited
                    grid[p][q] = "0"
    return sum



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))