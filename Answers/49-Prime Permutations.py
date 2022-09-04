"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?"""

import math, time
start=time.time()

def prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def comolokko():
    liste = []
    for a in range(999, 9999):
        if prime(a):
            liste.append(a)
    for a in liste:
        for b in liste:
            for c in liste:
                if c-b==b-a and not a==b==c and set(str(a))==set(str(b))==set(str(c)) and not str(a)+str(b)+str(c)=="148748178147":
                    return print(str(a)+str(b)+str(c))
comolokko()
end=time.time()
print(end-start)