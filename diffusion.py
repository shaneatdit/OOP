##########################################################################
#                                                                        #
# diffusion.py                                                           #
#   by Shane                                                             #
#                                                                        #
# Simulates the diffusion of heat through an insulated metal rod         #
# with a heat source at each end                                         #
#                                                                        #
##########################################################################


def init(left, right, inittemp, n):
    l = [left]
    for i in range(1, n - 1):
        l.append(inittemp)
    l.append(right)
    return l


def main():

    # Prompt for length of rod
    length = 0
    while length <= 0:
        length = float(input("How long is the rod? "))
        if length <= 0:
            print("")
            print("Please enter a positive number!")

    # Prompt for number of segments
    segments = 0
    while segments <= 4:
        segments = int(input("How many segments? "))
        if segments <= 4:
            print("")
            print("There should be at least five segments")

    # Prompt for initial temperature of left end
    left = float(input("Temperature of first end: "))

    # Prompt for initial temperature of right end
    right = float(input("Temperature of other end: "))

    # Prompt for initial temperature of middle
    inittemp = float(input("Temperature of middle of rod: "))

    # Prompt for duration of simulation
    duration = 0
    while duration <= 0:
        duration = float(input("How long would you like to run the simulation for? (seconds) "))
        if duration <= 0:
            print("")
            print("Please enter a positive number!")

    # Calculate length of each segment
    h = int(length / segments)

    # Calculate length of each time period
    dt = h ** 2 / 2
    # if dt is very small, output is too large
    if dt < 0.1:
        dt = 0.1

    time_elapsed = 0.0

    # Initiate rod
    start = init(left, right, inittemp, segments)
    print()
    print(time_elapsed, start)

    # Run simulation
    while time_elapsed < duration:
        time_elapsed += dt
        new = [left]
        for i in range(segments - 2):
            new.append((start[i] + start[i + 2]) / 2)
        new.append(right)
        print(time_elapsed, new)
        start = new

main()
