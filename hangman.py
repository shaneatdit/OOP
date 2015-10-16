##########################################################################
#                                                                        #
# hangman.py                                                             #
#   by Shane                                                             #
#                                                                        #
# The classic game                                                       #
#                                                                        #
##########################################################################
from random import randint

DICTIONARY = "dictionary.txt"
LIVES = 6
GALLOWS = {6: [" _________     ", "|         |    ", "|              ", "|             ",
                "|             ", "|              ", "|              ", "|_________     "],
            5: [" _________     ", "|         |    ", "|         0    ", "|             ",
                "|             ", "|              ", "|              ", "|_________     "],
            4: [" _________     ", "|         |    ", "|         0    ", "|         |   ",
                "|             ", "|              ", "|              ", "|_________     "],
            3: [" _________     ", "|         |    ", "|         0    ", "|        /|   ",
                "|             ", "|              ", "|              ", "|_________     "],
            2: [" _________     ", "|         |    ", "|         0    ", "|        /|\\  ",
                "|             ", "|              ", "|              ", "|_________     "],
            1: [" _________     ", "|         |    ", "|         0    ", "|        /|\\  ",
                "|        /    ", "|              ", "|              ", "|_________     "],
            0: [" _________     ", "|         |    ", "|         0    ", "|        /|\\  ",
                "|        / \\  ", "|              ", "|              ", "|_________     "]}


def wordlist(file):
    """Returns a list of all the words in a file."""
    with open(file) as f:
        return f.read().split()


def select_random_word(word_list):
    """Returns a random word from a list."""
    while True:
        rand = randint(0, len(word_list) - 1)
        if word_list[rand].isalpha():
            return word_list[rand]


def print_gallows(lives):
    gallows = GALLOWS[lives]
    for i in gallows:
        print(i)
    print()


def game_board(word, correct):
    """Returns the hangman game board."""
    output = ""
    for i in range(len(word)):
        if word[i] in correct:
            output += word[i]
        else:
            output += "-"
    return output


def hangman():
    """Plays the game."""
    guess_count = 1
    lives = LIVES
    guessed = []
    incorrect = []
    correct = []
    print()
    print()
    print("H * A * N * G * M * A * N")

    # Randomly select a word from the dictionary and generate game board
    answer = select_random_word(wordlist(DICTIONARY))
    board = game_board(answer, correct)

    # Loop game until player wins or loses
    while True:

        # print game board and current status
        print()
        print_gallows(lives)
        print(board)
        print()
        print("Incorrect guesses: ", end="")
        print(", ".join(incorrect))
        print("Lives remaining:", lives)
        print()

        # Prompt player for a valid guess
        while True:
            guess = input("Guess a letter: ").lower()
            if guess not in guessed and guess.isalpha() and len(guess) == 1:
                break
            elif guess in guessed:
                print()
                print("You already guessed", guess)
            else:
                print()
                print("Please guess a letter")
        guess_count += 1
        found = False
        guessed.append(guess)
        print()
        print()
        print()

        # If guess is correct, add to correct list
        for i in range(len(answer)):
            if guess == answer[i]:
                correct.append(guess)
                found = True

        # If guess is incorrect, add to incorrect list and lose a life
        if found is False:
            print()
            print("Wrong!")
            print()
            print()
            incorrect.append(guess)
            incorrect.sort()
            lives -= 1

            # If player has run out of lives
            if lives < 1:
                print()
                print(board)
                print()
                print("You lose!")
                print("The answer is:", answer)
                print("You guessed: ", end="")
                print(", ".join(incorrect))
                print()
                return

        # Recalculate game board
        board = game_board(answer, correct)

        # If all letters have been revealed, player wins
        if board.isalpha():
            print()
            print(answer)
            print()
            print("You win!")
            print("You got it in", guess_count, "guesses")
            print()
            break


def main():
    hangman()

    # Asks if user would like to play again
    print()
    while True:
        play = input("Would you like to play again? (Y/N) ").lower()
        if play == "y":
            hangman()
        elif play == "n":
            print()
            print("Goodbye")
            return

main()
