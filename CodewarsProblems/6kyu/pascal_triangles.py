# https://www.codewars.com/kata/5226eb40316b56c8d500030f/train/python

import unittest


def pascals_triangle(n):
    pascal_tr = [[1], [1, 1]]
    if n == 1:
        return [1]
    if n == 2:
        return [1,1,1]
    while len(pascal_tr) < n:
        last = pascal_tr[-1]
        layer = [1]
        for i in range(len(last)-1):
            layer.append(last[i]+last[i+1])
        layer.append(1)
        pascal_tr.append(layer)
    
    flatten_tr = []
    for line in pascal_tr:
        for item in line:
            flatten_tr.append(item)

    return flatten_tr


# test 

class PascalTest(unittest.TestCase):
    def test_pascal(self):

        self.assertEqual(pascals_triangle(1), [1])
        self.assertEqual(pascals_triangle(2), [1, 1, 1])
        self.assertEqual(pascals_triangle(3), [1, 1, 1, 1, 2, 1])


if __name__ == "__main__":
    unittest.main()
