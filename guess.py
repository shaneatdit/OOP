__author__ = 'Shane'
from random import randint
# user guesses a number


def guess(answer, spread):
    correct = False
    i = 0
    while not correct:
        guess = int(input("Guess a number: "))
        print("")
        i += 1
        if guess < 1 or guess > spread:
            print("Please guess a number between 1 and", spread)
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        elif guess == answer:
            print("Correct! You guessed correctly in", i, "attempts.")
            correct = True


def main():
    spread = int(input("Enter a maximum value: "))
    print("")
    answer = randint(1, spread)
    guess(answer, spread)

main()
