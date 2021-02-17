'''
Given two strings text1 and text2, return the length of their longest common subsequence. A subsequence of a 
string is a new string generated from the original string with some characters(can be none) deleted without 
changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" 
is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.
'''

def longestCommonSubsequence(text1, text2):
    l1 = len(text1)
    l2 = len(text2)
    dp = [ [0 for _ in range(l2+1) ] for _ in range(l1+1) ]
        
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
    return dp[l1][l2]

text1="abcde"
text2="ace"
print(longestCommonSubsequence(text1,text2))
