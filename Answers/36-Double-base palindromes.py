"""Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""

def polindrom_test(sayi):#polindrom olup olmadığını kontrol eder. True ya da False.
    uzunluk=len(str(sayi))
    if uzunluk%2==0:
        for i in range((uzunluk)//2):
            if str(sayi)[i]==str(sayi)[-i-1]:
                continue
            else:
                return False
        return True
    elif uzunluk%2==1:
        for i in range((uzunluk)//2):
            if str(sayi)[i]==str(sayi)[-i-1]:
                continue
            else:
                return False
        return True

toplam=0
for a in range(1,1000000):
    if polindrom_test(a):
        if polindrom_test(int(str(bin(a))[2:])):
            toplam+=a
print(toplam)