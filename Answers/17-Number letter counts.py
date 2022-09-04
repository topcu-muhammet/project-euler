#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
#(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
import re

sayilar={0:"",1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen",
17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 100:"one hundred", 1000:"one thousand"}


def yaziyla(sayi):
    yazi=""
    if sayi in sayilar:
        yazi=yazi + sayilar[sayi]
    elif sayi>20 and sayi%10!=0:
        if sayi>100:
            yazi=yazi+ sayilar[sayi//100]+" hundred" +"and"
        if ((sayi%100)//10)*10>19:
            yazi=yazi + sayilar[((sayi%100)//10)*10] + sayilar[sayi%10]
        if ((sayi%100)//10)*10<20:
            yazi=yazi + sayilar[(((sayi%100)//10)*10)+(sayi%10)]
    elif sayi%100==0 and sayi>100:
        yazi=yazi+ sayilar[sayi//100]+" hundred"
    elif sayi%10==0 and sayi>20:
        yazi=yazi + sayilar[sayi//100]+ " hundred" + "and" + sayilar[(sayi%100)]
    else:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    return yazi
b=""
for a in range(1,1001):
    b=b+yaziyla(a)
    b = re.sub(' ', '', b)
    b = re.sub("\n","", b)
print(len(b))
