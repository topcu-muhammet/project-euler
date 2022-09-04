"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?"""

#Buradan çıkan sonuç, bizim aradığımız sonucun en az 21 terimlik bir zincir olması anlamına geliyor. Bu da bizim
#1.000.000/21'e kadar olan primelara bakmamızı gerektirir. Zira oradan sonrasının 21'lik bir zincirinin 1.000.000'u geçeceği
#aşikardır. Bu sebeple bir asal sayı dizisi oluşturup içierisini 1000000'a kadar olan asallarla dolduralım. Sınır parametresi olarak 1000000/zincir diyelim.
import time

start=time.time()

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

prime=primes_sieve2(1000000)
liste=[]
for a in prime:
    liste.append(a)
sinir=21

for a in range(0,len(liste)-sinir):
    for b in range(a+sinir, len(liste)+1):
        toplam=sum(liste[a:b])
        if toplam>1000000:
            break
        if toplam in liste and b-a>=sinir:
            sinir=b-a
            asal=toplam
        if b>1000000/sinir:
            break
    if a>1000000/sinir:
        break
print(asal)
end=time.time()
print(end-start)