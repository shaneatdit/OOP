##########################################################################
#                                                                        #
# printfile2.py                                                          #
#   by Shane                                                             #
#                                                                        #
# Prints a file using the .readlines() method                            #
# (prints double-spaced)                                                 #
#                                                                        #
##########################################################################


def main():
    file = input("Enter filename: ")
    # file = "c.txt"
    with open(file) as f:
        for line in f.readlines():
            print(line)

main()
