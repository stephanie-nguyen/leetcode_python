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
    compressedstring = ""

    count = 1
    for i in range(len(chars)-1): #end of the range cannot equal nothing "abcd" [0123] d cannot be compared to nothing in the next line
        if chars[i] == chars[i+1]: 
            count += 1 
        else:
            compressedstring += chars[i] + str(count) #append to compressed string
            count = 1
            #pdb.set_trace()
    compressedstring += chars[i+1] + str(count) #last value was ignored, this takes it into account

    #in case our compressedstring is longer than the original string
    if len(compressedstring) >= len(chars):
        return chars
    else:
        return compressedstring

chars = "aabbbbccccbbba"
print(compress(chars))