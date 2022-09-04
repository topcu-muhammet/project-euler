"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""

pay = 1
payda = 1
for b in range(11, 100):
    for a in range(10, b):
        if str(a)[0] == str(b)[0] and int(str(b)[1]) != 0:
            if int(str(a)[1]) / int(str(b)[1]) == a / b:
                pay *= int(str(a)[1])
                payda *= int(str(b)[1])
        if str(a)[0] == str(b)[1] and int(str(b)[0]) != 0:
            if int(str(a)[1]) / int(str(b)[0]) == a / b:
                pay *= int(str(a)[1])
                payda *= int(str(b)[0])
        if str(a)[1] == str(b)[0] and int(str(b)[1]) != 0:
            if int(str(a)[0]) / int(str(b)[1]) == a / b:
                pay *= int(str(a)[0])
                payda *= int(str(b)[1])
        if str(a)[1] == str(b)[1] and int(str(b)[0]) != 0 and int(str(b)[1]) != 0:
            if int(str(a)[0]) / int(str(b)[0]) == a / b:
                pay *= int(str(a)[0])
                payda *= int(str(b)[0])
for a in range(1, pay):
    if pay % a == 0 and payda % a == 0:
        pay /= a
        payda /= a
print(payda)
