# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
kalanlar = []
max_iter = -1
number = -1
for b in range(3, 1000):
    kalanlar = []
    kalan = 1
    while kalan != 0:
        kalan = kalan % b
        kalanlar.append(kalan)
        if len(kalanlar) == 1:
            kalan *= 10
            continue
        if kalanlar[-1] in kalanlar[:-1]:
            first = kalanlar[:-1].index(kalanlar[-1])
            second = len(kalanlar) - 1
            break
        kalan *= 10
    if (second - first) > max_iter:
        max_iter = (second - first)
        number = b
print(number, max_iter)
