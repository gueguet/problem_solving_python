# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

'''
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
'''

from collections import Counter
import unittest

def score(dice_list):

    # create dictionnary
    dice_counter = Counter()

    for dice_res in dice_list:
        dice_counter[dice_res] += 1

    final_score = 0
    triple_score_table = {1:1000, 2:200, 3:300, 4:400, 5:500, 6:600}
    unique_score_table = {1:100, 2:0, 3:0, 4:0, 5:50, 6:0}

    for key, value in dice_counter.items():
        final_score += ((value // 3) * triple_score_table[key] + (value % 3) * unique_score_table[key])

    return final_score

# test 

class DiceTest(unittest.TestCase):

    def test_dice(self):

        self.assertEqual(score([2, 3, 4, 6, 2]), 0)
        self.assertEqual(score([4, 4, 4, 3, 3]), 400)
        self.assertEqual(score([2, 4, 4, 5, 4]), 450)


if __name__ == "__main__":
    unittest.main()
