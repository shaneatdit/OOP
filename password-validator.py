"""
Checks if a string is a valid password.

Prompts user to input a string, then informs user if password is valid.
A valid password:
    * has between 6 and 12 characters,
    * contains at least one upper-case letter,
    * contains at least one lower-case letter,
    * contains at least one digit, and
    * contains at least one of the following characters: $#@
"""


def is_valid_password(string):
    if len(string) < 6 or len(string) > 12:
        return False
    has_number = False
    has_lower_case = False
    has_upper_case = False
    has_punctuation = False
    for i in string:
        if i.islower():
            has_lower_case = True
        elif i.isupper():
            has_upper_case = True
        elif i.isdigit():
            has_number = True
        elif i in "$#@":
            has_punctuation = True
    if has_number and has_punctuation and has_upper_case and has_lower_case:
        return True
    else:
        return False


def main():
    password = input("Please enter password: ")
    if is_valid_password(password):
        print("That's a valid password")
    else:
        print("I'm sorry, that's not a valid password")

main()
