# https://www.codewars.com/kata/55a29405bc7d2efaff00007c/train/python
# un = (1 / n!) * (1! + 2! + 3! + ... + n!)

import math
from decimal import Decimal

"""
def factoriel(n):
   if n == 1:
       return n
   else:
       return (n * factoriel(n-1))


def fact_suite(n):
    res = 0
    for i in range(1, n+1):
        res += factoriel(i)
    return res


def going(n):
    res = Decimal(1/factoriel(n)) * Decimal(fact_suite(n))
    res = float(str(res)[:8])
    return float(Decimal(res).normalize())
"""


def factoriel(n):
   if n == 1:
       return n
   else:
       return (n * factoriel(n-1))


def fact_suite(n):
    res = 0
    for i in range(1, n+1):
        res += factoriel(i)
    return res

# using log allow us to not have any conversion problem with large int number
def going(n):
    res = math.log(1) - math.log(factoriel(n)) + math.log(fact_suite(n))
    res = round(res, 9)
    res = math.exp(res)
    res = float(str(res)[:8])
    return float(Decimal(res).normalize())

# NOT FINISHED --> PB WHEN GO TO SUCH HIGH NUMBER
print(going(998))
