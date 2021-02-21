'''
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the 
input character array chars. Note that group lengths that are 10 or longer will be split 
into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
'''

import pdb
def compress(chars):
    left = i = 0
    while i < len(chars):
        char = chars[i]
        length = 1
        #char, length = chars[i], 1
        #pdb.set_trace()
        while (i + 1) < len(chars) and char == chars[i + 1]:
            length = length +1
            i = i + 1
            #length, i = length + 1, i + 1
        chars[left] = char
        if length > 1:
            len_str = str(length)
            chars[left + 1 : left + 1 + len(len_str)] = len_str
            left += len(len_str)
        left = left + 1
        i = i + 1
        #left, i = left + 1, i + 1
    return left

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))