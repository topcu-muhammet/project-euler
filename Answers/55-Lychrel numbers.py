"""If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is
Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i)
become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists,
has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty
iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers."""

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

def reverse(sayi): #sayiyi tersine çevirir.
    return int(str(sayi)[::-1])

lych_count=0
for a in range(1,10000):
    count=0
    while count<50:
        a=a+reverse(a)
        if polindrom_test(a):
            break
        count+=1
    if count==50:
        lych_count+=1
print(lych_count)
end=time.time()
print(end-start)