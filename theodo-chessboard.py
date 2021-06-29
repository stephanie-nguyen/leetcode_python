'''
A chessboard of size N*M (N is rows, M is columns) is given. Each field of the chessboard can be indexed using a pair of integers (P, Q) where O<=P<=N and o<=Q<=M
On each field of the chessboard lies a number of grains of rice. A pawn is located initially at field (0,0). It can perform two kinds of moves:
  1. move from field (P,Q) to field (P+1,Q), or
  2. move from field (P,Q) to field (P,Q+1)
After N+M-2 moves the pawn will arrive at field (N-1, M-1). During its movement across the chessboard it collects all the grains of rice from the fields it lands on.
Write a function:
  def solution(A)
that, given a matrix of size N*M describing the number of grains of rice lying on each field of a N*M-sizedd chessboard, returns the maximal number of rice grains 
a pawn can colect while moving from the field (0,0) to the field (N-1, M-1) in the manner specified above.

For example, given matrix A such that:
A[0][0]==2    A[0][1]=2   A[0][2]==4    A[0][3]=2
A[1][0]==1    A[1][1]=3   A[1][2]==0    A[1][3]=1
A[2][0]==0    A[2][1]=2   A[2][2]==4    A[2][3]=1
A[3][0]==4    A[3][1]=1   A[3][2]==4    A[3][3]=2
the function should return 15. The fields in bold indicate one of the paths that the pawn can take. Following this path, the pawn will collect A[0][0] + A[0][1] 
+ A[2][1] + A[2][2] + A[3][2] + A[3][3] = 2 + 2 + 3 + 2 + 2 + 2 + 2 = 15 rice grains. No path allows the pawn to collect more than 15 grains of rice
'''

def solution(A):
  N=len(A)
  M=len(A[0])
  total=[[0 for i in range(M+1)] for i in range(N+1)]
  for x in range(1,N+1):
    for y in range(1,M+1):
      total[x][y] = max(total[x-1][y], total[x][y-1]) + A[x-1][y-1]
  print(total)
  return total[N][M]

A = [[2,2,4,2], [0,3,0,1], [1,2,2,1], [4,1,2,2]]
print(solution(A))
