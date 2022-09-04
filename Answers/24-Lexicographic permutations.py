"""A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""


"""Algrotima:

Condensed mathematical description:

Find the largest x such that P[x]<P[x+1].
(If there is no such x, P is the last permutation.)
Find the largest y such that P[x]<P[y].
Swap P[x] and P[y].
Reverse P[x+1 .. n].."""
import time
start=time.time()

liste=[0,1,2,3,4,5,6,7,8,9]

def lex_permutation(a, b): #üstteki iki fonksiyonu da kullanarak içine yazılan listenin tüm potansiyel permutasyonlarını bulur.
    sayac=1 #kacıncı permutasyonda olduğu
    while sayac!=b: #istediğimiz sıradaki permutasyona gelene kadar döngüde kalacak.
        for i in range(len(a)-2, -1, -1):#p[x]'i bulma
            if int(a[i])<int(a[i+1]):
                x=i
                break
        for i in range(len(a)-1, -1, -1):#p[y]'yi bulma
            if int(a[i])>int(a[x]):
                y=i
                break
        a[x], a[y]=a[y], a[x] #p[x] ve p[y]yi değiştirmek
        a = a[:x + 1] + a[:x:-1] #p[x]ten sonrasını tersine çevirme
        sayac+=1
    return print(a)

lex_permutation(liste, 1000000)
end=time.time()
print(end-start)