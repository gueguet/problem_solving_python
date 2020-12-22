# https://www.codewars.com/kata/58d06bfbc43d20767e000074/train/python

import unittest

class SecureList():
    def __init__(self, my_message):
        self.message = my_message.copy() # be careful otherwise il will delete the original message
        
    def __getitem__(self, key):
        tmp_item = self.message.__getitem__(key)
        del self.message[key]
        return tmp_item

    def __str__(self):
        tmp_str = self.message.__str__()
        self.message = []
        return tmp_str

    def __repr__(self):
        self.message = []
        return self.message.__repr__()

    def __len__(self):
        return len(self.message)



# test

class SecureListTest(unittest.TestCase):

    def test_only_readable_one(self):

        base=[1,2,3,4]

        a=SecureList(base)
        self.assertEqual(a[0],base[0],"List returned wrong value.")
        self.assertEqual(a[0],base[1],"List returned wrong value.")
        self.assertEqual(len(a),2,"List hasn't deleted it's items once accessed")

        print("current List: %s"%a)
        self.assertEqual(len(a),0,"List Should be empty after printing")

        a=SecureList(base)
        print("current List: %r"%a)
        self.assertEqual(len(a),0,"List Should be empty after printing a representation")



if __name__ == "__main__":
    unittest.main()
