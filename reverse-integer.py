'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go 
outside the signed 32-bit integer range [-231, 231 - 1], then return 0. 

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

def reverse(x):
    result = 0
    num = abs(x)
    while num:
        num, digit = divmod(num, 10)
        result = result*10 + digit
    if result > 2**31-1:  # MAX 32 bit int, does not apply to python really
        return 0
    return result if x > 0 else -result

x=123456789
print(reverse(x))
