"""The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?"""

#9'dan büyük her sayının herhangi bir üssü bu kurala uymuyor. 10^2=100 misal.

count=0
for a in range(1,10):
    for b in range(1,100):
        if len(str(a**b))==b:
            count+=1
        if len(str(a**b))>b:
            break
print(count)