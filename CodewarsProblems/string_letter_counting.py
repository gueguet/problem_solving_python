# https://www.codewars.com/kata/59e19a747905df23cb000024/train/python


from collections import Counter
from pprint import pprint
import unittest

def string_letter_counting(my_string):

    letter_dict = {}

    my_string = my_string.lower().replace(" ", "")


    for l in my_string:

        if l.isalpha():
            if l in letter_dict:
                letter_dict[l] += 1
            else:
                letter_dict[l] = 1

    sorted_letter_dict = dict( sorted(letter_dict.items(),key= lambda x:x[0].lower()) )

    res = ""
    for key in sorted_letter_dict:
        res += str(sorted_letter_dict[key])
        res += key

    return res



# test 

class Test(unittest.TestCase):

    def test_string_letter_counting(self):

        self.assertEqual(string_letter_counting("The quick brown fox jumps over the lazy dog."),
                         "1a1b1c1d3e1f1g2h1i1j1k1l1m1n4o1p1q2r1s2t2u1v1w1x1y1z")
        self.assertEqual(string_letter_counting(
            "The time you enjoy wasting is not wasted time."), "2a1d5e1g1h4i1j2m3n3o3s6t1u2w2y")
        self.assertEqual(string_letter_counting("./4592#{}()"), "")



if __name__ == "__main__":
    unittest.main()


# better solution --> just use counter !

def string_letter_count_2(s):
    cnt = Counter(c for c in s.lower() if c.isalpha())
    return ''.join(str(n)+c for c, n in sorted(cnt.items()))

