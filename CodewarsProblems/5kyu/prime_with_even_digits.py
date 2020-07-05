# https://www.codewars.com/kata/582dcda401f9ccb4f0000025/train/python

import unittest

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if (n % i == 0):
            return False
    return True


def num_even_digits(x):
    return len([y for y in str(x) if int(y) % 2 == 0])


def f(n):
    res = 0
    max_even_found = 0
    for i in range(n-1, 0, -1): # need to exclude n itself !

        if is_prime(i):
            
            # limit calculation
            # this break condition is very important for performance issue !
            if (len(str(i)) <= max_even_found + 1):
                break

            if num_even_digits(i) > max_even_found:
                res = i
                max_even_found = num_even_digits(i)

    return res



# test

class Test(unittest.TestCase):

    def test_prime_with_even(self):
        self.assertEqual(f(1000), 887)
        self.assertEqual(f(1210), 1201)
        self.assertEqual(f(10000), 8887)
        self.assertEqual(f(500), 487)
        self.assertEqual(f(487), 467)



if __name__ == "__main__":
    unittest.main()
    



# best practice 
def is_prime(n):
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def f(n):
    max_prime, max_even_cnt = 0, 0

    for x in range(n-1, 0, -1):
        if len(str(x)) <= max_even_cnt + 1: 
            break

        if is_prime(x):
            even_cnt = sum(d in "02468" for d in str(x))
            if even_cnt > max_even_cnt:
                max_prime = x
                max_even_cnt = even_cnt

    return max_prime
