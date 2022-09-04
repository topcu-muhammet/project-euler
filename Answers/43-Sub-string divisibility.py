"""The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property."""
import itertools

def pandigital(number): #0^dan 9'a pandigital olduğunu ölçmek.
    sayac=0
    if str(number)[0]==0:
        return False
    for a in range(0,len(str(number))+1):
        if str(a) in str(number) and str(number).count(str(a))==1:
            sayac+=1
        else:
            break
    if sayac==len(str(number)) and sayac<=10:
        return True
    else:
        return False

toplam=0
import itertools
liste= list(itertools.permutations([1, 2, 3, 4, 5, 6, 7 ,8, 9, 0]))
za=[]
for a in liste:
    c=""
    for b in a:
        c+=str(b)
    za.append(c)
del(liste)

for a in za:
    if int(str(a)[0])!=0:
        if int(str(a)[1:4])%2==0:
            if int(str(a)[2:5])%3==0:
                if int(str(a)[3:6])%5==0:
                    if int(str(a)[4:7]) % 7 == 0:
                        if int(str(a)[5:8]) %11 == 0:
                            if int(str(a)[6:9]) % 13 == 0:
                                if int(str(a)[7:10]) % 17 == 0:
                                    print(a)
                                    toplam+=int(a)
print("-------", "\n", toplam)


