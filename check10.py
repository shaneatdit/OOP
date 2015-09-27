__author__ = 'Shane'
# returns the check digit of a 9-digit ISBN string


def check10(s):
    total = 0
    for i in range(len(s)):
        n = int(s[i])
        total += n * (i + 1)
        check = total % 11
        if check == 10:
            check = "X"
    return check


def main():
    a = ""
    while len(a) != 9:
        a = input("Enter ISBN: ")
    print(a, check10(a))

main()
