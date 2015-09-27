from random import randint
import time
# rolls n dice, reports results


def roll(n):
    tally = [0, 0, 0, 0, 0, 0]
    for i in range(n):
        r = randint(0, 5)
        tally[r] += 1
    return tally


def main():
    n = 0
    while n <= 0:
        n = int(input("How many dice would you like to roll? "))
        if n <= 0:
            print("")
            print("Please enter a positive number!")

    start = time.clock()
    result = roll(n)

    print("")
    for i in range(6):
        print("You rolled a", i + 1, "", result[i], "times (", '%.2f' % (100 * result[i] / n), "%)")

    print("")
    stop = time.clock()
    print("Time taken:", stop - start, "seconds")

main()
