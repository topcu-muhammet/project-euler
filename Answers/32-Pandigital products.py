#Pandigital products
#Problem 32
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

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

liste=[]
for a in range(100, 988):
    for b in range(10,99):
        if pandigital(str(a)+str(b)+str(a*b)) and ((a*b) not in liste):
            liste.append(a*b)
for a in range(1000, 5000):
    for b in range(2,9):
        if pandigital(str(a)+str(b)+str(a*b)) and ((a*b) not in liste):
            liste.append(a*b)

print(sum(liste))
