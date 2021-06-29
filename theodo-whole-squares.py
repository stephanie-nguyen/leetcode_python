'''
An integers P is a whole square if it is a square of some integers Q; i.e. if P=Q^2.
Write a function:
  def solution(A,B)
that, given two integers, A and B, returns the number of whole squares within the interval [A,B] (both ends included).
For example, given A=4 and B=17, the function should return 3, because there are 3 squares of integers in the interval [4, 17] namely 4=2^2, 9=3^2 and 16=4^2
Assume that:
  1. A and B are integers within the range [-10000, 10000]
  2. A <= B
'''
def solution(a,b):
  count = 0
  for i in range(a,b+1):
    j=1
    while j*j <= i:
      if j*j == i:
        count += 1
      j += 1
  return count

a=2;
b=24;
print(solution(a,b))
