##########################################################################
#                                                                        #
# monty-hall-simulation.py                                               #
# by Shane                                                               #
#                                                                        #
# Runs Monty Hall simulation repeatedly, either switching doors or not   #
#                                                                        #
##########################################################################

from random import randint


def get_change():
    # asks user if they'd like to switch doors every time
    # returns True or False
    while True:
        i = input("Do you wish to switch doors every time? (y/n) ")
        print()
        if i == "y" or i == "Y":
            return True
        elif i == "n" or i == "N":
            return False
        else:
            print("Please enter 'y' or 'n'!")


def monty_hall(guess, prize, change):

    # if player guesses correctly
    if guess == prize:
        flip = randint(0, 1)

        if guess == 1:
            if flip == 0:
                # print("Monty opened door number 2, revealing a goat")
                if change:
                    guess = 3
            else:
                # print("Monty opened door number 3, revealing a goat")
                if change:
                    guess = 2

        elif guess == 2:
            if flip == 0:
                # print("Monty opened door number 1, revealing a goat")
                if change:
                    guess = 3
            else:
                # print("Monty opened door number 3, revealing a goat")
                if change:
                    guess = 1

        elif guess == 3:
            if flip == 0:
                # print("Monty opened door number 1, revealing a goat")
                if change:
                    guess = 2
            else:
                # print("Monty opened door number 2, revealing a goat")
                if change:
                    guess = 1

    # if player guesses incorrectly
    else:
        if guess == 1:
            if prize == 2:
                # print("Monty opened door number 3, revealing a goat")
                if change:
                    guess = 2
            elif prize == 3:
                # print("Monty opened door number 2, revealing a goat")
                if change:
                    guess = 3

        elif guess == 2:
            if prize == 1:
                # print("Monty opened door number 3, revealing a goat")
                if change:
                    guess = 1
            elif prize == 3:
                # print("Monty opened door number 1, revealing a goat")
                if change:
                    guess = 3

        elif guess == 3:
            if prize == 1:
                # print("Monty opened door number 2, revealing a goat")
                if change:
                    guess = 1
            elif prize == 2:
                # print("Monty opened door number 1, revealing a goat")
                if change:
                    guess = 2

    '''
    print("Final guess:", guess)
    print("Car:", prize)
    print("Switch:", change)
    '''

    if guess == prize:
        return True
    else:
        return False


def main():

    # Ask how many times to run simulation
    print()
    while True:
        n = int(input("How many times would you like to play? "))
        if n > 0:
            break
        print("Please enter a positive number")

    # Run simulation n times
    change = get_change()
    wins = 0
    for i in range(n):
        prize = randint(1, 3)
        guess = randint(1, 3)
        if monty_hall(guess, prize, change):
            wins += 1

    # Print result
    print("You won", wins, "times out of", n, "games (", 100 * wins / n, "%)")

main()
