"""
Checks if a number is prime.
"""


def isprime(number):
    """Returns True is number if prime, otherwise returns False."""
    if number < 1:
        return False
    a = 2
    while a <= number ** 0.5:
        if number % a == 0:
            return False
        a += 1
    return True


def main():
    # Prompt user to enter an integer
    while True:
        string = input("Enter an integer: ")
        try:
            int(string)
            n = int(string)
            break
        except ValueError:
            print()
            print(string, "is not an integer")

    if isprime(n):
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

main()
