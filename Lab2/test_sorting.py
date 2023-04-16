import unittest
from sorting import MergeSort, InsertionSort

class SearchTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        input = [5,4,3,2,1]
        output = [1,2,3,4,5]
        InsertionSort(input)
        self.assertListEqual(input, output)

    def test_merge_sort(self):
        input = [5,4,3,2,1]
        output = [1,2,3,4,5]
        MergeSort(input,0,len(input)-1)
        self.assertListEqual(input, output)

if __name__ == "__main__":
    unittest.main()