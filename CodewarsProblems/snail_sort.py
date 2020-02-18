"""
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
"""


def print_mat(A):
    for i in range(len(A)):
        print(A[i])
    print("\n")

# A is a matrix 
def snail_sort(A):

    print_mat(A)

    if A==[[]]: # len of this matrix == 1...
        return []

    out_list = []

    while A != []:
        
        n = len(A)
        if n == 0:
            break

        # remove top
        for i in range(n):
            out_list.append(A[0][i])
        del(A[0])
        n = len(A)

        if n == 0:
            break

        # remove right
        for i in range(n):
            out_list.append(A[i][-1])
        for i in range(n):
            del(A[i][-1])
        n = len(A)

        if n == 0:
            break

        # remove bottom !! in reverse order
        for i in range(1, n+1):
            out_list.append(A[-1][-i])
        del(A[-1])
        n = len(A)

        if n == 0:
            break

        # remove left !! inverse order
        for i in range(n-1, -1, -1):
            print(i)
            out_list.append(A[i][0])
        for i in range(n):
            del(A[i][0])
        n = len(A)

        if n == 0:
            break

    return out_list


# test 

import unittest

class SnailTest(unittest.TestCase):

    def test_snail(self):

        array = [[19, 532, 302, 739, 18], [492, 24, 557, 650, 204], [721, 199, 100, 55, 908], [936, 664, 461, 540, 69], [99, 173, 972, 97, 824]] 
        expected = [19, 532, 302, 739, 18, 204, 908, 69, 824, 97, 972, 173, 99, 936, 721, 492, 24, 557, 650, 55, 540, 461, 664, 199, 100]

        self.assertEqual(snail_sort(array), expected)


if __name__ == "__main__":
    unittest.main()
