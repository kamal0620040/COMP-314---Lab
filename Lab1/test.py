import imp
import unittest
from search import linearSearch, binarySearch

class SearchTestCase(unittest.TestCase):

    def test_linear_search(self):
        data = [1, 2, 4, 6 ,5, 3]
        self.assertEqual(linearSearch(data, 4),2)
        self.assertEqual(linearSearch(data, 2),1)
        # checking for the element(10) which is not present in the list
        self.assertEqual(linearSearch(data, 10),-1)

    def test_binary_search(self):
        data = [1, 2, 3, 4 ,5, 6]
        self.assertEqual(binarySearch(data, 0, len(data) - 1, 4),3)
        self.assertEqual(binarySearch(data, 0, len(data) - 1, 3),2)
        # checking for the element(10) which is not present in the list
        self.assertEqual(binarySearch(data,0,len(data)-1, 10), -1)

if __name__ == '__main__':
    unittest.main()