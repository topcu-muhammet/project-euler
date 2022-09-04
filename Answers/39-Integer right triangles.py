import time
start= time.time()

def triplet(p):
    sum=0
    liste=[]
    for c in range((p//3)+1,p):
        for b in range ((p-c)//2, p-c):
            a=p-(c+b)
            if (a**2)+(b**2)==(c**2):
                sum+=1
    return sum

toplam=0
perimeter=0
for p in range(10,1000):
    if triplet(p)>toplam:
        toplam=triplet(p)
        perimeter=p
print(perimeter, toplam)
end=time.time()
print(start-end)