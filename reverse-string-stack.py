'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
'''

def createStack(): 
    stack=[] 
    return stack 
    
def size(stack):            # determine size of stack
    return len(stack) 

def isEmpty(stack):         # if size 0, stack is empty
    if size(stack) == 0: 
        return true 
      
def push(stack,item):       # this adds item to stack, increasing size by 1
    stack.append(item) 
   
def pop(stack):             # this removes item from stack, decreasing size by 1
    if isEmpty(stack): return
    return stack.pop() 
   
def reverse(string):        # stack based func to reverse a string
    n = len(string) 
    stack = createStack()   #  create an empty stack
    for i in range(0,n,1):  #push all characters of the string to stack
        push(stack,string[i]) 
    string=""               # makes string empty bc all characters saved in stack

    for i in range(0,n,1):  # pop all characters of string and put them back to string
        string+=pop(stack) 
           
    return string 
  
s = "stephanie"
print (reverse(s))
