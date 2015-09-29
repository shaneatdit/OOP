##########################################################################
#                                                                        #
# letter-value.py                                                        #
#   by Shane                                                             #
#                                                                        #
# Finds the word in a file with the highest total "letter value"         #
# (where A = a = 1, B = b = 2, C = c = 3, etc.)                          #
#                                                                        #
##########################################################################


def letter_value(letter):
    # Returns the letter value of a letter
    if 65 <= ord(letter) <= 90:
        return ord(letter) - 64
    elif 97 <= ord(letter) <= 122:
        return ord(letter) - 96
    else:
        return 0


def word_value(word):
    # Returns the letter value of a word
    total = 0
    for i in range(len(word)):
        total += letter_value(word[i])
    return total


def wordlist(file):
    # Splits a file into a list of words
    with open(file) as f:
        return f.read().split()


def find_max_word(file):
    # Returns the word(s) in a file with the greatest letter value
    max_length = 0
    max_word = [""]
    for word in wordlist(file):
        if word_value(word) > max_length:
            max_word = [word]
            max_length = word_value(word)
        elif word_value(word) == max_length:
            max_word.append(word)
    return max_word


def main():
    file = input("Enter filename: ")
    # file = "c.txt"
    print()
    print(find_max_word(file))

main()
