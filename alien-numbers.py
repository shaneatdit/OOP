"""
Converts a number from any numeral system into any other.

A solution to the Google Code Jam 'Alien Numbers' contest:
https://code.google.com/codejam/contest/dashboard?c=32003
"""

INPUT = "A-large-practice.txt"
OUTPUT = "A-large-practice-output.txt"


def read_file(file):
    with open(file) as f:
        return f.readlines()


def convert_alien_to_decimal(alien_number, source_language):
    """
    Converts a number from any other numeral system into a decimal integer.

    Args: alien_number (string): the number to be converted to decimal;
          source_language (string): the set of digits used in the alien numeral system
          (e.g., for decimal this would be "0123456789",
          for hexadecimal it would be "0123456789ABCDEF").

    Returns: a decimal integer.
    """
    alien_base = len(source_language)
    decimal = 0
    place = 1
    while alien_number != "":
        current_digit = alien_number[-1]
        for i in range(alien_base):
            if current_digit == source_language[i]:
                decimal += i * place
        place *= alien_base
        alien_number = alien_number[:-1]
    return decimal


def convert_decimal_to_alien(decimal_number, target_language):
    """
    Converts a decimal integer into any other numeral system.

    Args: decimal_number (integer): the number to be converted;
          target_language (string): the set of digits used in the alien numeral system
          (e.g., for decimal this would be "0123456789",
          for hexadecimal it would be "0123456789ABCDEF").

    Returns: a string representing the number in the alien numeral system.
    """
    alien_base = len(target_language)
    alien_number = ""
    while decimal_number > 0:
        current_digit = decimal_number % alien_base
        alien_digit = target_language[current_digit]
        alien_number = alien_digit + alien_number
        decimal_number -= current_digit
        decimal_number //= alien_base
    return alien_number


def main():
    problem_set = read_file(INPUT)
    number_of_cases = int(problem_set[0])
    destination = open(OUTPUT, "w")

    for i in range(number_of_cases):
        line = problem_set[i + 1].strip().split()

        input_number = line[0]
        source_language = line[1]
        target_language = line[2]

        converted_number = convert_decimal_to_alien(convert_alien_to_decimal(input_number, source_language), target_language)

        # Write answer to file
        output = "Case #" + str(i + 1) + ": " + converted_number + "\n"
        destination.write(output)

    destination.close()

main()
