# https: // www.codewars.com/kata/52840d2b27e9c932ff0016ae/train/python

# locate(['a','b',['c','d',['e']]],'e');

import unittest


# My solution :
def locate(seq, value):
    for element in seq:
        if element == value:
            return True

    for element in seq:
        if not isinstance(element, str):
            return locate(element, value)

    return False


# Better :
def locate2(seq, value):
    for s in seq:
        if s == value or (isinstance(s, list) and locate(s, value)):
            return True
    return False


# test 

class Test(unittest.TestCase):

    def test_locate(self):

        self.assertEqual(locate(['a', 'b', ['c', 'd', ['e']]], 'e'), True)

        self.assertEqual(
            locate(('two', 'six', ('five', 'seven'), 'three,nine'), 'five, seven'), False)

        self.assertEqual(locate(['a', 'b', ['c', 'd', ['e']]], 'f'), False)
        self.assertEqual(locate(
            ['a', 'b', ['c', 'd', ['e', ['a', 'b', ['c', 'd', ['e4']]]]]], 'e4'), True)
        self.assertEqual(locate(['a', 'b', ['c', 'd', ['e', ['a', 'b', ['c', 'd', ['e', ['a', 'b', ['c', 'd', ['e4', [
                       'a', 'b', ['c', 'd', ['e', ['a', 'b', ['c', 'd', ['e', ['a', 'b', ['c', 'd', ['e14']]]]]], ]]]]]]]]], ]]], 'e'), True)



if __name__ == "__main__":
    unittest.main()
