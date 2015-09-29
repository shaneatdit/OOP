##########################################################################
#                                                                        #
# wotd.py                                                                #
#   by Shane                                                             #
#                                                                        #
# Prints a random word of the day from a dictionary                      #
#                                                                        #
##########################################################################
from random import randint


# Creates a list of words from file
def wordlist(file):
    with open(file) as f:
        return f.read().split()


# Delects a word at random from dictionary
def main():
    word_list = wordlist("dictionary.txt")
    todays_word = randint(0, len(word_list) - 1)
    print("Today's word is:", word_list[todays_word])

main()
