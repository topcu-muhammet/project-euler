with open(r"C:\Users\Muhammet TOPCU\Desktop\p067_triangle.txt", 'r', encoding="utf-8") as myfile:
    data=myfile.readlines()
liste=[]
for a in data:
    liste.append(a.rstrip().split(" "))
print(liste)
def path():
    for n in range(len(liste)-1, 0, -1):
        a=0
        while a in range(len(liste[n])-1):
            if int(liste[n][a])>=int(liste[n][a+1]):
                liste[n-1][a]=int(liste[n-1][a])+int(liste[n][a])
                a+=1
            elif int(liste[n][a])<int(liste[n][a+1]):
                liste[n-1][a]=int(liste[n-1][a])+int(liste[n][a+1])
                a+=1
    return liste[0][0]
print(path())
