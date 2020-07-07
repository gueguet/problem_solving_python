# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python


from collections import Counter
import unittest


def dirReduc(arr):
    dict = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    res = []
    for i in arr:
        if res and dict[i] == res[-1]: # if res --> means there is at least one element inside --> can acces [-1]
            res.pop()
        else:
            res.append(i)
    return res






# test

class Test(unittest.TestCase):

    def test_dirReduc(self):

        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        self.assertEqual(dirReduc(a), ['WEST'])
        u = ["NORTH", "WEST", "SOUTH", "EAST"]
        self.assertEqual(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])




if __name__ == "__main__":
    unittest.main()
