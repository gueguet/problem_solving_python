# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

import unittest

def move_zeros(array):
  newarr =[]
  zeroarr=[]
  for item in array:
      if item!= 0 or type(item)== bool :
          newarr.append(item)
      else:
          zeroarr.append(item)
              
  newarr.extend(zeroarr)
  return(newarr)


class TestMovingZeros(unittest.TestCase):

  def test_moving_zeros(self):
    self.assertEqual(move_zeros([1,2,0,1,0,1,0,3,0,1]), [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
    self.assertEqual(move_zeros(['a', 0, 0, 'b', None, 'c', 'd', 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]), ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])

if __name__ == "__main__":
  unittest.main()


# clever solution 
"""
def move_zeros(arr):
  l = [i for i in arr if isinstance(i, bool) or i!=0]
  return l+[0]*(len(arr)-len(l))
"""