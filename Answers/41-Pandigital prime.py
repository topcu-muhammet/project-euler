"""Pandigital prime
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?"""

import math
import time
start=time.time()
def prime(number):
    if number<2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def pandigital(number):
    sayac=0
    for a in range(1,len(str(number))+1):
        if str(a) in str(number) and str(number).count(str(a))==1:
            sayac+=1
        else:
            break
    if sayac==len(str(number)) and sayac<=9:
        return True
    else:
        return False

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

for a in range(7654321, 0, -2):#9 ve 8 basamaklı pandigital sayıların tümü 3ün katıdır.
    if pandigital(a):
        if prime(a):
            print(a)
            break
end=time.time()
print(end-start)