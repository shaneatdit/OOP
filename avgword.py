##########################################################################
#                                                                        #
# avgword.py                                                             #
#   by Shane                                                             #
#                                                                        #
# Calculates the average length of all the words in a file               #
#                                                                        #
##########################################################################


def main():
    file = input("Enter filename: ")
    f = open(file, "r")
    words = f.read().split()

    wordcount = 0
    charcount = 0

    for word in words:
        wordcount += 1
        charcount += len(word)

    average = charcount / wordcount
    print("")
    print("Average word length in", file, ":", "%.2f" % average, "characters")

main()
