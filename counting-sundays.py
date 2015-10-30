"""
Counts how many months started on a Sunday during the twentieth century (1 Jan 1901 to 31 Dec 2000).

A solution to the problem at https://projecteuler.net/problem=19
"""
COMMON_YEAR_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_YEAR_MONTHS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    """
    Returns True if year is a leap year; otherwise returns false.
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def main():
    total = 0
    day = 2      # 1 Jan 1901 was a Tuesday

    for year in range(1901, 2001):
        total_this_year = 0

        # Check if it's a leap year
        if isLeapYear(year):
            months = LEAP_YEAR_MONTHS
        else:
            months = COMMON_YEAR_MONTHS

        # Iterate through the twelve months, checking if each one started on a Sunday
        for month_length in months:
            day += month_length
            day %= 7
            if day == 0:
                total_this_year += 1

        # Print this year's result and add to total
        if total_this_year == 1:
            print("In ", year, ", 1 month started on a Sunday", sep="")
        else:
            print("In ", year, ", ", total_this_year, " months started on a Sunday", sep="")
        total += total_this_year

    # Print total
    print()
    print("Total:", total, "months started on a Sunday")

main()
