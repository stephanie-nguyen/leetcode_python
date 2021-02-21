'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''


def shuffle(nums,n):
    res = []
    for i in range(n): #range 0,1,2,3
        res.append(nums[i]) #starts at 2, which is nums[0]=2
        res.append(nums[i+n]) #moves to nums[0+4]= nums[4]=4
    return res
        
nums = [2,5,1,3,4,7,4,5]
n=4
print(shuffle(nums,n))

