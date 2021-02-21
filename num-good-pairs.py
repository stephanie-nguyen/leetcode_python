'''
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
'''

def numIdenticalPairs(nums):
    dict = {}
    count = 0
    for i in nums:
        if i in dict: 
            if dict[i] == 1:
                count += 1
                print(f"i= {i},initial count: {count}") #if the value is already in, we can either add to an existing ONE // 
            else:
                count += dict[i]
                print(f"i= {i},new count for additional value: {count}") #create another counter because we found additional pair
                #dict[i] += 1
            dict[i] += 1
            print(f"    updated i= {i}, {dict[i]} of 2 stored in dict, pair count: {count}")

        else:
            dict[i] = 1
            print(f"initial {i} added, {dict[i]} of 2 stored in dict, pair count: {count}") 

    return count

nums = [1,2,3,1,1,4,4,3,1,2]
print(numIdenticalPairs(nums))