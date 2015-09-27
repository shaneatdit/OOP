__author__ = 'Shane'
from random import randint
# flips a bunch of coins


def coinflip(n):
    count = 0
    for i in range(n):
        if randint(0, 1) == 0:
            count += 1
    return count


def main():
    a = int(input("How many coins would you like to flip? "))
    b = coinflip(a)
    c = 100 * (b / a)
    print(b, "heads (", c, "%)")

main()
