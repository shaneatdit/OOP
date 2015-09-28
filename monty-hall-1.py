####################################################################
#                                                                  #
# monty-hall-1.py                                                  #
# by Shane                                                         #
#                                                                  #
# A simple version of the Monty Hall Problem                       #
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
        reveal = 0
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
            if prize == 1:
                reveal = randint(2, 3)
            elif prize == 2:
                reveal = randint(1, 3)
            else:
                reveal = randint(1, 2)
            print("Monty has opened door number", reveal, "revealing a goat")

            change = get_change()
            if not change:
                    win = True
            else:
                    win = False

        # if player guesses incorrectly, Monty opens the other wrong door
        else:
            if guess == 1:
                if prize == 2:
                    reveal = 3
                else:
                    reveal = 2
            elif guess == 2:
                if prize == 1:
                    reveal = 3
                else:
                    reveal = 1
            elif guess == 3:
                if prize == 1:
                    reveal = 2
                else:
                    reveal = 1
            print("Monty has opened door number", reveal, "revealing a goat")
            win = get_change()

        # print result
        if win:
            print("You win!")
        else:
            print("You lose!")

        '''
        print()
        print("Guess:", guess)
        print("Car:", prize)
        '''

main()
