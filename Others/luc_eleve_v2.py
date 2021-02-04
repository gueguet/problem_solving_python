#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest

from termcolor import cprint

def count_occurrences_in_text(word, text):
    """
    Return the number of occurrences of the passed word (case insensitive) in text
    """

    # TODO: your code goes here, but it's OK to add new functions or import modules if needed

    counter = 0
    word = word.lower()

    # replace big sequence of special character
    for spe_char in ["'''''","'''","''","_"]:
      text = text.replace(spe_char, "")

    # double word
    ### TODO : optimize this part ###
    if (" " in word):

      delimitors_start = ["\u201c", "(", "'","«","\""]
      delimitors_end = ["\u201d", ")", "'","»"]

      # check if any delimitor present
      for idx, item in enumerate(delimitors_start):
            
        if (item in text):

          # very specific case with '
          if (item == "'" and word[0] == "'" and word[-1] == "'"):
            if word in text.lower():
              counter += 1
              return counter

          elif (item == "'"):
            if ("'" in word and word in text.lower()):
                counter += 1
            return counter

          elif (item == "\""):
            if word in text.replace('\n', " ").lower():
              counter += 1
              return counter

          # other separator
          else:
            if ((delimitors_start[idx] + word + delimitors_end[idx]) in text.lower()):
              counter += 1
              return counter

      # no delimitor
      if (word.lower() in text.lower()):
        counter += 1
        return counter


    # single word
    ### TODO : try in with exact match... ? without re which is too slow...
    else:
      for delimiter in ['?','!','.','\n',',',':']:
        text = text.replace(delimiter, '|')

      for sub in text.lower().split("|"):
        # need to be sure that the match is exact...
        # pb --> the "in" will also count the substring 
        # example : "george" in "georges do something" --> True

        if (word in sub):
          for item in sub.split(" "):
            if (item == word):
              counter += 1

    return counter



class TestCountoccurrencesInText(unittest.TestCase):
    def test_count_occurrences_in_text(self):
      """
      Test the count_occurrences_in_text function
      """
      text = """Georges is my name and I like python. Oh ! your name is georges? And you like Python!
Yes is is true, I like PYTHON
and my name is GEORGES"""

      # test with a little text.
      self.assertEqual(3, count_occurrences_in_text("Georges", text))
      self.assertEqual(3, count_occurrences_in_text("GEORGES", text))
      self.assertEqual(3, count_occurrences_in_text("georges", text))
      self.assertEqual(0, count_occurrences_in_text("george", text))
      self.assertEqual(3, count_occurrences_in_text("python", text))
      self.assertEqual(3, count_occurrences_in_text("PYTHON", text))
      self.assertEqual(2, count_occurrences_in_text("I", text))
      self.assertEqual(0, count_occurrences_in_text("n", text))
      self.assertEqual(1, count_occurrences_in_text("true", text))
      # regard ' as text:
      self.assertEqual(0, count_occurrences_in_text("maley", "John O'maley is my friend"))

      # Test it but with a BIG length file. (we once had a memory error with this...)
      text = """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
      text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
      text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
      text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
      text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
      text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
      text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
      text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
      text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
      text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
      text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
      text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
      text += """The quick brown fox jump over the true lazy dog.The quick brown fox jump over the lazy dog."""
      text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
      text += """ I vsfgsdfg sfdg sdfg sdgh sgh I sfdgsdf"""
      text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500

      self.assertEqual(3, count_occurrences_in_text("Georges", text))
      self.assertEqual(3, count_occurrences_in_text("GEORGES", text))
      self.assertEqual(3, count_occurrences_in_text("georges", text))
      self.assertEqual(0, count_occurrences_in_text("george", text))
      self.assertEqual(3, count_occurrences_in_text("python", text))
      self.assertEqual(3, count_occurrences_in_text("PYTHON", text))
      self.assertEqual(2, count_occurrences_in_text("I", text))
      self.assertEqual(0, count_occurrences_in_text("n", text))
      self.assertEqual(1, count_occurrences_in_text("true", text))


      # double word
      # handle open + close symbols
      self.assertEqual(0, count_occurrences_in_text("reflexion mirror",
                                                    "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida"))
      self.assertEqual(1, count_occurrences_in_text("'reflexion mirror'",
                                                    "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida"))
      self.assertEqual(1, count_occurrences_in_text("reflexion mirror",
                                                    "I am a senior citizen and I live in the Fun-Plex (Reflexion Mirror) in Sopchoppy, Florida"))


      self.assertEqual(1, count_occurrences_in_text("reflexion mirror",
                                                    "Reflexion Mirror\" in Sopchoppy, Florida"))


      self.assertEqual(1, count_occurrences_in_text("reflexion mirror",
                                                    "I am a senior citizen and I live in the Fun-Plex «Reflexion Mirror» in Sopchoppy, Florida"))

      self.assertEqual(1, count_occurrences_in_text("reflexion mirror",
                                                    "I am a senior citizen and I live in the Fun-Plex \u201cReflexion Mirror\u201d in Sopchoppy, Florida"))


      # handle multiple words
      self.assertEqual(1, count_occurrences_in_text("get back to me",
                                                    "I hope you will consider this proposal, and get back to me as soon as possible"))

      self.assertEqual(1, count_occurrences_in_text("skin-care",
                                                    "enable Delavigne and its subsidiaries to create a skin-care monopoly"))
      self.assertEqual(1, count_occurrences_in_text("skin-care monopoly",
                                                    "enable Delavigne and its subsidiaries to create a skin-care monopoly"))
      self.assertEqual(0, count_occurrences_in_text("skin-care monopoly in the US",
                                                    "enable Delavigne and its subsidiaries to create a skin-care monopoly"))
      self.assertEqual(1, count_occurrences_in_text("get back to me",
                                                    "When you know:get back to me"))

      self.assertEqual(1, count_occurrences_in_text("don't be left", """emergency alarm warning.
Don't be left unprotected. Order your SSSS3000 today!"""))
      self.assertEqual(1, count_occurrences_in_text("don", """emergency alarm warning.
Don't be left unprotected. Order your don SSSS3000 today!"""))
      self.assertEqual(1, count_occurrences_in_text("take that as a 'yes'",
                                                    "Do I have to take that as a 'yes'?"))
      self.assertEqual(1, count_occurrences_in_text("don't take that as a 'yes'",
                                                    "I don't take that as a 'yes'?"))
      self.assertEqual(1, count_occurrences_in_text("take that as a 'yes'",
                                                    "I don't take that as a 'yes'?"))
      self.assertEqual(1, count_occurrences_in_text("don't",
                                                    "I don't take that as a 'yes'?"))


      self.assertEqual(1, count_occurrences_in_text("attaching my c.v. to this e-mail",
                                                    "I am attaching my c.v. to this e-mail."))

      self.assertEqual(1, count_occurrences_in_text("Linguist",
                                                    "'''Linguist Specialist Found Dead on Laboratory Floor'''"))
      self.assertEqual(1, count_occurrences_in_text("Linguist Specialist",
                                                    "'''Linguist Specialist Found Dead on Laboratory Floor'''"))
      self.assertEqual(1, count_occurrences_in_text("Laboratory Floor",
                                                    "'''Linguist Specialist Found Dead on Laboratory Floor'''"))
      self.assertEqual(1, count_occurrences_in_text("Floor",
                                                    "'''Linguist Specialist Found Dead on Laboratory Floor'''"))
      self.assertEqual(1, count_occurrences_in_text("Floor",
                                                    "''Linguist Specialist Found Dead on Laboratory Floor''"))
      self.assertEqual(1, count_occurrences_in_text("Floor",
                                                    "__Linguist Specialist Found Dead on Laboratory Floor__"))
      self.assertEqual(1, count_occurrences_in_text("Floor",
                                                    "'''''Linguist Specialist Found Dead on Laboratory Floor'''''"))
      self.assertEqual(1, count_occurrences_in_text("Linguist",
                                                    "'''Linguist Specialist Found Dead on Laboratory Floor'''"))
      self.assertEqual(1, count_occurrences_in_text("Linguist",
                                                    "''Linguist Specialist Found Dead on Laboratory Floor''"))
      self.assertEqual(1, count_occurrences_in_text("Linguist",
                                                    "__Linguist Specialist Found Dead on Laboratory Floor__"))
      self.assertEqual(1, count_occurrences_in_text("Linguist",
                                                    "'''''Linguist Specialist Found Dead on Laboratory Floor'''''"))


SAMPLE_TEXT_FOR_BENCH = """
A Suggestion Box Entry from Bob Carter

Dear Anonymous,

I'm not quite sure I understand the concept of this 'Anonymous' Suggestion Box. If no one reads what we write, then how will anything ever
change?

But in the spirit of good will, I've decided to offer my two cents, and hopefully Kevin won't steal it! (ha, ha). I would really like to
see more varieties of coffee in the coffee machine in the break room. 'Milk and sugar', 'black with sugar', 'extra sugar' and 'cream and su
gar' don't offer much diversity. Also, the selection of drinks seems heavily weighted in favor of 'sugar'. What if we don't want any suga
r?

But all this is beside the point because I quite like sugar, to be honest. In fact, that's my second suggestion: more sugar in the office.
Cakes, candy, insulin, aspartame... I'm not picky. I'll take it by mouth or inject it intravenously, if I have to.

Also, if someone could please fix the lock on the men's room stall, that would be helpful. Yesterday I was doing my business when Icarus ne
arly climbed into my lap.

So, have a great day!

Anonymously,
Bob Carter
"""


def doit():
    """
    Run count_occurrences_in_text on a few examples
    """
    i = 0
    for x in range(400):
        i += count_occurrences_in_text("word", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("sugar", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("help", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("heavily", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("witfull", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("dog", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("almost", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("insulin", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("attaching", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("asma", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("neither", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("won't", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("green", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("parabole", SAMPLE_TEXT_FOR_BENCH)
    print(i)


# Start the tests
#     # # I need to be fast as well:
#     # import profile
#     # profile.run('doit()')


if __name__ == '__main__':
    import profile
    profile.run('doit()')
    unittest.main()



