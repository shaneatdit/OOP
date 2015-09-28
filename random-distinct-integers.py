from random import randint
# prints n distinct pseudorandom integers in a given range


def randdistinctints(n, a, b):
    output = []
    for i in range(n):
        while True:
            new = randint(a, b)
            if new not in output:
                output.append(new)
                break
    return output


def main():
    # Prompt user for three positive integers
    num = 0
    while num <= 0:
        num = int(input("How many numbers would you like? "))
        if num <= 0:
            print("")
            print("Please enter a positive number!")
    mini = 0
    while mini <= 0:
        mini = int(input("Lower bound: "))
        if mini <= 0:
            print("")
            print("Please enter a positive number!")
    maxi = 0
    while maxi <= mini + num - 2:
        maxi = int(input("Upper bound: "))
        if maxi <= 0:
            print("")
            print("Please enter a positive number!")
        elif maxi <= mini + num - 2:
            print("")
            print("If you want", num, "numbers, the upper bound must be at least", mini + num - 1)

    print("")
    print(randdistinctints(num, mini, maxi))

main()
