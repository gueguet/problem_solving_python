# https://www.codewars.com/kata/5a48fab7bdb9b5b3690009b6/train/python

import unittest
import numpy as np

def reorder(a,b):
    res = []
    res.append([i for i in range (0, a//2)])
    res.append([i for i in range (a//2, a)])

    res[0] = list(np.roll(res[0], b))
    res[1] = list(np.roll(res[1], b))

    return res



# test 

class Test(unittest.TestCase):

    def test_reorder(self):

        self.assertEqual(reorder(10, 1),  [[4, 0, 1, 2, 3], [9, 5, 6, 7, 8]])
        self.assertEqual(reorder(10, 3),  [[2, 3, 4, 0, 1], [7, 8, 9, 5, 6]])
        self.assertEqual(reorder(10, 97), [[3, 4, 0, 1, 2], [8, 9, 5, 6, 7]])


if __name__ == "__main__":
    unittest.main()


# we could have use reshape and arrange
# test_array = np.roll(np.arange(10).reshape(2, -1), 1).tolist()

