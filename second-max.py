'''
Given a list of numbers, the task is to write a Python program to find the second largest number in given list.

'''


# O(n) time
def solution(s):
  first_max = max(s[0],s[1])
  second_max = min(s[0], s[1]) 
  for i in range(len(s)):
    if s[i]>first_max:
      second_max = first_max
      first_max = s[i]
    elif s[i]>second_max and s[i]!=first_max:
      second_max=s[i]
  return second_max
  
s=[1,2,5,9,3,4,3,2,5,6,3]
print(solution(s))



'''
def solution(s):
  new_list = set(s)
  new_list.remove(max(new_list))
  return max(new_list)
  
s=[1,2,5,9,3,8,4,3,2,5,6,3]
print(solution(s))
'''
