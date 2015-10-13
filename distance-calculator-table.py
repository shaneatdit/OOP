"""
distance-calculator-table.py

Prints a table of distances between the airports in AIRPORT_LIST.
Uses the following formula to calculate distances:

  distance = EARTH_RADIUS * acos((sin(phi1) * sin(phi2) * cos(theta1 - theta2)) + cos(phi1) * cos(phi2))

where phi is the angle in radians from the North Pole to a coordinate,
and theta is the angle in radians from the Prime Meridian (east is positive, west is negative)
"""

from math import acos, cos, sin, pi

EARTH_RADIUS = 6371          # kilometers
NUMBER_OF_MILES_IN_A_KILOMETER = 0.621371

AIRPORT_LIST = [["JFK", 40.639751, -73.778925], ["AAL", 57.092789, 9.849164], ["CDG", 49.012779, 2.55],
                ["SYD", -33.946111, 151.177222], ["LHR", 51.4775, -0.461389], ["DUB", 53.421333, -6.270075]]


def distance_between(airport1, airport2):
    """
    Returns the distance between two airports.
    Args: Two airport codes from AIRPORT_LIST.
    Returns: The distance in kilometers between the two airports.
    """

    # Get coordinates of each airport from AIRPORT_LIST
    lat1 = airport1[1]
    long1 = airport1[2]
    lat2 = airport2[1]
    long2 = airport2[2]

    # Calculate angles phi and theta (in radians) for each airport
    phi1 = (90 - lat1) * 2 * pi / 360
    theta1 = long1 * 2 * pi / 360
    phi2 = (90 - lat2) * 2 * pi / 360
    theta2 = long2 * 2 * pi / 360

    # Calculate the distance, return
    return EARTH_RADIUS * acos((sin(phi1) * sin(phi2) * cos(theta1 - theta2)) + cos(phi1) * cos(phi2))


def print_distance_table():
    """
    Prints a table of distances between all airports in AIRPORT_LIST
    """

    # Print header
    print()
    print(" " * 22, "Distance between airports")
    print()
    print("          ", end="")
    for i in AIRPORT_LIST:
        print(i[0], end="       ")
    print()
    print("-" * 64)

    # Print row
    for row in range(len(AIRPORT_LIST)):
        airport1 = AIRPORT_LIST[row]
        print(airport1[0], end="     ")

        # Print cell
        for column in range(len(AIRPORT_LIST)):
            airport2 = AIRPORT_LIST[column]

            # Calculate distance
            distance_in_kilometers = distance_between(airport1, airport2)
            distance_in_miles = distance_in_kilometers * NUMBER_OF_MILES_IN_A_KILOMETER

            # Convert to strings (with commas)
            kilometers_string = str("{:,}".format(int(distance_in_kilometers)))
            miles_string = str("{:,}".format(int(distance_in_miles)))

            if row == column:
                # Print dash
                print("   - ", end="     ")

            elif row < column:
                # Print distance in kilometers (right-justified)
                print(kilometers_string.rjust(6), end="    ")

            elif row > column:
                # Print distance in miles (right-justified)
                print(miles_string.rjust(6), end="    ")

        if row == 2:
            print(" kilometers", end="")
        print()

    print()
    print(" " * 31, "miles")
    print()


def main():
    print_distance_table()


main()
