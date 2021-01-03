# https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python

import unittest

def dbl_linear(n):
  list = [1] 
  x = 0
  y = 0
      
  while(len(list)<=n) : 
      a = 2*list[x] + 1 
      b = 3*list[y] + 1 
          
      if a>b : 
          list.append(b)
          y+= 1 
      elif a<b : 
          list.append(a)
          x += 1 
      else : 
          list.append(a)
          x += 1 
          y += 1
              
  return list[n]


# test
class Test(unittest.TestCase):
  def test_twice_linear(self):

    self.assertEqual(dbl_linear(10), 22)
    self.assertEqual(dbl_linear(20), 57)
    self.assertEqual(dbl_linear(30), 91)
    self.assertEqual(dbl_linear(50), 175)



if __name__ == "__main__":
    unittest.main()



# solution best practice --> use deque
"""
from collections import deque

def dbl_linear(n):
    u, q2, q3 = 1, deque([]), deque([])
    for _ in range(n):
        q2.append(2 * u + 1)
        q3.append(3 * u + 1)
        u = min(q2[0], q3[0])
        if u == q2[0]: q2.popleft()
        if u == q3[0]: q3.popleft()
    return u
"""