"""
Given a string, write a function to check if it
is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
"""


import unittest
from collections import Counter


def exist_palindrome(my_string):

    # first we need to remove stape and ponctuation
    alpha_only = [letter for letter in my_string.lower() if letter.isalpha()]
    print(alpha_only)

    # create counter
    cnt = Counter()
    for letter in alpha_only:
        cnt[letter] += 1

    # a palindrome can exist only if there 0 or 1 odd (pivot) count 
    number_of_odd = 0
    print(cnt)
    for letter, count in cnt.items():
        if (count%2):
            number_of_odd += 1
    
    return number_of_odd <= 1



exist_palindrome("Tact Coa")
