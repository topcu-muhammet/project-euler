#Digit factorials
#Problem 34
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
import time
def facto(n):
    if n>0:
        return n*facto(n-1)
    else:
        return 1

faktoriyeller=[facto(n) for n in range(1,10)]
print(faktoriyeller)
def to_digits(sayi):
    a=str(sayi)
    liste=[int(b) for b in a]
    liste.sort()
    return liste

def digit_facto(number):
    toplam=0
    liste=to_digits(number)
    if len(liste)==2 and liste[0]>4:
        return None
    elif len(liste)==3 and liste[0]>5 and liste[1]>5:
        return None
    elif len(liste)==4 and liste[0]>6 and liste[0]>6:
        return None
    elif len(liste)==4 and liste[0]>7:
        return None
    elif len(liste)==5 and liste[0]>8:
        return None
    for a in liste:
        if facto(a)>number:
            return None
        elif number>facto(a):
            toplam+=facto(a)
        if toplam==number:
            return number
start=time.time()
cevap=[]
for a in range(10, 1500000):#neden sınır 1.5 milyon? Sebebi şöyle:
    if digit_facto(a)!=None:
        cevap.append(digit_facto(a))
print(cevap)
end=time.time()
print(end-start)
#If n is a natural number of d digits that is a factorion, then 10d − 1 ≤ n ≤ 9!d. This fails to hold for d ≥ 8 thus n has at most 7 digits, and the first upper bound is 9,999,999.
#But the maximum sum of factorials of digits for a 7 digit number is 9!*7 = 2,540,160 establishing the second upper bound.
#All factorials of digits at least 5 have the factors 5 and 2 and thus end on 0. Let 1abcdef denote our 7 digit number.
#If all digits a-f are all at least 5, the sum of the factorials – which is supposed to be equal to 1abcdef – will end on 1 (coming from the 1! in the beginning).
#This is a contradiction to the assumption that f is at least 5. Thus, at least one of the digits a-f can be at most 4, which establishes 1!+4!+5*9!=1814425
#as fifth upper bound. Assuming n is a 7 digit number, the second digit is at most 8. There are two cases: If a is at least 5,
#by the same argument as above one of the remaining digits b-f has to be at most 4. This implies an upper bound (since a is at most 8) of 1!+8!+4!+4*9!= 1491865,
#a contradiction to a being at least 5. Thus, a is at most 4 and the sixth upper bound is 1499999.
