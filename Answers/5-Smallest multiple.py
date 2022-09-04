#pozitif tüm çarpanlarını bulmak
import math
def factorize(n): #bu fonksiyon sayının çarpanlarını verir.
    if n == 1:
        return []  # special case
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n + 1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n + i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res

sayilar=[i for i in range(1,21)]
carpanlar=[]
for i in sayilar:
    #print(factorize(i))
    for s in factorize(i):
        if factorize(i).count(s)>carpanlar.count(s):
            for i in range(1, factorize(i).count(s)-carpanlar.count(s)+1):
                carpanlar.append(s)
sonuc=1
for i in carpanlar:
    sonuc*=i
print(sonuc)
