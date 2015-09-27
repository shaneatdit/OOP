__author__ = 'Shane'
# converts a message into a string containing the ASCII codes of each character of the message


def encode(string):
    output = ""
    for i in range(len(string)):
        output += str(ord(string[i]))
        if i < len(string) - 1:
            output += " "
    return output


def main():
    a = input("Enter a string: ")
    print("")
    print(encode(a))


main()
