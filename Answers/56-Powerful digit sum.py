"""A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large:
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?"""
import time

start=time.time()

def pow_digit():
    digit_sum=0
    for a in range(90,100):
        for b in range(90,100):
            sayi=a**b
            sum=0
            for c in str(sayi):
                sum+=int(c)
            if sum>digit_sum:
                digit_sum=sum
    print(digit_sum)
pow_digit()
end=time.time()
print(end-start)