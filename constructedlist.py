'''
Scenario 1:
A non-empty array A consisting of N integers if given.
Array A represents a linked list. A list is constructed from this array as follows:
    1. the first node (the head) is located at index 0;
    2. the value of a node is located at index K is A[K];
    3. if the value of a node is -1 then it is the last node of the list
    4. otherwise the sucessor of a node is located at index K is valid index, that is 0 ≤ A[K] < N

For example, for array A such that: 
    A[0] = 1
    A[1] = 4
    A[2] = -1
    A[3] = 3
    A[4] = 2

    The following list is constructed:
        1. the first node (the head) is located at index 0 and has a value of 1
        2. the second node is located at index 1 and has a value of 4
        3. the third node is located at index 4 and has a value of 2
        4. the fourth node is located at index 2 and has a value of -1


Write a function:

    def solution(A)

that, give a non-empty array A consisting of N integers, returns the length of the list constructed from A in the above manner.
For example, given array A such that:
    A[0] = 1
    A[1] = 4
    A[2] = -1
    A[3] = 3
    A[4] = 2
the function should return 4, as explained in the example above. 

Assume that:
    1. N is an integer within the range [1...200000]
    2. each element of array A is an integer within the range [-1 ... N-1]
    3. it will always be possible to construct the list and its length will be finite
'''
def solution(A):
    length=0
    if not A:
        return length
    x = 0
    while A[x] != -1:
        x = A[x]
        length += 1
    length += 1
    return length

A = [1,4,-1,3,2]
print(solution(A))