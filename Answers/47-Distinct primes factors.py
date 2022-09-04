"""The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?"""
import time
def distinct_prime_factors(in_num):
    i = 2
    distinct_factors = set()
    while i * i <= in_num:#Proof: Suppose n is a positive integer s.t. n=pq, where p and q are prime numbers. Assume p>n−−√ and q>n−−√.
        # Multiplying these inequalities we have p.q>n−−√.n−−√,
        # which implies pq>n. This is a contradiction to our hypothesis n=pq. Hence we can conclude that either p≤n−−√ or q≤n−−√.
        if in_num % i:
            i += 1
        else:
            in_num //= i
            distinct_factors.add(i)
    if in_num > 1:
        distinct_factors.add(in_num)
    return len(distinct_factors)

start=time.time()
b=0
c=0
d=0
a=1
while distinct_prime_factors(a) != 4 or distinct_prime_factors(b) != 4 or distinct_prime_factors(c) != 4 or distinct_prime_factors(d) != 4:
    if distinct_prime_factors(d)!=4:
        a=a+4
    elif distinct_prime_factors(c)!=4:
        a=a+3
    elif distinct_prime_factors(b)!=4:
        a=a+2
    elif distinct_prime_factors(a)!=4:
        a=a+1
    b = a + 1
    c = b + 1
    d = c + 1
print(a,b,c,d)
end=time.time()
print(end-start)