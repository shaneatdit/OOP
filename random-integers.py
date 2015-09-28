from random import randint
# prints n pseudorandom integers in a given range


def randints(n, a, b):
    l = []
    for i in range(n):
        l.append(randint(a, b))
    return l


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
    while maxi <= mini:
        maxi = int(input("Upper bound: "))
        if maxi <= mini:
            print("")
            print("Please enter a number greater than", mini)

    print("")
    print(randints(num, mini, maxi))

main()
