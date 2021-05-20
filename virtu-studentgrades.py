'''
Write a function:
    def solution(S)
that, given a zero-indexed array A consisting of N integers representing the initial test scores of a row of students, returns 
an array of integers representing their final test scores (in the same order).
There uis a group of students sat next to eachother in a row. Each day, students study together and take a test at the end of 
the day. Test scores for a given student can only change once per day as follows:
    - If a student sits immediately between two students with bettter scores, that student's score will improve bby 1 when they 
    take the test.
    - If a student sits between two students with worse scores, that student's test score will decrease by 1.

This process will repeat each day as long as at least one student keeps changing their score. Note that the first and last 
student in the row never change their schores as they never sit between two students.

Return an array representing the final test scores for each student once their scores fully stop changing

Example 1:
Input: [1, 6, 3, 4, 3, 5]
Returns: [1, 4, 4, 4, 4, 5]

On the first day, the second students score will decrease, the third students schore will increase, the fourth students score 
will decrease by 1 and the fifth students score will increase by 1, i.e. [1,5,4,3,4,5]. On the second day, the second student's 
score will decrease again and the fourth student's score will increase, i.e. [1,4,4,4,4,5]. There will be no more changes in 
scores after that.

Example 2: 
Input: [100, 50, 40, 30]
Returns: [100, 50, 40, 30]
No students changed score

You can assume that:
    - The number of students is in the range from 1 to 1,000
    - Student's scores are in the range from 0 to 1,000
'''

def solution(S):
    B = A.copy()
    changes = True
    while changes: 
        for x in range(1, len(A)-1):
            if B[x-1] > B[x] and B[x+1] > B[x]:
                A[x] += 1
            if B[x-1] < B[x] and B[x+1] < B[x]:
                A[x] -= 1
            if A==B:
                changes = False
            else:
                B=A.copy()
    return(A)

S = [100, 50, 40, 30]
print(solution(S))
