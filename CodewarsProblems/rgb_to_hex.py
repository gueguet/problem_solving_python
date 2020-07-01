# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

import unittest

hex_dict = {
    0:"0",
    1:"1",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F"
}




def dec_to_hex(num):
    if (0 <= num <= 255):
        q = num // 16
        r = num % 16
        return hex_dict[q] + hex_dict[r]
    
    elif (num < 0):
        return "00"

    elif (num > 255):
        return "FF"


def rgb(r, g, b):
    return dec_to_hex(r) + dec_to_hex(g) + dec_to_hex(b)




# test 

class Test(unittest.TestCase):

    def test_rgb(self):

        self.assertEqual(rgb(0, 0, 0), "000000", "testing zero values")
        self.assertEqual(rgb(1, 2, 3), "010203", "testing near zero values")
        self.assertEqual(rgb(255, 255, 255), "FFFFFF", "testing max values")
        self.assertEqual(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        self.assertEqual(rgb(-20, 275, 125), "00FF7D", "testing out of range values")



if __name__ == "__main__":
    unittest.main()
    
    
# or we can simply use the converter of python... 
def rgb(r, g, b):
    def round(x): return min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
