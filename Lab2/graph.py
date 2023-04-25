import random
import copy
import time
from matplotlib import pyplot as plt
from sorting import MergeSort, InsertionSort
 
dataset_size = [1000, 2500, 5000, 7500, 10000]
dataset = []
 
for size in dataset_size:
    # random.sample(list, no_of_element) => it will return list that contain random 
    # number of element from the given list
    dataset.append(random.sample(range(1, size*10), size))

 
insertion_sort_times = [0] * len(dataset_size)
merge_sort_times = [0] * len(dataset_size)
 
def calculate_time():
    for i in range(0,len(dataset_size)):
        
        # for insertion sort
        temp1 = copy.copy(dataset[i]) # creating deep copy
        
        # sorting the already sorted list - best case
        # temp1 = sorted(temp1)
        # start_time = time.time_ns()
        # InsertionSort(temp1)
        # end_time = time.time_ns()

        # sorting the reversly sorted list - Worst case
        temp1 = sorted(temp1, reverse=True)
        start_time = time.time_ns()
        InsertionSort(temp1)
        end_time = time.time_ns()

        insertion_sort_times[i] = end_time - start_time
 
        # for merge sort
        temp2 = copy.copy(dataset[i])
        
        # sorting the already sorted list - best case
        # temp2 = sorted(temp2)
        # start_time = time.time_ns()
        # MergeSort(temp2,0,dataset_size[i]-1)
        # end_time = time.time_ns()

        # sorting the reversly sorted list - worst case
        temp2 = sorted(temp2, reverse=True)
        start_time = time.time_ns()
        MergeSort(temp2,0,dataset_size[i]-1)
        end_time = time.time_ns()
        
        # print(end_time-start_time)
        merge_sort_times[i] = end_time - start_time
 
 
calculate_time()
print(insertion_sort_times)
print(merge_sort_times)
 
plt.plot(dataset_size,insertion_sort_times,color="blue",label="Insertion Sort")
plt.plot(dataset_size,merge_sort_times,color="red", label="Merge Sort")
plt.xlabel('Amount of data')
plt.ylabel('Time taken (ns)')
plt.title('Search algorithm performance')
plt.legend()
plt.show()