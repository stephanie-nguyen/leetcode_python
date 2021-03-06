"""
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character 
is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many 
numerical digits as possible, and interprets them as a numerical value. The string can contain additional characters 
after those that form the integral number, which are ignored and have no effect on the behavior of this function. If 
the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists 
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""
class Solution:
    def myAtoi(self, s):
        maxval = 2147483647                         # maximum limit, 2^31
        minval = -2147483648                        # minimum limit, -2^31
        s = s.strip()                               # remove leading and trailing whitespaces
        if not s:
            return 0
        sign, idx = 1, 0                                  # sign set to 1 -> Positive, index set to 0
        if s[idx]=='+':                                   # check if the first character is a '+'
            idx+=1                                        # if so, move index to next character
        elif s[idx]=='-':                                 # check if first character is '-'
            sign = -1                                     # change status of sign to be a negative number
            idx+=1                                        # update the index
        num = 0
        n = len(s)
        while idx<n:
            if not s[idx].isdigit():                      # if the number is not a digit, then stop
                break
            num = num*10 + ord(s[idx])-ord('0')           # else move the units, tenths, hundredth... places by multiplying the number by 10 and add the unicode integer
            if num>maxval:
                break
            idx+=1
        return min(max(sign*num, minval), maxval)         # return answer if its within the maximum and minimum range
