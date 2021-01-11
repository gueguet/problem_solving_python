# https://www.codewars.com/kata/5a6225e5d8e145b540000127/train/python

import unittest
from collections import Counter


def common(a, b, c):
    return sum((Counter(a) & Counter(b) & Counter(c)).elements())


class TestCommonArrayElements(unittest.TestCase):
    def test_common_array_elements(self):
        self.assertEqual(common([1, 2, 3], [5, 3, 2], [7, 3, 2]), 5)
        self.assertEqual(common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]), 7)


if __name__ == "__main__":
    unittest.main()
