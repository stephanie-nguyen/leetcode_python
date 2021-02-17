import sys  
def eggDrop(n, k): #fx for min #trials needed in worst case with negg and kfloor
 
    if (k == 1 or k == 0): #0floors,0trials. 1floor,1trial
        return k 
    if (n == 1): #needs ktrials for 1egg and kfloors
        return k 
  
    min = sys.maxsize #if egg breaks on 4floor, thats the max meaning it will not break from any lower floors
    for x in range(1, k + 1): #considering all drops from 1st to kth floor. returns the      min of that +1
        res = max(eggDrop(n - 1, x - 1), eggDrop(n, k - x)) 
        if (res < min): 
            min = res 
    return min + 1
  
n = 2
k = 10
print("Minimum number of trials in worst case with", n, "eggs and", k, "floors is", eggDrop(n, k)) 
