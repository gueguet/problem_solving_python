# https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/train/python

import binascii

def encode(string):

    ascii_arr = []
    bin_arr = []
    tripled_arr = []

    for char in string:
        ascii_arr.append(ord(char))
    
    for ascii_val in ascii_arr
        bin_arr.append(binascii.a2b_uu(ascii_val))

    print(ascii_arr)

encode("hey")



