"""
Is Unique: Implement an algorithm to determine if a string has
all unique characters.
What if you cannot use additional data structures?
"""

import unittest


def is_unique(my_string):
    letter_dict = {}

    for letter in my_string:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

    for letter in my_string:
        if letter_dict[letter] > 1:
            return False

    return True


# Test


class Test(unittest.TestCase):
    data_true = [("abcd"), ("zea ")]
    data_false = [("abca"), ("z z")]

    def test_is_unique(self):

        # true res
        for test_string in self.data_true:
            res = is_unique(test_string)
            self.assertTrue(res)

        # false res
        for test_string in self.data_false:
            res = is_unique(test_string)
            self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()
