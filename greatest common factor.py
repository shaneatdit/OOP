__author__ = 'Shane'
# Finds the greatest common factor of two positive integers


def gcd(m, n):
    if n == 0:
        return m
    else:
        temp = m
        m = n
        n = temp % n
        return gcd(m, n)


def main():
    a = 0
    while a <= 0:
        a = int(input("First number: "))
        if a <= 0:
            print("")
            print("Please enter a positive number!")
    b = 0
    while b <= 0:
        b = int(input("Second number: "))
        if b <= 0:
            print("")
            print("Please enter a positive number!")
    print("The greatest common denominator of", a, "and", b, "is", gcd(a, b))

main()
