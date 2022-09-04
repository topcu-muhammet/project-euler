veri=open("Largest product in a grid.txt", "r")
liste=[]
a;
for a in range(1,20):
    b=veri.readline()
    c=b.replace("\n", "")
    c=c.split(" ")
    liste.append(c)
print(liste)
sum=0
for a in range(20):
     for b in range(20):
        try:
            toplam=int(liste[a][b])*int(liste[a][b+1])*int(liste[a][b+2])*int(liste[a][b+3])
            if toplam>sum:
                sum=toplam
                x=a
                y=b
            toplam=0
        except IndexError:
            continue

for a in range(20):
     for b in range(20):
        try:
            toplam=int(liste[a][b])*int(liste[a+1][b])*int(liste[a+2][b])*int(liste[a+3][b])
            if toplam>sum:
                sum=toplam
            toplam=0
        except IndexError:
            continue

for a in range(20,0, -1):
     for b in range(20):
        try:
            toplam=int(liste[a][b])*int(liste[a-1][b+1])*int(liste[a-2][b+2])*int(liste[a-3][b+3])
            if toplam>sum:
                sum=toplam
            toplam=0
        except IndexError:
            continue

for a in range(20):
     for b in range(20):
        try:
            toplam=int(liste[a][b])*int(liste[a+1][b+1])*int(liste[a+2][b+2])*int(liste[a+3][b+3])
            if toplam>sum:
                sum=toplam
            toplam=0
        except IndexError:
            continue

print(sum)