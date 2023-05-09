def zero_one_knapsack_brute_force(weight, value, cap, n):
    if(n == 0 or cap == 0):
        return 0
 
    if(weight[n-1] <= cap):
        return max(value[n-1] + zero_one_knapsack_brute_force(weight, value, cap - weight[n-1], n-1), zero_one_knapsack_brute_force(weight, value, cap, n - 1))
    elif(weight[n - 1]  > cap):
        return zero_one_knapsack_brute_force(weight, value, cap, n - 1)


def fractional_knapsack_brute_force(weights, values, capacity):
    n = len(values)
    ratios = [values[i] / weights[i] for i in range(n)]
    total_value = 0
    while capacity > 0:
        max_ratio_index = -1
        max_ratio = -1
        for i in range(n):
            if weights[i] > 0 and ratios[i] > max_ratio:
                max_ratio_index = i
                max_ratio = ratios[i]
        if max_ratio_index == -1:
            break
        weight_added = min(weights[max_ratio_index], capacity)
        total_value += weight_added * max_ratio
        weights[max_ratio_index] -= weight_added
        capacity -= weight_added
    return total_value

# values = [15,14,10,45,30]
# weights = [2,5,1,3,4]
# bag_capacity = 7
# print(zero_one_knapsack_brute_force(weights, values, bag_capacity, len(values)))
# print(fractional_knapsack_brute_force(weights, values, bag_capacity))