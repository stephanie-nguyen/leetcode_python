'''
Write a finction:
    def solution(s)
that, given a string s, returns an integer that represents the number of ways in which we can select non-empty substring 
of S where all of the characters of the substring are identical. Two substrings with the same letters but different 
locations are still considered different.

For example, the string "zzzyz" contains 2 sub substrings. Four instances of "z", two of "zz", one of "zzz", and one of "y".
String "K" only contains one such substring: "k".

The length of s will be between 1 and 100, inclusive.

Each character in s will be a lowercase letter (a-z).
'''
import pdb
def solution(s):
    substrings = 0
    for a,b in enumerate(s):
        substrings += 1
        #pdb.set_trace()
        for repeating in s[a+1:]:
            if repeating == b:
                substrings += 1
            else:
                break
    return substrings

s = "zzzyz"
print(solution(s))