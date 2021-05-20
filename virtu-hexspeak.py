'''
Write a function:
    def solution(S)
that, given a string S encoding a decimal integer N, returns a string representing the Hexspeak representiion H of N if H is a 
valid Hexspeak word, otherwise it should return "ERROR".

A decimal number can be converted into hexspeak by first converting it to a hexadecimal, then converting the number 0 to the 
letter "O" and the number 1 to the letter "I". A string is considered a valid hexspeak word if it consists of only the ABCDEFIO 
letters.

The input string S will represent a decimal integer between 1 and 1,000,000,000,000 inclusive.

Example:
If the input string S is "257", the decimal number it encodes is 257 which is written as 101 in hexadecimal. Since 1 and 0 
represent "I" and "O", respectively, we should return "IOI"

If the input string is "3", it is written as 3 in hexadecimal, which does not represent a hexspeak letter, so we return "ERROR"
All answers should be in uppercase letters.
'''

def solution(S):
    def convert(n):
        numbers = []
        while n>0:
            numbers.append(n%16)
            n //= 16
        return numbers[::-1]
    converted = convert(int(S))
    res = ""
    checklist = {0:"O",
                1:"I",
                10:"A",
                11:"B",
                12:"C",
                13:"D",
                14:"E",
                15:"F"}
    for x in converted:
        if x in checklist:
            res += checklist[x]
        else:
            return "ERROR"
    return res

S = "257"
print(solution(S))
