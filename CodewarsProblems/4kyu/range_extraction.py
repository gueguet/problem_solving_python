# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def range_extraction(my_list):

    my_list.sort()
    follow_int_counter = 0
    output_str = ""

    for i in range(1, len(my_list)):

        if my_list[i] == (my_list[i-1] + 1):
            follow_int_counter += 1

        else:
            if (follow_int_counter == 0):
                output_str += str(my_list[i-1]) + ","
            elif (follow_int_counter == 1):
                output_str += str(my_list[i-2]) + ","
                output_str += str(my_list[i-1]) + ","
                follow_int_counter = 0
            else:
                output_str += "{}-{},".format(
                    my_list[i - follow_int_counter - 1], my_list[i - 1])
                follow_int_counter = 0


    # last one
    if (follow_int_counter == 0):
        output_str += str(my_list[i])
    elif (follow_int_counter == 1):
        output_str += str(my_list[i - 1]) + ","
        output_str += str(my_list[i])
    else:
        output_str += "{}-{}".format(my_list[i - follow_int_counter], my_list[i])

    return output_str



import unittest

class RangeExtractionTest(unittest.TestCase):

    def testExtraction(self):

        self.assertEqual(
            range_extraction([
                -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18,
                19, 20
            ]), '-6,-3-1,3-5,7-11,14,15,17-20')

        self.assertEqual(
            range_extraction([
                1,2,3,4,5
            ]), '1-5')

if __name__ == '__main__':
    unittest.main()
