# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python


import unittest



def sum_pairs(nums, sum_value):
  seen = set()
  for num in nums:
      diff = sum_value - num
      if diff in seen:
          return [diff, num]
      seen.add(num)


# test

l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]

class Test(unittest.TestCase):

    def test_som_of_pairs(self):
        self.assertEqual(sum_pairs(l1, 8), [1, 7])
        self.assertEqual(sum_pairs(l2, -6), [0, -6])
        self.assertEqual(sum_pairs(l3, -7), None)
        self.assertEqual(sum_pairs(l5, 10), [3, 7])


if __name__ == "__main__":
    unittest.main()
    pass