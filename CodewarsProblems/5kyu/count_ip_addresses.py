# https://www.codewars.com/kata/526989a41034285187000de4/train/python

import unittest

def ips_between(start, end):

  print(start)
  print(end)

  start_list = start.split(".")
  end_list = end.split(".")

  res = 0

  for i in range(0,len(end_list)):
    diff = int(end_list[i]) - int(start_list[i])
    # print("i : ", i)
    # print("diff : ", diff)
    res = res + (diff * (256 ** (3-i)))

  return res


# test 
class TestCountIpAddresses(unittest.TestCase):
  def test_count_ip_add(self):
    self.assertEqual(ips_between("10.0.0.0", "10.0.0.50"), 50)
    self.assertEqual(ips_between("20.0.0.10", "20.0.1.0"), 246)


if __name__ == "__main__":
  unittest.main()