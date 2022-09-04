"""There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3=10.

In general, nCr=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.

It is not until n=23, that a value exceeds one-million: 23C10=1144066.

How many, not necessarily distinct, values of nCr for 1≤n≤100, are greater than one-million?"""

import time

start=time.time()

count=0
def fact(n):
    if n>1:
        return n*fact(n-1)
    else:
        return 1

for c in range(1,101):
    for r in range(c,0,-1):
        comb=(fact(c))/(fact(r)*fact(c-r))
        if comb>1000000:
            count+=1
print(count)
end=time.time()
print(end-start)