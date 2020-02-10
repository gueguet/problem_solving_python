"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
"""

import unittest

def string_compression(my_string):

    output_list = []
    letter_counter = 0

    for letter in my_string:

        # letter is the last seen
        if output_list != [] and type(output_list[-1] == "string") and letter == output_list[-1]:
            letter_counter += 1

        else:
            if(letter_counter >= 1):
                output_list.append(letter_counter)
            output_list.append(letter)

            letter_counter = 1

    # check fot the last letter
    if letter_counter >= 1:
        output_list.append(letter_counter)

    # return the outpu only if it's 'benefical'
    if len(output_list) < len(my_string):
        output_string = ""
        for value in output_list:
            output_string += str(value)
        return output_string

    else:
        return my_string


string_compression("aabcccccaaa")


# test
class Test(unittest.TestCase):

    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
