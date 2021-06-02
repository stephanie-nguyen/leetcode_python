''''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example:
Input: 1210
Output: False

'''
def isPalindrome(x):
    x = str(x)
    if x[0] == '-':
        return False       
    else:
        x=abs(int(x[::-1]))
                
    if x==x:
        return True
        
    return False
            
x=1210
print(isPalindrome(x))
