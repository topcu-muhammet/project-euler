import time
start=time.time()

def triplet():
    for c in range(334,1000):
        for b in range (1, c):
            for a in range(1, b+1):
                if (a+b+c)==1000 and (a**2)+(b**2)==(c**2):
                    return (a, b, c, a*b*c)
print(triplet())

end=time.time()
print(end-start)