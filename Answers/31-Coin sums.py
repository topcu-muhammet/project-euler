"""In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?"""

sayac=0
for i in range(0, 201):
    h = i * 1
    for i in range(0, 101):
        g = i * 2
        if g+h > 200:
            continue
        for i in range(0, 41):
            f = i * 5
            if h+g + f > 200:
                continue
            for i in range(0, 21):
                e = i * 10
                if e+g+h+f > 200:
                    continue
                for i in range(0, 11):
                    d = i * 20
                    if e+g+h+f +d > 200:
                        continue
                    for i in range(0, 5):
                        c = i * 50
                        if e+g+h+f +d+ c > 200:
                            continue
                        for i in range(0, 3):
                            b = i * 100
                            if e+g+h+f +d+c+ b > 200:
                                continue
                            for i in range(0, 2):
                                a = i * 200
                                if e+g+h+f +d+c+ b+a>200:
                                    continue
                                elif a+b+c+d+e+f+g+h==200:
                                    sayac+=1




print(sayac)