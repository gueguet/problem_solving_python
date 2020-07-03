# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python


import math
import unittest


def primeFactors(n):

    n = abs(n)

    res = []

    while n % 2 == 0:
        res.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(abs(n)))+1, 2):
        while n % i == 0:
            res.append(i)
            n = n / i

    if n > 2:
        res.append(int(n))

    res = list(set(res))
    return res




def sum_for_list(lst):
    
    final_dict = {}

    for i in lst:
        for prime_num in primeFactors(i):
            if (prime_num in final_dict.keys()):
                final_dict[prime_num] += i
            else:
                final_dict[prime_num] = i


    final_dict = dict(sorted(final_dict.items(), key=lambda x: x[0]))

    final_array = []

    for key, values in final_dict.items():
        final_array.append([key, values])

    return final_array









# test 

class Test(unittest.TestCase):

    def test_sum_prime_factor(self):

        a = [12, 15]
        self.assertEqual(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])

        b = [-29804, -4209, -28265, -72769, -31744]
        self.assertEqual(sum_for_list(b), [[2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], [7451, -29804]])


if __name__ == "__main__":
    unittest.main()

