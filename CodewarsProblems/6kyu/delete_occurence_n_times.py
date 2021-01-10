# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

import unittest

def delete_nth(order, max_e):

    res = []
    occ_dict = {}
    for num in order:
        if num not in occ_dict:
            occ_dict[num] = 1
        else:
            occ_dict[num] += 1

        if (occ_dict[num] <= max_e):
            res.append(num)

    return res
    

class TestDeleteOccurence(unittest.TestCase):

    def test_occ(self):
        self.assertEqual(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
        self.assertEqual(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()