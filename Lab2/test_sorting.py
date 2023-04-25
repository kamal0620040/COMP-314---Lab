import unittest
from sorting import MergeSort, InsertionSort

class SearchTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        # when the input is reverse sorted
        input1 = [5,4,3,2,1]
        output1 = [1,2,3,4,5]
        InsertionSort(input1)
        self.assertListEqual(input1, output1)
        
        # when the input is already sorted
        input2 = [1,2,3,4,5]
        output2 = [1,2,3,4,5]
        InsertionSort(input2)
        self.assertListEqual(input2, output2)

    def test_merge_sort(self):
        # when the input is reverse sorted
        input1 = [5,4,3,2,1]
        output1 = [1,2,3,4,5]
        MergeSort(input1,0,len(input1)-1)
        self.assertListEqual(input1, output1)

        # when the input is already sorted
        input2 = [1,2,3,4,5]
        output2 = [1,2,3,4,5]
        MergeSort(input2, 0, len(input2) - 1)
        self.assertListEqual(input2, output2)

if __name__ == "__main__":
    unittest.main()