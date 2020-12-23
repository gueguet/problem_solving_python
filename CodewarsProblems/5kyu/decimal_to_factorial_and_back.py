# https://www.codewars.com/kata/54e320dcebe1e583250008fd/train/python

import unittest
import math
import string


key_list = [x for x in range (0,37)]

value_list = [str(x) for x in range (0,10)]
for letter in string.ascii_uppercase:
  value_list.append(letter)

hex_dict = dict(zip(key_list, value_list))
hex_dict_reverse = dict(zip(value_list, key_list))


def dec2FactString(nb):
  res = ""
  divider = 1
  while nb != 0:
    reste = nb % divider
    nb = nb // divider
    res += hex_dict[reste]
    divider += 1
  return res[::-1]

def factString2Dec(string):
  res = 0
  counter = 0
  for l in string[::-1]:
    if (str(l) == "0"):
      res += (int(l) * 1)
    else:
      res += hex_dict_reverse[str(l)] * math.factorial(counter)
    counter += 1
  return res


# test 
class DecToFacAndBackTest(unittest.TestCase):
  def test_basic(self):
    self.assertEqual(dec2FactString(463), "341010")
    self.assertEqual(dec2FactString(371993326789901217467999448150835199999999), "ZYXWVUTSRQPONMLKJIHGFEDCBA9876543210")
    self.assertEqual(factString2Dec("341010"), 463)
    self.assertEqual(factString2Dec("ZYXWVUTSRQPONMLKJIHGFEDCBA9876543210"), 371993326789901217467999448150835199999999)


if __name__ == "__main__":
  unittest.main()
