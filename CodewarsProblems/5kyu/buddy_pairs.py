# https://www.codewars.com/kata/59ccf051dcc4050f7800008f/train/python


import unittest


def div_sum(n):
    divs = set() # avoid duplicate
    for x in range(2, int(n**0.5)+1): # don't count 1 
        if n % x == 0:
            divs.add(x)
            divs.add(n // x) # reduce calculation time by adding the other quotien directly
    return sum(divs)


def buddy(start, limit):
    for n in range(start, limit+1):
        buddy = div_sum(n) # 1 was not counted

        if buddy > n and div_sum(buddy) == n:
            return [n, buddy]

    return "Nothing"




# test

class Test(unittest.TestCase):

    def test_buddy(self):

        self.assertEqual(buddy(10, 50), [48, 75])
        self.assertEqual(buddy(2177, 4357), "Nothing")
        self.assertEqual(buddy(57345, 90061), [62744, 75495])
        self.assertEqual(buddy(1071625, 1103735), [1081184, 1331967])






if __name__ == "__main__":
    unittest.main()
    
