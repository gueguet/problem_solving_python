# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001/train/python


import unittest

def valid_ISBN10(isbn):

  if (len(isbn) != 10):
    return False

  res = 0

  for idx,digit in enumerate(isbn):

    if (idx!=9 and digit.isalpha()):
      return False

    if (digit == 'X'):
      digit = 10

    digit = int(digit)
    res += (digit * (idx+1))

  if (res%11 == 0):
    return True
  else:
    return False

# test

class ValidIsbn10Test(unittest.TestCase):
  def test_valid_isbn_10(self):
    self.assertTrue(valid_ISBN10('1112223339'))
    self.assertTrue(valid_ISBN10('048665088X'))
    self.assertTrue(valid_ISBN10('1293000000'))
    self.assertFalse(valid_ISBN10('1234512345'))
    self.assertFalse(valid_ISBN10('1293'))
    self.assertFalse(valid_ISBN10('ABCDEFGHIJ'))
    self.assertFalse(valid_ISBN10('XXXXXXXXXX'))


if __name__ == "__main__":
  unittest.main()



