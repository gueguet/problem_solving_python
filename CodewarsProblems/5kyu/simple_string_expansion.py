# https://www.codewars.com/kata/5a793fdbfd8c06d07f0000d5/train/python


from termcolor import cprint


import unittest

def solve(st):

  st = st.replace(')','')
  split_string = st.split('(')

  res = ""

  # could also use split_string[::-1] to reverse it!
  for char in reversed(split_string):

    if (char.isalpha()):
      res = char + res

    elif (char.isdigit()):
      res = int(char) * res

    else:
      # supose always letter|number

      res = int(char[-1]) * res
      res = char[0] + res

  return res



class TestSimpleString(unittest.TestCase):
  def test_simple_st_expansion(self):
    solve("3(ab)"),"ababab"
    solve("2(a3(b))"),"abbbabbb"
    solve("3(b(2(c)))"),"bccbccbcc"




if __name__ == "__main__":
    solve("3(ab)")
    # solve("2(a3(b))")


# Test.it("Basic tests")
# Test.assert_equals(solve("3(ab)"),"ababab")
# Test.assert_equals(solve("2(a3(b))"),"abbbabbb")
# Test.assert_equals(solve("3(b(2(c)))"),"bccbccbcc")
# Test.assert_equals(solve("k(a3(b(a2(c))))"),"kabaccbaccbacc")