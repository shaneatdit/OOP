__author__ = 'Shane'
# user thinks of a number, computer guesses the number


def find(mini, maxi, n):
    n += 1
    current_guess = (mini + maxi) // 2
    print("")
    print("Guess ", n, ":", current_guess)
    ans = input("Enter 'y' if correct, 'l' for lower, or 'h' for higher: ")

    if ans == "h" or ans == "H":
        find(current_guess + 1, maxi, n)

    elif ans == "l" or ans == "L":
        find(mini, current_guess - 1, n)

    elif ans == "y" or ans == "Y":
        print("")
        print("Woohoo!")
        print("Got it in", n, "guesses.")

    else:
        n -= 1
        print("That doesn't make sense")
        find(mini, maxi, n)


def main():
    lower = int(input("Enter minimum value: "))
    higher = int(input("Enter maximum value: "))
    find(lower, higher, 0)

main()
