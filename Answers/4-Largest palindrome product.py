# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(number):
    """
    Checks if a number is palindrome or not?
    @param number: Number to be checked
    @return: Boolean
    """
    for i in range(len(str(number)) // 2):
        if str(number)[i] == str(number)[-i - 1]:
            continue
        else:
            return False
    return True


def two_three_digits():
    """
    Find palindromes as a product of two three digits numbers.
    @return: List
    """
    palindrome_list = []
    for a in range(100, 1000):
        for b in range(100, 1000):
            candidate = a * b
            if is_palindrome(candidate):
                palindrome_list.append(a * b)
            else:
                continue
    palindrome_list.sort()
    return palindrome_list


print(two_three_digits()[-1])
