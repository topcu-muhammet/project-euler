# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math


def factorize(n):
    """
    This function gives factors of a number.
    @param n: int
    @return: list
    """
    if n == 1:
        return []  # special case
    factors = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n + 1)
    i = 3
    while i <= limit:
        if n % i == 0:
            factors.append(i)
            n //= i
            limit = math.sqrt(n + i)
        else:
            i += 2
    if n != 1:
        factors.append(n)
    return factors


def smallest_multiple():
    numbers = [i for i in range(1, 21)]
    factors = []
    for i in numbers:
        # print(factorize(i))
        for s in factorize(i):
            if factorize(i).count(s) > factors.count(s):
                for i in range(1, factorize(i).count(s) - factors.count(s) + 1):
                    factors.append(s)
    result = 1
    for i in factors:
        result *= i
    return result


print(smallest_multiple())
