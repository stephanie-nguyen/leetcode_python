'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

def merge(intervals):
    #intervals.sort(key =lambda x: x[0])
    merged =[]
    for i in intervals:
        if not merged or merged[-1][-1] < i[0]:
            merged.append(i)
        else:
            merged[-1][-1] = max(merged[-1][-1], i[-1])
    return merged

intervals=[[1,3],[2,6]]
print(merge(intervals))

