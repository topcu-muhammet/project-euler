"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

import math
def sum_factorize(n): #bu fonksiyon sayının çarpanlarının toplamını verir.
    if n < 1:
        raise ValueError('fact() argument should be >= 1')
    if n == 1:
        return []  # special case
    res = []
    # iterate over all even numbers first.
    for number in range(2, int(math.sqrt(n))+1):
        if n%number==0:
            res.append(number)
            res.append(int(n/number))
    res.append(1)
    return sum(res)

toplam=0
liste=[]
for a in range(2,10000):
    b=sum_factorize(a)
    if (sum_factorize(b)==a) and (a!=b) and (a not in liste):
        toplam=toplam+a+b
        liste.append(b)
print(toplam)

