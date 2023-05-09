import unittest
from knapsack_brute_force import zero_one_knapsack_brute_force, fractional_knapsack_brute_force
from knapsack_greedy import fractional_knapsack_greedy
from dynamic_programming_knapsack import dynamic_knapsack

class KnapsackTestCase(unittest.TestCase):

    def test_0_1_knapsack_brute_force(self):
        # where n=0 and cap=0, expected output=0
        assert zero_one_knapsack_brute_force([], [], 0, 0) == 0

        # where one item can be picked, expected output=value[0]
        assert zero_one_knapsack_brute_force([2], [4], 2, 1) == 4

        # where some items can be picked
        assert zero_one_knapsack_brute_force([2, 3, 4], [4, 5, 1], 5, 3) == 9
    
    def test_fractional_knapsack_brute_force(self):
        # where n=0 and cap=0, expected output=0
        assert fractional_knapsack_brute_force([], [], 0) == 0

        # where one item can be picked, expected output=value[0]
        assert fractional_knapsack_brute_force([2], [4], 2) == 4

        # where some items can be picked
        assert fractional_knapsack_brute_force([2,5,1,3,4], [15,14,10,45,30], 7) == 77.5

    def test_fractional_knapsack_greedy(self):
        # where n=0 and cap=0, expected output=0
        assert fractional_knapsack_greedy([], [], 0) == 0

        # where one item can be picked, expected output=value[0]
        assert fractional_knapsack_greedy([2], [4], 2) == 4

        # where some items can be picked
        assert fractional_knapsack_greedy([2,5,1,3,4], [15,14,10,45,30], 7) == 77.5

    def test_dynamic_knapsack(self):
        # Test case to test dynamic_knapsack function
        weight = [2,5,1,3,4]
        value = [15,14,10,45,30]
        cap = 7
        state = [[-1 for j in range(cap+1)] for i in range(len(value) + 1)]
        expected_output = 75
        assert dynamic_knapsack(weight, value, state, cap, len(value)) == expected_output


if __name__ == "__main__":
    unittest.main()