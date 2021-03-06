'''
Given a string s, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s):
  '''
  first, create a dictionary to store all the letters
  max_len will be our counter
  start will be our initial letter
  '''
  dict={} 
  max_len=0
  start = 0
        
  for i in range(len(s)):
      if s[i] in dict:
        start=max(start,dict[s[i]]+1)
      dict[s[i]]=i
      max_len=max(max_len,i-start+1)
  return max_len

s="teststring"
print(lengthOfLongestSubstring(s))
