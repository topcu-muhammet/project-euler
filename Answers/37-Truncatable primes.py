"""Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

import math
import time

def prime(number):
    if number<2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def eratosthenes():
	'''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
	D = {}  # map composite integers to primes witnessing their compositeness
	q = 2   # first integer to test for primality
	while 1:
		if q not in D:
			yield q        # not marked composite, must be prime
			D[q*q] = [q]   # first multiple of q not already marked
		else:
			for p in D[q]: # move each witness to its next multiple
				D.setdefault(p+q,[]).append(p)
			del D[q]       # no longer need D[q], free memory
		q += 1

start=time.time()
liste=[]
for a in eratosthenes():
    if a < 10:
        continue
    if len(liste)==11:
        break
    if "0" in str(a):
        continue
    t = 0
    for j in range(4,10,2):
        if str(j) in str(a):
            t += 1
            break
    if t != 0:
        continue
    zaza=0
    for i in range(1,len(str(a))):
        b = a
        c = a
        b=int(str(b)[i:])
        c = int(str(c)[:-i])
        if not prime(b) or not prime(c):
            zaza+=1
            break
        if len(str(b))==1:
            break
    if zaza==0:
        liste.append(a)
end=time.time()
print(sum(liste))
print(end-start)