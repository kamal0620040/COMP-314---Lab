import random
import matplotlib.pyplot as plt
import time
from search import binarySearch,linearSearch

dataset_size = [50, 100, 500, 1000, 10000, 100000, 1000000,10000000]
dataset = []

for size in dataset_size:
    # random.sample(list, no_of_element) => it will return list that contain random 
    # number of element from the given list
    dataset.append(sorted(random.sample(range(1, size*10), size)))
     
linear_search_time = []
binary_search_time = []

for data in dataset:
    start = time.time_ns()
    # searching for element present in dataset - Average Case
    # linearSearch(data, data[random.randint(1,len(data)-1)])

    # searching for element not present in dataset - Worst Case
    # linearSearch(data, -1)

    # searching the first element in dataset  - Best Case
    linearSearch(data, data[0])

    end = time.time_ns()
    linear_search_time.append(end - start)

    start = time.time_ns()
    # searching for element present in dataset - Average Case
    # binarySearch(data, 0, len(data) - 1, data[random.randint(1,len(data))])
    
    # searching for element not present in dataset - Worst Case
    # binarySearch(data, 0, len(data) - 1, -1)

    # searching the first element in dataset  - Best Case
    binarySearch(data, 0, len(data) - 1, data[(0 + len(data) - 1) // 2])
    end = time.time_ns()
    binary_search_time.append(end - start)

print(linear_search_time)
print(binary_search_time)

plt.plot(dataset_size, linear_search_time, label='Linear search')
plt.plot(dataset_size, binary_search_time, label='Binary search')
plt.xlabel('Amount of data')
plt.ylabel('Time taken (ns)')
plt.title('Search algorithm performance')
plt.legend()
plt.show()