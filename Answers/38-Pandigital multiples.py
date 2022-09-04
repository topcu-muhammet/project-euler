"""Pandigital multiples
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?"""
import time
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
start=time.time()
max=0
max_a=0
max_b=0
for a in range(1,10000):
    d = ""
    for b in range(1,50):
        c=a*b
        d=d+str(c)
        if len(d)>9:
            break
        if len(d)==9 and pandigital(int(d)) and int(d)>max:
            max=int(d)
            max_a=a
            max_b=b
print(max)
end=time.time()
print(end-start)