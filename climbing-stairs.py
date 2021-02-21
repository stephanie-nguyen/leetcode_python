'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
'''
import pdb
def climbStairs(n):
    steps = [1,1]
    for i in range(2,n+1):
        steps.append(steps[i-1] + steps[i-2])
    return steps[n]

'''
#recursive solution
def climbStairs(n):
    if n==0 or n==1:
        return 1
    else:
        return climbStairs(n-1) + climbStairs(n-2)

n=20
print(climbStairs(n))
