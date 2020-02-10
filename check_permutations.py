"""
Check Permutation: Given two strings, write a method to decide if one is 
a permutation of the other.
"""

import unittest
import time


def check_permutation(string_1, string_2):

    if (len(string_1) != len(string_2)):
        return False

    dict_string_1 = {}
    dict_string_2 = {}

    for letter in string_1:
        if letter not in dict_string_1:
            dict_string_1[letter] = 1
        else:
            dict_string_1[letter] += 1

    for letter in string_2:
        if letter not in dict_string_2:
            dict_string_2[letter] = 1
        else:
            dict_string_2[letter] += 1

    if dict_string_1 == dict_string_2:
        return True
    else:
        return False


# test

class Test(unittest.TestCase):
    def test_permutation(self):
        data_true = ("abc", "bca")
        data_false = ("abba", "aba")

        self.assertTrue(check_permutation(data_true[0], data_true[1]))
        self.assertFalse(check_permutation(data_false[0], data_false[1]))


if __name__ == "__main__":
    unittest.main()

"""
We could have use Counter() collections
"""
