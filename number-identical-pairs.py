'''
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
'''
'''
def numIdenticalPairs(nums):
    dict = {}
    count = 0
    for i in nums:
        if i in dict: #if the value is already in, we can either add to an existing ONE, else we can create another count for it
            if dict[i] == 1:
                count += 1
            else:
                count += dict[i]
            dict[i] += 1
        else:
            dict[i] = 1
    return count

nums = [1,2,3,1,1,4,4,3,1,2]
print(numIdenticalPairs(nums))

'''


def numIdenticalPairs(nums):
    dict = {}
    count = 0
    for i in nums:
        if i in dict: #if the value is already in, we can either add to an existing ONE, else we can create another counter for it
            if dict[i] == 1:
                count += 1
                print(f"count:{count}")
            else:
                count += dict[i]
                print(f"2ndcount:{count}")
                #dict[i] += 1
            dict[i] += 1
            print(f"i={i},dict:{dict[i]}")

        else:
            dict[i] = 1
            print(f"i={i},dict:{dict[i]}")

    return count

nums = [1,3,3,1,1,4,4,3,1,2]
print(numIdenticalPairs(nums))