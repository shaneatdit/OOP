"""
distance-calculator-using-dictionary.py

Prompts user to input two three-letter airport codes and then calculates
the distance between those two airports, using the following formula:

  distance = EARTH_RADIUS * acos((sin(phi1) * sin(phi2) * cos(theta1 - theta2)) + cos(phi1) * cos(phi2))

where phi is the angle in radians from the North Pole to a coordinate,
and theta is the angle in radians from the Prime Meridian (east is positive, west is negative)

(Note: only works for airport codes in the COORDINATES dictionary.)
"""

from math import acos, cos, sin, pi

EARTH_RADIUS = 6371          # kilometers
NUMBER_OF_MILES_IN_A_KILOMETER = 0.621371

COORDINATES = {"JFK": [40.639751, -73.778925], "AAL": [57.092789, 9.849164], "CDG": [49.012779, 2.55],
               "SYD": [-33.946111, 151.177222], "LHR": [51.4775, -0.461389], "DUB": [53.421333, -6.270075]}


def distance_between(airport1, airport2):
    """
    Returns the distance between two airports.
    Args: Two airport codes from the COORDINATES dictionary.
    Returns: The distance in kilometers between the two airports.
    """

    # Get coordinates of each airport from COORDINATES dictionary
    lat1 = COORDINATES[airport1][0]
    long1 = COORDINATES[airport1][1]
    lat2 = COORDINATES[airport2][0]
    long2 = COORDINATES[airport2][1]

    # Calculate angles phi and theta (in radians) for each airport
    phi1 = (90 - lat1) * 2 * pi / 360
    theta1 = long1 * 2 * pi / 360
    phi2 = (90 - lat2) * 2 * pi / 360
    theta2 = long2 * 2 * pi / 360

    # Calculate the distance (in both km and miles)
    return EARTH_RADIUS * acos((sin(phi1) * sin(phi2) * cos(theta1 - theta2)) + cos(phi1) * cos(phi2))


def main():
    print()

    # Prompt user for first airport code
    airport1 = "A"
    while True:
        airport1 = input('Please enter the first airport code (e.g. "DUB"): ').upper()
        if airport1 in COORDINATES:
            break
        else:
            print("That's not a valid airport code.")
            print()

    # Prompt user for second airport code
    airport2 = "A"
    while True:
        airport2 = input('Please enter the second airport code (e.g. "LHR"): ').upper()
        if airport2 in COORDINATES:
            break
        else:
            print("That's not a valid airport code.")
            print()

    # Calculate distance between the two airports
    distance_in_kilometers = distance_between(airport1, airport2)
    distance_in_miles = distance_in_kilometers * NUMBER_OF_MILES_IN_A_KILOMETER

    # Print answer
    print()
    print("The distance between", airport1, "and", airport2, "is ", end="")
    print("{:,}".format(int(distance_in_kilometers)), "kilometers (", end="")
    print("{:,}".format(int(distance_in_miles)), "miles).")

main()
