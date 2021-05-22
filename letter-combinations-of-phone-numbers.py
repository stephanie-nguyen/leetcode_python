'''
Suppose we have a string containing digits from 2-9 inclusive. We have to return all possible letter combinations that the number 
could represent. One mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to 
any letters.

For an example, if the given string is “23”, then the possible strings will be [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf”]

To solve this, we will follow these steps −
    1. Define an array called solve to solve the problem recursively
    2. solve method takes digits, characters, result, current_string and current_level, the function will be like
    3. if current_level = length of digits, then add current string after the result, and return
    4. for all characters i in characters[digits[current_level]] 
        perform solve(digits, characters, result, current_string + i, current_level + 1)
    5. The actual function will be like
    6. if digits length is 0, then return an empty list
    7. define one map to hold numbers and corresponding characters as a string
    8. result := an empty list
    9. call solve(digits, characters, result, “”, 0)
'''

class Solution(object):
   def letterCombinations(self, digits):
      if len(digits) == 0:
         return []
      characters = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
      result = []
      self.solve(digits,characters,result)
      return result
   def solve(self, digits, characters, result, current_string="",current_level = 0):
      if current_level == len(digits):
         result.append(current_string)
         return
      for i in characters[int(digits[current_level])]:
         self.solve(digits,characters,result,current_string+i,current_level+1)

ob1 = Solution()
print(ob1.letterCombinations("379"))