import random
import copy
from time import time
from matplotlib import pyplot as plt
from sorting import MergeSort, InsertionSort
 
data_setsize = [50, 100, 500, 1000, 2500, 5000, 7500, 10000]
dataset = []
 
def generate_dataset():
    for i in data_setsize:
        temp = []
        for _ in range(0, i):
            temp.append(random.randint(0, i))
        dataset.append(temp)
 
generate_dataset()
 
insertion_sort_times = [0] * len(data_setsize)
merge_sort_times = [0] * len(data_setsize)
 
def calculate_time():
    for i in range(0,len(data_setsize)):
        # for insertion sort
        temp1 = copy.copy(dataset[i]) # creating deep copy
        start_time = time()
        InsertionSort(temp1)
        end_time = time()
        # print(end_time-start_time)
        insertion_sort_times[i] = end_time - start_time
 
        # for merge sort
        temp2 = copy.copy(dataset[i])
        start_time = time()
        MergeSort(temp2,0,data_setsize[i]-1)
        end_time = time()
        # print(end_time-start_time)
        merge_sort_times[i] = end_time - start_time
 
 
calculate_time()
print(insertion_sort_times)
print(merge_sort_times)
 
plt.plot(data_setsize,insertion_sort_times,color="blue")
plt.plot(data_setsize,merge_sort_times,color="red")
plt.show()