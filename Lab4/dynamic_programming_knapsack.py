# memoized solution
def dynamic_knapsack(weight, value, state, cap, n):
    if(n == 0 or cap == 0):
        return 0
 
    if(state[n][cap] != -1):
        return state[n][cap]
 
    if(weight[n-1] <= cap):
        state[n][cap] = max(value[n-1] + dynamic_knapsack(weight, value,state, cap - weight[n-1], n-1), dynamic_knapsack(weight, value,state, cap, n - 1))
        return state[n][cap]
    elif(weight[n - 1]  > cap):
        state[n][cap] = dynamic_knapsack(weight, value,state, cap, n - 1)
        return state[n][cap]
    
# value = [15,14,10,45,30]
# weight = [2,5,1,3,4]
# cap = 7
# state = [[-1 for j in range(cap+1)] for i in range(len(value) + 1)]
# print(dynamic_knapsack(weight, value,state, 7, len(value)))