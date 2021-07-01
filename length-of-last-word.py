'''
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World"
Output: 5
'''

def lengthOfLastWord(str):
  s = str.split(' ')
  print(s)
  while s[-1] == '' and len(s) > 1:
    s.pop()
  print(s)
  return len(s[-1])

str="hello world"
print(lengthOfLastWord(str))
