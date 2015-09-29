##########################################################################
#                                                                        #
# alpha-only.py                                                          #
#   by Shane                                                             #
#                                                                        #
# Prints only the alphabetic characters in a phrase                      #
#                                                                        #
##########################################################################


def alpha_only(phrase):
    # Returns a copy of phrase that retains only alphabetic characters
    output = ""
    for i in phrase:
        if i.isalpha():
            output += i
    return output


def main():
    phrase = input("Enter a phrase: ")
    print("")
    print(alpha_only(phrase))

main()
