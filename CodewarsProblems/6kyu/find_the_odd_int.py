# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

import unittest
from pprint import pprint


# total overkill...
# just go through the seq and use :
# seq.count(i) to get the number of time the num is contained inside the seq

def find_it(seq):
  counter = {}
  
  for num in seq:
    if num not in counter:
      counter[num] = 0
    else:
      counter[num] += 1
  

  for item in counter:
    if (counter[item] % 2 == 0):
      return item


# test

class TestFindTheOddInt(unittest.TestCase):
  
  def test_find_odd_int(self):
    self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
    self.assertEqual(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)


if __name__ == "__main__":
    unittest.main()
