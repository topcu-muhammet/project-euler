#1000-digit Fibonacci number
#Problem 25
#The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:

#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
import time
start=time.time()
def bin_digit(sayi):
    prev=1
    num=1
    index=2
    new_num=0
    while len(str(new_num))<sayi:
        new_num=num+prev
        prev=num
        num=new_num
        index+=1
    return index
print(bin_digit(1000))
end=time.time()
print(end-start)