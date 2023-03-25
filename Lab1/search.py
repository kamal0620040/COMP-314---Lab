from math import floor

def linearSearch(data, target):
    for i in range(len(data)):
        if(data[i] == target):
            return i
    
    return -1



def binarySearch(data, start, end, target):
    mid = floor((start + end) / 2)

    if(start <= end):
        if(data[mid] == target):
            return mid
        elif(data[mid] > target):
            return binarySearch(data, start, mid - 1, target)
        elif(data[mid] < target):
            return binarySearch(data, mid + 1, end, target)
    else:
        return -1