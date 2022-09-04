# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


def largest_prime_factor(number):
    prime_factors = []
    for i in range(2, number + 1):
        if number % i == 0:
            prime_factors.append(i)
        while number % i == 0:
            number = number / i
        if number == 1:
            break
    return prime_factors[-1]


print(largest_prime_factor(600851475143))

