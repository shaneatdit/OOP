##########################################################################
#                                                                        #
# printfile4.py                                                          #
#   by Shane                                                             #
#                                                                        #
# Prints a file using a file for loop                                    #
# (prints double-spaced)                                                 #
#                                                                        #
##########################################################################


def main():
    file = input("Enter filename: ")
    # file = "c.txt"
    with open(file) as f:
        for line in f:
            print(line)

main()
