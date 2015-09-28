__author__ = 'Shane'
from random import uniform

# Uses a Monte Carlo simulation to estimate the value of pi
# by throwing darts at a square centered at the origin

def estpi(n):
    count = 0
    for i in range(n):
        x = uniform(0, 1)
        y = uniform(0, 1)
        if x ** 2 + y ** 2 <= 1:
            count += 1
    return count * 4 / n


def main():
    trials = 0
    while trials <= 0:
        trials = int(input("How many trials? "))
        if trials <= 0:
            print("")
            print("Please enter a positive number!")
    print("")
    print("Estimated value of pi:", estpi(trials))

main()
