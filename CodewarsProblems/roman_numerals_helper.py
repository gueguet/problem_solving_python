"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. 
It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 
1666 uses each Roman symbol in descending order: MDCLXVI.
"""

import re
import unittest

rom_list = [(1000,'M'), (900,'CM') , (500,'D') , (400 , 'CD'),
        (100,'C'),(90,'XC'), (50,'L'), (40, 'XL') , (10,'X'),
        (9,'IX'), (5,'V'),(4,'IV'),(1,'I')]

class RomanNumerals():

    def to_roman(self, number):
        result = ''
        for (num, letter) in rom_list:
            result+= (number // num) * letter
            number = number % num
        
        return result


    def from_roman(self, roman):
        result = 0
        i = 0

        while i < len(rom_list):
            reg = '^' + rom_list[i][1]
            if re.search(reg , roman) != None:
                result += rom_list[i][0]
                roman = re.sub(reg,'',roman)
            else:
                i+=1

        return result




my_ronan_converter = RomanNumerals()

# test 

class Test(unittest.TestCase):

    def test_roman_convert(self):

        self.assertEqual(my_ronan_converter.to_roman(1000), 'M', '1000 should == "M"')
        self.assertEqual(my_ronan_converter.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')

        self.assertEqual(my_ronan_converter.from_roman('XXI'), 21, 'XXI should == 21')
        self.assertEqual(my_ronan_converter.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')


if __name__ == "__main__":
    unittest.main()
