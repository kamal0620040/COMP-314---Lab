def fractional_knapsack_greedy(weights, values, capacity):
    items = [(value, weight) for value, weight in zip(values, weights)]
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    used_weight = 0

    for value, weight in items:
        if used_weight + weight <= capacity:
            total_value += value
            used_weight += weight
        else:
            remaining_capacity = capacity - used_weight
            fraction = remaining_capacity / (weight)
            total_value += fraction * value
            used_weight += fraction * weight
            break

    return total_value

# values = [15,14,10,45,30]
# weights = [2,5,1,3,4]
# bag_capacity = 7
# print(fractional_knapsack_greedy(weights, values, bag_capacity))