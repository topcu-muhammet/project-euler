# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def which_prime(number):
    prime = [2]
    for a in range(2, 10000000000000000000):
        for b in prime:
            if a % b == 0:
                break
            if a % b != 0 and b == prime[-1]:
                prime.append(a)
                break
        if len(prime) == number:
            break
    return prime[-1]


print(which_prime(10001))
