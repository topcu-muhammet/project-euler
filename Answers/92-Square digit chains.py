"""A number chain is created by continuously adding the square of the digits in a number to form a new number
until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY
starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?"""

import time
start=time.time()

liste=[False for a in range(10000001)]
count=0
temp1=[]
for a in range(1, 10000001):
    sum = 0
    c = a
    if liste[a]== True:
        continue
    else:
        while sum != 1 and sum != 89:
            lenght = len(str(c))
            for b in range(lenght):
                sum += int(str(c)[b]) ** 2
            temp1.append(sum)
            if sum == 89:
                for a in temp1:
                    liste[a] = True
                temp=[]
                break
            elif sum == 1:
                for a in temp1:
                    liste[a] = False
                temp1=[]
                break
            c = sum
            sum = 0

print(liste.count(True))
end=time.time()
print(end-start)

"""

import time
start=time.time()
count=0
for a in range(1, 10000000):
    sum = 0
    c = a
    while sum!=1 and sum!=89:
        lenght = len(str(c))
        for b in range(lenght):
            sum+=int(str(c)[b])**2
        if sum==89:
            count+=1
            break
        elif sum==1:
            break
        c=sum
        sum=0

print(count)
end=time.time()
print(end-start)"""