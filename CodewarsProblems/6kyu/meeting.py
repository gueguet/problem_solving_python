# https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python

from pprint import pprint

import unittest


def meeting(s):
    s = s.upper().split(";")

    dict_name = {}
    for element in s:
        if element.split(":")[1] not in dict_name:
            dict_name[element.split(":")[1]] = [element.split(":")[0]]
        else:
            dict_name[element.split(":")[1]].append(element.split(":")[0])

    output = ""

    for last_name in sorted(dict_name):
        for first_name in sorted(dict_name[last_name]):
            output += "({}, {})".format(last_name, first_name)

    print(output)
    return output


if __name__ == "__main__":
    s = "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
    meeting(s)

    "(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)"
    "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"



# good solution

"""
def meeting(s):
  s = s.upper()
  s = s.split(';')
  array = []
  string = ""
  for i in s:
    i = i.split(':')
    string = '('+i[1]+', '+i[0]+')'
    array.append(string)
  array.sort()
  output = ""
  for j in array:
    output += j
  return output
"""