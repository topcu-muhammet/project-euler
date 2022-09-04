"""Euler discovered the remarkable quadratic formula:

n2+n+41 It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However,
when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The
product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4 Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with
n=0. """
import math


def prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def quadratic_formula(n, a, b):
    return (n * n) + (a * n) + b

max_a = 0
max_b = 0
max_primes = 0

for a in range(-999, 1000, 1):
    for b in range(2, 1001, 1):
        n = 0
        while n >= 0:
            number = quadratic_formula(n, a, b)
            if number < 2:
                break
            if not prime(number):
                break
            n += 1
        if max_primes < n:
            max_primes = n
            max_a = a
            max_b = b

print(max_primes)
print(max_a*max_b)
print(max_a,max_b)