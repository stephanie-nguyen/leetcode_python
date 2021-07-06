'''
Given a grid with different colors in a different cell, each color represented by a different number. The task is to find 
out the largest connected component on the grid. Largest component grid refers to a maximum set of cells such that you can 
move from any cell to any other cell in this set by only moving between side-adjacent cells from the set. 
'''


n = 6
m = 8
  
# stores information about  which cell
# are already visited in a particular BFS
visited = [[0 for j in range(m)]for i in range(n)]
  
# result stores the final result grid
result = [[0 for j in range(m)]for i in range(n)]
  
# stores the count of cells in the largest
# connected component
COUNT = 0
  
# Function checks if a cell is valid i.e it
# is inside the grid and equal to the key
def is_valid(x, y, key, input):
 
    if (x < n and y < m and x >= 0 and y >= 0):
        if (visited[x][y] == 0 and input[x][y] == key):
            return True;
        else:
            return False;
     
    else:
        return False;
  
# BFS to find all cells in
# connection with key = input[i][j]
def BFS(x, y, i, j, input):
     
    global COUNT
     
    # terminating case for BFS
    if (x != y):
        return;
  
    visited[i][j] = 1;
    COUNT += 1
  
    # x_move and y_move arrays
    # are the possible movements
    # in x or y direction
    x_move = [ 0, 0, 1, -1 ]
    y_move = [ 1, -1, 0, 0 ]
  
    # checks all four points connected with input[i][j]
    for u in range(4):
     
        if (is_valid(i + y_move[u], j + x_move[u], x, input)):
            BFS(x, y, i + y_move[u], j + x_move[u], input);
  
# called every time before a BFS
# so that visited array is reset to zero
def reset_visited():
 
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0
  
# If a larger connected component
# is found this function is called
# to store information about that component.
def reset_result(key, input):
 
    for i in range(n):
        for j in range(m):
            if (visited[i][j] != 0 and input[i][j] == key):
                result[i][j] = visited[i][j];
            else:
                result[i][j] = 0;
         
# function to print the result
def print_result(res):
 
    print("The largest connected "+
          "component of the grid is :" + str(res));
  
    # prints the largest component
    for i in range(n):
        for j in range(m):
            if (result[i][j] != 0):
                print(result[i][j], end = ' ')
                 
            else:
                print('. ',end = '')
         
        print()
          
# function to calculate the largest connected
# component
def computeLargestConnectedGrid(input):
 
    global COUNT
    current_max = -10000000000
  
    for i in range(n):
        for j in range(m):
            reset_visited();
            COUNT = 0;
  
            # checking cell to the right
            if (j + 1 < m):
                BFS(input[i][j], input[i][j + 1], i, j, input);
  
            # updating result
            if (COUNT >= current_max):
                current_max = COUNT;
                reset_result(input[i][j], input);
             
            reset_visited();
            COUNT = 0;
  
            # checking cell downwards
            if (i + 1 < n):
                BFS(input[i][j], input[i + 1][j], i, j, input);
  
            # updating result
            if (COUNT >= current_max):
                current_max = COUNT;
                reset_result(input[i][j], input);
             
    print_result(current_max);
 
# Drivers Code
if __name__=='__main__':
     
    input = [ [ 1, 4, 4, 4, 4, 3, 3, 1 ],
                        [ 2, 1, 1, 4, 3, 3, 1, 1 ],
                        [ 3, 2, 1, 1, 2, 3, 2, 1 ],
                        [ 3, 3, 2, 1, 2, 2, 2, 2 ],
                        [ 3, 1, 3, 1, 1, 4, 4, 4 ],
                        [ 1, 1, 3, 1, 1, 4, 4, 4 ] ];
  
    # function to compute the largest
    # connected component in the grid
    computeLargestConnectedGrid(input);