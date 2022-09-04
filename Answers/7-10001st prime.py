#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import time
start=time.time()
prime=[2]

def kacinci_prime(sayi):
    for a in range(2,56161846123184318543):
        for b in prime:
            if a%b==0:
                break
            if a%b!=0 and b==prime[-1]:
                prime.append(a)
                break
        if len(prime)==sayi:
            return(prime[-1])
            break
print(kacinci_prime(10001))
end=time.time()
print(end-start)