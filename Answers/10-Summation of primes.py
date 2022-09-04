"""def eratosthenes():
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
sum=0
for a in eratosthenes():
    if a<2000000:
        sum+=a
    else:
        break
print(sum)"""

prime = [1] * 2000000
a = 2
b = 0
toplam = 0
while a < 2000000:
    toplam += a
    b = a
    while b < 2000000:
        prime[b] = 0
        b += a
    while prime[a] == 0:
        a += 1
        if a==2000000:
            break
    if a==2000000:
        break
print(toplam)
