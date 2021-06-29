'''
A non-empty aray A consisting of N integers is given. The unique number is the number that occurs exactly once in array A.
For example, the following array A:
  A[0] = 4
  A[1] = 10
  A[2] = 5
  A[3] = 4
  A[4] = 2
  A[5] = 10
contains two unique numbers (5 and 2)
You should first find unique number in A. In other words, find the unique number with the lowest position in A.
For above example, 5 is in second position (because A[2]=5) and 2 is in fourth position (because A[4]=2). So the first unique number is 5

Write a function:
  def solution(A):
that, given a non-empty array A of N integers, returns the first unique number in A. The function should return -1 if there are no unique numbers in A. 

'''
def solution(A):
  count = {}
  for i in A:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1
  for i in A:
    if count[i] == 1:
      return i
  return -1

A=[4, 10, 4, 5, 4, 2, 10]
print(solution(A))
