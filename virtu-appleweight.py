'''
There is a box with a capacity of 5000 grams. The box may already contain some items, reducing its capacity. You'll be adding apples to that box until it is full. 

Write a function:
    def solution(A)
that, given a zero-indexed array A consisting of N integers, representing the weight of items alreay in the box and each apple's weight, returns the maximum 
number of apples that could fit in the box, without exceeding its capacity.

The input array consists of an integer K as the first element, representing the sum of the weights of items already contained in the box followed by zero or more 
integers representing individual apple weights.

You can assume that A contains between 1 and 100 elements and that every number in it is >= 0 and <= 5000.
Note that an apple can weigh 0 grams, and that you should maximize the number of apples in the box, not their total weight.

For example, for an input of:
[4650, 150, 150, 150]

You should return 2, as the box already contains K=4650 grams of items, so only 2 more apples of weight 150 wiykd fit (bringing the total weight to 4950, still 
below the capacity).

For an input of: 
[4850, 100, 30, 30, 100, 50, 100]
You should return 3, as you could put in two 30-gram apples and the 50-gram apple.
'''

def solution(x):
    remaining = 5000-A[0]
    apples=A[1:]
    apples.sort()
    count=0
    for i in apples:
        remaining -= i
        count += 1
        if remaining <0:
            return count -1
    return count

x=[4850, 100, 30, 30, 100, 50, 100]
print(solution(x))
