##########################################################################
#                                                                        #
# printfile3.py                                                          #
#   by Shane                                                             #
#                                                                        #
# Prints a file using the .readline() method                             #
# (prints double-spaced)                                                 #
#                                                                        #
##########################################################################


def main():
    file = input("Enter filename: ")
    # file = "c.txt"
    with open(file) as f:
        while True:
            line = f.readline()
            if line == "":
                break
            print(line)

main()
