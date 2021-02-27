def getInvCount(arr): 
    n = len(arr) 
    invcount = 0  #Initialize result     
    for i in range(0,n-1): 
        for j in range(i+1 , n): 
                if arr[i] > arr[j]: 
                    for k in range(j+1 , n): 
                        if arr[j] > arr[k]: 
                            invcount += 1
    return invcount 
  
# Driver program to test above function 
arr = [8 , 4, 2 , 1] 
print(getInvCount(arr))
