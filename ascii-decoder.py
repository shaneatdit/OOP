__author__ = 'Shane'
# decodes message from asciiencode.py


def decode(original):
    output = ""
    char_list = original.split()
    length = len(char_list)
    for i in range(length):
        output += chr(int(char_list[i]))
    return output


def main():
    a = input("Enter message to be decoded: ")
    # a = "72 101 108 108 111 44 32 119 111 114 108 100 33"
    print("")
    print(decode(a))


main()
