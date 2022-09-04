"""The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact,
41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube."""

#it must be at least 5 digit to have 5 permutations, so our cube must start from 22 whose cube is 10.648.
import time

start=time.time()

cubes=[]
uzunluk=5
sayi=1
count=1
test=False
while True:
    for a in range(sayi, 100000):
        b=a**3
        if len(str(b)) > uzunluk:
            break
        cubes.append(sorted(list(str(b))))
        count+=1
    for a in cubes:
        if cubes.count(a)==5:
            print((cubes.index(a)+sayi)**3)
            test=True
            break
    if test:
        break
    sayi=count
    uzunluk+=1
    cubes=[]
end=time.time()
print(end-start)