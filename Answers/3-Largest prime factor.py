#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?
import time
start=time.time()
def zaza(sayi):
    dizi = []
    for i in range(2, sayi+1):
        if sayi%i==0:
            dizi.append(i)
        while sayi%i==0:
            sayi=sayi/i
        if sayi==1:
            break
    return dizi[-1]
print(zaza(600851475143))
end=time.time()
print(end-start)