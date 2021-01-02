# https://www.codewars.com/kata/559a28007caad2ac4e000083/train/python

import unittest


# timeout problem if use that for each single number
# in permieter function --> need to keep track of the last fibonacci number
# also better to calculate the res once a the very end and not in the loop
"""
def fibonacci(n):
  if (n==0):
    return 0
  if (n==1):
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
"""

def perimeter(n):
  print(n)
  fib_list = [0,1,1]
  for i in range (3,n+2):
    fn = sum(fib_list[-2:])
    fib_list.append(fn)
  return 4*sum(fib_list)


class Test(unittest.TestCase):

  def test_permieter(self):
    self.assertEqual(perimeter(5),80)
    self.assertEqual(perimeter(7),216)
    self.assertEqual(perimeter(100),6002082144827584333104)


if __name__ == "__main__":
    unittest.main()