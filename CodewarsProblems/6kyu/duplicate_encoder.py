# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

import unittest

def duplicate_encode(word):

    word = word.lower()
    word_dict = {}

    for char in word:
        if (char not in word_dict):
            word_dict[char] = 1
        else:
            word_dict[char] += 1

    res = ""

    for char in word:
        if (word_dict[char] == 1):
            res += "("
        else:
            res += ")"

    return res


class TestDuplicatedEncode(unittest.TestCase):
    def test_duplicated_encode(self):

        self.assertEqual(duplicate_encode("din"), "(((")
        self.assertEqual(duplicate_encode("Success"), ")())())")


if __name__ == "__main__":
    unittest.main()
