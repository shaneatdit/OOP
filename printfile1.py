##########################################################################
#                                                                        #
# printfile1.py                                                          #
#   by Shane                                                             #
#                                                                        #
# Prints a file using the .read() method                                 #
# (prints single-spaced)                                                 #
#                                                                        #
##########################################################################


def main():
    file = input("Enter filename: ")
    # file = "c.txt"
    with open(file) as f:
        print(f.read())

main()


'''
Alternatively:

def read(file):
    with open(file) as f:
        return f.read()


def main():
    # file = input("Enter filename: ")
    file = "c.txt"
    print(read(file))
'''
