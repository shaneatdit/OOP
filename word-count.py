##########################################################################
#                                                                        #
# word-count.py                                                          #
#   by Shane                                                             #
#                                                                        #
# Prints the number of lines, words, and characters in a file            #
#                                                                        #
##########################################################################


def main():
    file = input("Enter filename: ")

    lines = 0
    words = 0
    chars = 0

    with open(file) as f:
        for line in f:
            # print(line)
            lines += 1
            line_words = line.split()
            words += len(line_words)
            chars += len(line)

    print(file, "contains", lines, "lines,", words, "words, and", chars, "characters.")

main()
