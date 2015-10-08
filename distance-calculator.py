"""
Calculates the distance between any two points on the surface of the earth,
given the coordinates (degrees latitude and longitude).
Also prints a table of distances between airports.
"""

from math import sin, cos, acos, pi

EARTH_RADIUS = 6371
COORDINATES = {"JFK": [40.639751, -73.778925], "AAL": [57.092789, 9.849164], "CDG": [49.012779, 2.55],
               "SYD": [-33.946111, 151.177222], "LHR": [51.4775, -0.461389], "DUB": [53.421333, -6.270075]}


def distance(airport1, airport2):
    """
    Returns the distance between two airports.

    Args: Two airport codes from the COORDINATES dictionary.

    Returns: The distance in kilometers between the two airports, as an integer.
    """
    lat1 = COORDINATES[airport1][0]
    long1 = COORDINATES[airport1][1]
    lat2 = COORDINATES[airport2][0]
    long2 = COORDINATES[airport2][1]

    phi1 = (90 - lat1) * 2 * pi / 360
    theta1 = long1 * 2 * pi / 360
    phi2 = (90 - lat2) * 2 * pi / 360
    theta2 = long2 * 2 * pi / 360

    return int(EARTH_RADIUS * acos((sin(phi1) * sin(phi2) * cos(theta1 - theta2)) + cos(phi1) * cos(phi2)))


def print_distance_table():
    """
    Prints a table of distances between airports.
    """

    # Print header
    print()
    print("             Distance between airports (to nearest km)")
    print("          ", end="")
    for i in COORDINATES:
        print(i, end="      ")
    print()
    print("----------------------------------------------------------")

    # Print each row
    for i in COORDINATES:
        print(i, end="     ")
        for j in COORDINATES:
            if i == j:
                print("   -", end="     ")
            else:
                distance_str = str(distance(i, j))
                print(distance_str.rjust(5), end="    ")
        print()


def main():
    print_distance_table()

main()
