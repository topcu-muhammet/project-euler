# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# birler
# za=(984%10)//1
# onlar
# za=(984%100)//10
# yüzler
# za=(984%1000)//100
# binler
# za=(8984%10000)//1000
import time
start=time.time()
def polindrom_test(sayi):  # polindrom olup olmadığını kontrol eder.
    # True ya da False.
    uzunluk = len(str(sayi))
    for i in range((uzunluk) // 2):
        if str(sayi)[i] == str(sayi)[-i - 1]:
            continue
        else:
            return False
    return True


def two_three_digits():  # 3 basamaklı iki sayının çarpımı olarak bulmak
    palindrome_list = []
    for a in range(100, 1000):
        for b in range(100, 1000):
            canditate = a * b
            if polindrom_test(canditate):
                palindrome_list.append(a * b)
            else:
                continue
    palindrome_list.sort()
    return palindrome_list[-1]


print(two_three_digits())
end=time.time()
print(end-start)