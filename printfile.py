"""
Four different ways to print a file.
"""


def printfile1(file):
    """
    Prints file using the .read() method.
    (Prints single-spaced.)
    """
    with open(file) as f:
        print(f.read())


def printfile2(file):
    """
    Prints file using the .readlines() method.
    (Prints double-spaced.)
    """
    with open(file) as f:
        for line in f.readlines():
            print(line)


def printfile3(file):
    """
    Prints file using the .readline() method.
    (Prints double-spaced.)
    """
    with open(file) as f:
        while True:
            line = f.readline()
            if line == "":
                break
            print(line)


def printfile4(file):
    """
    Prints file using a file for loop
    (Prints double-spaced.)
    """
    with open(file) as f:
        for line in f:
            print(line)


def main():
    file = input("Enter filename: ")
    printfile4(file)

main()
