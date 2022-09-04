"""It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?"""

def combinationSum(dizi, hedef):
    za = []
    for a in sorted(dizi):
        tam = hedef // a
        for b in range(tam):
            za.append(a)
    all_comb = []
    tekler = []
    comb = [[a] for a in sorted(dizi)]
    temp = []
    for a in sorted(dizi):
        tekler.append([a])
    all_comb.extend(tekler)
    tur = len(za) - 1
    while tur >= 0:
        temp2=[]
        for a in comb:
            for b in tekler:
                temp.append(a + b)
                if sorted(temp[0]) not in temp2 and sum(temp[0])<=hedef:
                    temp2.append(sorted(temp[0]))
                temp.clear()
        tur = tur - 1
        all_comb.extend(temp2)
        comb = temp2
    comolokko = [a for a in all_comb if sum(a) == hedef]
    return len(comolokko)

for a in range(100,10000000):
    if combinationSum([2,3,5,7,11,13,17,19,23,29,31], a)>5000:
        print(a)
        break