"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""

import unittest


def pprint_matrix(A):
    for row in A:
        print("{}".format(row))
    print("\n")

def zero_matrix(A):

    num_lin = len(A)
    num_col = len(A[0])

    zero_list = []

    for i in range (num_lin):
        for j in range (num_col):

            # need to keep track of the zero and make row and col null in another loop
            if (A[i][j]) == 0:
                zero_list.append((i,j))

    pprint_matrix(A)

    for row, col in zero_list:

        for j in range(num_col):
            A[row][j] = 0

        for i in range(num_lin):
            A[i][col] = 0

        pprint_matrix(A)


    return A


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 120, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [16, 0, 18, 19, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

