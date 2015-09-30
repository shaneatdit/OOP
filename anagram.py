##########################################################################
#                                                                        #
# anagram.py                                                             #
#   by Shane                                                             #
#                                                                        #
# Checks if two words are anagrams                                       #
#                                                                        #
##########################################################################


def alphalist(word):
    # Converts word to list of lower-case letters, in alphabetical order
    word = word.lower()
    chars = list(word)
    chars.sort()
    return chars


def anagram(a, b):
    # Checks if a and b are anagrams
    if alphalist(a) == alphalist(b):
        return True
    else:
        return False


def main():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    print()
    if word1.lower() == word2.lower():
        print(word1, "and", word2, "are the same")
    elif anagram(word1, word2):
        print(word1, "and", word2, "are anagrams")
    else:
        print(word1, "and", word2, "are not anagrams")

main()
