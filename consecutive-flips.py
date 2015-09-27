__author__ = 'Shane'
from random import randint


# keeps flipping coins until it gets a streak of n
def consecflip(n):
    count = 0
    run = 0
    r = 2
    while run < n:
        count += 1
        current = randint(0, 1)
        if current == r:
            run += 1
        else:
            run = 1
            r = current
    return count


def main():
    a = 0
    while a <= 0:
        a = int(input("How many coins would you like in a row? "))
        if a <= 0:
            print("")
            print("Please enter a positive number!")
    print("")
    print("It took", consecflip(a), "flips to get a streak of", a)

main()
