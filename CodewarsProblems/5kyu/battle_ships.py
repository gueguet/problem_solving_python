# https://www.codewars.com/kata/58d06bfbc43d20767e000074/train/python
# 1 to 3 boats

import unittest
from collections import Counter


def damaged_or_sunk(board, attacks):

    # initialize boat present on the board
    boat_len = Counter()
    for i in range(len(board)):
        for j in range(len(board[0])):
            boat_num = board[i][j]
            if boat_num != 0:
                boat_len[boat_num] += 1

    # dict for touched boat
    boat_touch = Counter()
    for atck in attacks:
        atck_boat = board[-atck[1]][atck[0]-1]
        if atck_boat != 0:
            boat_touch[atck_boat] += 1

    # scoer implementation
    final_output = {'sunk': 0, 'damaged': 0, 'not_touched': 0, 'points': 0}
    for keys, values in boat_len.items():

        if keys in boat_touch:
            if boat_touch[keys] == boat_len[keys]:
                final_output['points'] += 1
                final_output['sunk'] += 1
            else:
                final_output['points'] += 0.5
                final_output['damaged'] += 1

        else:
            final_output['not_touched'] += 1
            final_output['points'] -= 1

    return final_output


# test

class BattleShipTest(unittest.TestCase):
    def test_battle_ship(self):

        board_1 = [[0, 0, 1, 0],
                   [0, 0, 1, 0],
                   [0, 0, 1, 0]]

        attacks_1 = [[3, 1], [3, 2], [3, 3]]

        expected_1 = {'sunk': 1, 'damaged': 0, 'not_touched': 0,
                      'points': 1}

        self.assertEqual(damaged_or_sunk(board_1, attacks_1), expected_1)

        board_2 = [[3, 0, 1],
                   [3, 0, 1],
                   [0, 2, 1],
                   [0, 2, 0]]

        attacks_2 = [[2, 1], [2, 2], [3, 2], [3, 3]]

        expected_2 = {'sunk': 1, 'damaged': 1, 'not_touched': 1,
                      'points': 0.5}

        self.assertEqual(damaged_or_sunk(board_2, attacks_2), expected_2)


if __name__ == "__main__":
    unittest.main()
