'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

You may assume all the characters consist of printable ascii characters. 
RECURSIVE SOLUTION
'''
'''
def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return s[::-1] 
s="stephanie"
print(reverse(s))
'''
def reverse(s):
    reverse = []
    index = len(s)
    while index > 0:
        reverse += s[index-1]
        index = index -1
    return reverse

s = 'stephanie'
print(''.join(reverse(s)))
