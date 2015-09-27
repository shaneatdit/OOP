__author__ = 'Shane'
# Finds the lowest common multiple of two positive integers


def lcm(m, n):
    i = m
    while i <= m * n:
        if (i % m == 0) and (i % n == 0):
            return i
        i += 1


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
    print("The lowest common multiple is", lcm(a, b))

main()
