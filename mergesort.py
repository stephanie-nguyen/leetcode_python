'''
Given an array of integers nums, sort the array in ascending order.
'''

def mergesort(n):
    if len(n) > 1:
        middle = len(n)/2
        Lside = n[:middle]
        Rside = n[middle:]
        mergeSort(Lside)
        mergeSort(Rside)
        i=j=k=0
        while i<len(Lside) and j<len(Rside):
            if Lside[i]<Rside[j]:
                n[k] = Lside[i]
                i += 1
            else:
                n[k] = Rside[j]
                j += 1
            k += 1

        while i<len(Lside):
            n[k]=Lside[i]
            i += 1
            k += 1

        while j<len(Rside):
            n[k] = Rside[j]
            j += 1
            k += 1
            
