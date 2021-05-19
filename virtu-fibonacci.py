'''
Write a function

    def solution(x)

that given an integer x, returns an integer that corresponds to the minimum number of steps required to change x to a fibonacci number.
In each step you can either increment or decrement the current number, i.e you can change x to either x+1 or x-1.
x will be between 0 and 1,000,000 inclusive.

The fibonacci sequence is defined as follows:
F[0] = 0
F[1] = 1

for each i >= 2: F[i] = F[i-1] + F[i-2]

The elements of the fibonacci sequence are called fibonacci numbers

For example, for x=15, the function should return 2.
For x=1 and x=13 the function should return 0.
'''

def solution(x):
    a=b=1
    while 2+x > a+b:
        a,b=b,a+b
    return x-a

x=1
print(solution(x))
