##########################################################################
#                                                                        #
# linenum.py                                                             #
#   by Shane                                                             #
#                                                                        #
# prints the contents of a file with line numbers along the left edge    #
#                                                                        #
##########################################################################


def main():
    f = input("Enter filename: ")
    file = open(f, "r")

    line_number = 0
    print("")

    for line in file:
        line_number += 1
        print(line_number, line, end='')

    file.close()

main()
