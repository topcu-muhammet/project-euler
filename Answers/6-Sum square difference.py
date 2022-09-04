# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_of_squares(number):
    sum2 = 0
    sum1 = 0
    for i in range(number + 1):
        sum1 += i * i
    for i in range(number + 1):
        sum2 += i
    sum2 = sum2 * sum2
    return sum2 - sum1


print(sum_of_squares(100))
