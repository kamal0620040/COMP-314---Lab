import random
import matplotlib.pyplot as plt
import time
from search import binarySearch,linearSearch

dataset_size = [50, 100, 500, 1000, 10000,100000,1000000,1000000,10000000]
dataset = []

for size in dataset_size:
    # random.sample(list, no_of_element) => it will return list that contain random 
    # number of element from the given list
    dataset.append(sorted(random.sample(range(1, size*10), size)))

# print(data)
# print(random.sample(range(1,10),5))
    
linear_search_time = []
binary_search_time = []

for data in dataset:
    # print(data)
    start = time.time_ns()
    linearSearch(data, random.randint(1,len(data)))
    end = time.time_ns()
    linear_search_time.append(end - start)

    start = time.time_ns()
    # binarySearch(sorted(data), 0, len(data) - 1,random.randint(0,len(data)-1))
    binarySearch(data, 0, len(data) - 1, random.randint(1,len(data)))
    end = time.time_ns()
    binary_search_time.append(end - start)

print(linear_search_time)
print(binary_search_time)

plt.plot(dataset_size, linear_search_time, label='Linear search')
plt.plot(dataset_size, binary_search_time, label='Binary search')
plt.xlabel('Amount of data')
plt.ylabel('Time taken (seconds)')
plt.title('Search algorithm performance')
plt.legend()
plt.show()