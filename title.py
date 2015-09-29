##########################################################################
#                                                                        #
# title.py                                                               #
#   by Shane                                                             #
#                                                                        #
# Capitalises each word in a phrase                                      #
#                                                                        #
##########################################################################


def title(phrase):
    # Capitalises each word in phrase
    output = phrase[0].upper()
    for i in range(1, len(phrase)):
        if phrase[i - 1] == " ":
            output += phrase[i].upper()
        else:
            output += phrase[i]
    return output


def main():
    phrase = input("Enter a phrase: ")
    print("")
    print("Title:", title(phrase))

main()
