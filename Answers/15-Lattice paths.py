#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

#diyelim ki 3x3lük bir karemiz var. burada yukarı ve sağa toplamda 3'er kare ilerleyebiliyoruz. o halde  6 tane çizgimiz olacak:
# _ _ _ _ _ _ > Y S S Y S Y gibi. E burada yleri ya da sleri nereye koyduğumuz önemli. Bunlar birbirlerinin aynısı oladuğundan ise kombinasyon yerine permutasyon kullanacağız.
#Yani 3'e 3'lük için 6'nın 3'lü permutasyonu. -> (6*5*4)/(3!)

def permutasyon(a, b):
    ust=1
    alt=1
    for i in range(a, b,-1):
        ust*=i
    for j in range(b, 0, -1):
        alt*=j
    return ust/alt
print(permutasyon(40,20))
