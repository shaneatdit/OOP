"""
Calculates the largest palindrome that is a product of two three-digit numbers.

A solution to this problem:
https://projecteuler.net/problem=4
"""


def isPalindrome(number):
    """Returns True if number is a palindrome, otherwise returns False."""
    string = str(number)
    reverse = string[::-1]
    if string == reverse:
        return True
    else:
        return False


def main():
    largest_palindrome = [0, 0, 0]
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if product > largest_palindrome[2]:
                if isPalindrome(product):
                    largest_palindrome[0] = i
                    largest_palindrome[1] = j
                    largest_palindrome[2] = product
    print(largest_palindrome[0], "x", largest_palindrome[1], "=", largest_palindrome[2])

main()
