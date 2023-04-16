import math
import sys

def InsertionSort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        while i > -1 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key


def MergeSort(arr, s, e):
    if s < e:
        m = math.floor((s + e)/2)
        MergeSort(arr, s, m)
        MergeSort(arr, m+1, e)
        Merge(arr, s, m, e)

def Merge(arr, s, m, e):
    # size of first sub array
    n1 = m - s + 1
    # size of second sub array
    n2 = e - m
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    for i in range(n1):
        L[i] = arr[s + i]
    
    for j in range(n2):
        R[j] = arr[m + j + 1]
    
    L[n1] = sys.maxsize
    R[n2] = sys.maxsize

    i = 0
    j = 0
    for k in range(s, e + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i + 1
        else:
            arr[k] = R[j]
            j = j + 1
