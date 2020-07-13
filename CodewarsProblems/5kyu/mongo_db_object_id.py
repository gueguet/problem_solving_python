# https://www.codewars.com/kata/52fefe6cb0091856db00030e/train/python


from datetime import datetime
import unittest

class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        """returns True if s is a valid MongoID; otherwise False"""

        if (isinstance(s, str)):

            if (len(s) == 24) and s.islower() and all(c in '0123456789abcdef' for c in s):
                return True

        return False





    @classmethod
    def get_timestamp(cls, s):
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""

        if (Mongo.is_valid(s) == True):
            extract_date = datetime.fromtimestamp(int(s[:8], base=16))
            return extract_date

        else:
            return False





# test 

class Test(unittest.TestCase):

    def test_mùongo_id(self):



        self.assertEqual(Mongo.is_valid('507f1f77bcf86cd79943901'), False)
        self.assertEqual(Mongo.is_valid('507f1f77bcf86cd799439016'), True)
        self.assertEqual(Mongo.is_valid(False), False)
        self.assertEqual(Mongo.is_valid([]), False)
        self.assertEqual(Mongo.is_valid(1234), False)
        self.assertEqual(Mongo.is_valid('123476sd'), False)

        
        self.assertEqual(Mongo.get_timestamp(False), False)
        self.assertEqual(Mongo.get_timestamp([]), False)
        self.assertEqual(Mongo.get_timestamp(1234), False)
        self.assertEqual(Mongo.get_timestamp('123476sd'), False)
        self.assertEqual(Mongo.get_timestamp('507f1f77bcf86cd79943901'), False)
        self.assertEqual(Mongo.get_timestamp('507f1f77bcf86cd799439016'), datetime(2012, 10, 17, 21, 13, 27))



if __name__ == "__main__":
    unittest.main()
