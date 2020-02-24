"""https: // www.codewars.com/kata/53c93982689f84e321000d62/train/python"""

def getAllPrimeFactors(n):
    factors = []
    if type(n) is not int or n < 1:
        return []
    elif n < 3:
        return [n]
    while n > 1:
        for i in range(2, n+1):
            if is_prime(i) and n%i == 0:
                factors.append(i)
                n = int(n/i)
                break
    return factors


def getUniquePrimeFactorsWithCount(n):
    factors = getAllPrimeFactors(n)
    set_factors = list(set(factors))
    powers = [factors.count(factor) for factor in set_factors]
    return [set_factors, powers]


def getUniquePrimeFactorsWithProducts(n):
    factors = getUniquePrimeFactorsWithCount(n)
    return [factor**count for factor, count in zip(factors[0], factors[1])]


def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
