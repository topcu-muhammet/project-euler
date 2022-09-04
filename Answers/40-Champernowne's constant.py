#Champernowne's constant
#Problem 40
#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following expression.
#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
import time
start=time.time()
metin=""
for a in range(1,10101010):
    metin=metin+str(a)
    if len(metin)>1000000:
        break
print(int(metin[0])*int(metin[9])*int(metin[99])*int(metin[999])*int(metin[9999])*int(metin[99999])*int(metin[999999]))
end=time.time()
print(end-start)