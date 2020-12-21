# https://www.codewars.com/kata/5e4bb05b698ef0001e3344bc/train/python


"""
Not finished... Timeout error when subit final response --> algo not efficient enough...
"""

import math 
import unittest

def is_square(n):
  sqrt = math.sqrt(n)
  return (sqrt - int(sqrt)) == 0


# from :
# 
def judgeSquareSum(n):  
  
  i = 2
  while (i * i <= n):  
      count = 0
      if (n % i == 0):  
                
          # Count all the prime factors.  
          while (n % i == 0):  
              count += 1 
              n = int(n / i)
        
          # Ifany prime factor of the 
          # form (4k+3)(4k+3) occurs 
          # an odd number of times.  
          if (i % 4 == 3 and count % 2 != 0):  
              return False
      i += 1
        
  # If n itself is a x prime number and  
  # can be expressed in the form of 4k + 3  
  # we return false.  
  return n % 4 != 3


def solve(arr):

  chunk = (len(arr)//4)
  P = 1

  for i in range(chunk):
    P *= ((arr[0+(i*4)]**2 + arr[1+(i*4)]**2) * (arr[2+(i*4)]**2 + arr[3+(i*4)]**2))

  if (judgeSquareSum(P) == True):
    res = []
    for A in range(int(math.sqrt(P/2))):
      B = P - A**2
      if (is_square(B)):
        res.append(A)
        res.append(int(math.sqrt(B)))
        print(res)
        return(res)

  else:
    return [0,0]

  return [0,0]



# test
solve([3, 9, 8, 4, 6, 8, 7, 8, 4, 8, 5, 6, 6, 4, 4, 5])

# bad testing since multiple possibilities --> check testing on codewars 
class OperationSeqTest(unittest.TestCase):

    def tests(self):
        self.assertEqual(solve([2,1,3,4]), [2, 11])


# if __name__ == "__main__":
#   unittest.main()