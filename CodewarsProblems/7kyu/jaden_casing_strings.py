# codewars.com/kata/jaden-casing-strings/train/python


def toJadenCase(quote):
    splitQuote = quote.split()
    newQuote = ""

    
    for word in splitQuote:
        if word[0].islower():
            word.capitalize()
            newQuote += " " + word.capitalize()
        else:
            newQuote += " " + word

    return newQuote[1::]



# test 
import unittest

quote = "How can mirrors be real if our eyes aren't real"

assert toJadenCase(quote) == "How Can Mirrors Be Real If Our Eyes Aren't Real", "Should be okay" 

