####################################################################
#                                                                  #
# monty-hall-2.py                                                  #
# by Shane                                                         #
#                                                                  #
# Another simple version of the Monty Hall Problem                 #
# (gives the same result as monty-hall-1.py)                       #
#                                                                  #
####################################################################

from random import randint


def get_change():
    # asks user if they'd like to switch doors
    # returns True or False
    while True:
        i = input("Do you wish to switch doors? (y/n) ")
        print()
        if i == "y" or i == "Y":
            return True
        elif i == "n" or i == "N":
            return False
        else:
            print("Please enter 'y' or 'n'!")


def main():
    prize = randint(1, 3)
    print()

    # prompt player to choose a door
    while True:
        guess = input("Choose a door (1, 2 or 3): ")
        print()
        if guess in ["1", "2", "3"]:
            guess = int(guess)
            break
        print("I told you to choose 1, 2 or 3, idiot!")

    # if player guesses correctly, Monty randomly opens another door, revealing a goat
    if guess == prize:
        flip = randint(0, 1)

        if guess == 1:
            if flip == 0:
                print("Monty has opened door number 2, revealing a goat")
                change = get_change()
                if change:
                    guess = 3
            else:
                print("Monty has opened door number 3, revealing a goat")
                change = get_change()
                if change:
                    guess = 2

        elif guess == 2:
            if flip == 0:
                print("Monty has opened door number 1, revealing a goat")
                change = get_change()
                if change:
                    guess = 3
            else:
                print("Monty has opened door number 3, revealing a goat")
                change = get_change()
                if change:
                    guess = 1

        elif guess == 3:
            if flip == 0:
                print("Monty has opened door number 1, revealing a goat")
                change = get_change()
                if change:
                    guess = 2
            else:
                print("Monty has opened door number 2, revealing a goat")
                change = get_change()
                if change:
                    guess = 1

    # if player guesses incorrectly
    else:
        if guess == 1:
            if prize == 2:
                print("Monty has opened door number 3, revealing a goat")
                change = get_change()
                if change:
                    guess = 2
            elif prize == 3:
                print("Monty has opened door number 2, revealing a goat")
                change = get_change()
                if change:
                    guess = 3

        elif guess == 2:
            if prize == 1:
                print("Monty has opened door number 3, revealing a goat")
                change = get_change()
                if change:
                    guess = 1
            elif prize == 3:
                print("Monty has opened door number 1, revealing a goat")
                change = get_change()
                if change:
                    guess = 3

        elif guess == 3:
            if prize == 1:
                print("Monty has opened door number 2, revealing a goat")
                change = get_change()
                if change:
                    guess = 1
            elif prize == 2:
                print("Monty has opened door number 1, revealing a goat")
                change = get_change()
                if change:
                    guess = 2

    # print result
    if guess == prize:
        print("You win!")
    else:
        print("You lose!")

    '''
    print("Guess:", guess)
    print("Car:", prize)
    print("Switch:", change)
    '''

main()
