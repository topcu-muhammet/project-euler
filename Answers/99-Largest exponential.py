"""Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.
Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.
NOTE: The first two lines in the file represent the numbers in the example given above."""

"""50^12 = 12*log(50)"""


import math, time
start=time.time()
sayilar=open("G:/Programlama/Project Euler/p099_base_exp.txt", "r")

a="3"
max=0
base="0"
exp="0"
counter=0
sira=0
uzunluk=0

while a!='':
    counter+=1
    try:
        if a=='':
            continue
        else:
            a=sayilar.readline()
            a=a.strip('\n')
            b = a.split(",")
            uzunluk=math.log(int(b[0]), 10)*int(b[1])
            if uzunluk>=max:
                base=b[0]
                exp=b[1]
                max=uzunluk
                sira=counter
    except ValueError:
        continue
    except IndexError:
        continue

print(sira)
end=time.time()
print(end-start)
