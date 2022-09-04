"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further
by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

import math
def perfect_number(n): #bu fonksiyon sayının çarpanlarının toplamını verir.
    if n == 1:
        return 0  # special case
    toplam=0
    # iterate over all even numbers first.
    for number in range(2, int(math.sqrt(n))+1):
        if n%number==0:
            toplam+=(number)
            if number!=(n/number):
               toplam+=(int(n/number))
    toplam+=1
    if toplam==n:
        return "Perfect"
    elif toplam>n:
        return "Abundant"
    else:
        return "Deficient"

abundant_liste=[]
toplam=0
for number in range(1,28123):
    if perfect_number(number)=="Abundant":
        abundant_liste.append(number)

for number in range(24,28123):
    for a in abundant_liste:
        if number-a in abundant_liste:
            break
        if number-a<0:
            toplam+=number
            break

print(toplam)