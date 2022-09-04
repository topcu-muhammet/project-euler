#10'dan küçük 3'ün ya da 5'in katları olan sayıları sıralarsak
# 3, 5, 6 ve 9 sayılarını elde ederiz. Bu katların toplamları 23 eder.
#1000'den küçük 3'ün veya 5'in katları olan sayıların toplamını bulun.
sum=0
for number in range(1, 1000, 1):
    if number%3==0:
        sum+=number
    elif number%5==0:
        sum+=number
print(sum)
