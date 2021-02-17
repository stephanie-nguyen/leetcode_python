'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the 
British mathematician John Horton Conway in 1970." The board is made up of an m x n grid of cells, where each cell has 
an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors 
(horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
        1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
        2. Any live cell with two or three live neighbors lives on to the next generation.
        3. Any live cell with more than three live neighbors dies, as if by over-population.
        4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births 
and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
'''

def gameOfLife(board):
        #Do not return anything, modify board in-place instead.
    nei=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    dies=[]
    lives=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            livenei=0
            for k in nei:
                itemp=i+k[0]
                jtemp=j+k[1]
                if 0<=itemp<= len(board)-1 and 0<=jtemp<= len(board[0])-1:
                    if board[itemp][jtemp]==1:
                        livenei +=1
            if board[i][j]==1:
                if livenei<2 or livenei > 3:
                    dies.append([i,j])
            else:
                if livenei==3:
                    lives.append([i,j])
    for die in dies:
        board[die[0]][die[1]]=0
    for live in lives:
        board[live[0]][live[1]]=1
    return board
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(gameOfLife(board))
