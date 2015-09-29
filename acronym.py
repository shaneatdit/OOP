##########################################################################
#                                                                        #
# acronym.py                                                             #
#   by Shane                                                             #
#                                                                        #
# Prints an acronym for a phrase                                         #
#                                                                        #
##########################################################################


def find_next_letter(phrase, i):
    # Returns the next letter in a string, or None
    if i == len(phrase):
        return None
    elif phrase[i].isalpha():
        return i
    else:
        return find_next_letter(phrase, i + 1)


def find_next_space(phrase, i):
    # Returns the next space in a string, or None
    if i == len(phrase):
        return None
    elif phrase[i] == " ":
        return i
    else:
        return find_next_space(phrase, i + 1)


def acronym(phrase):
    # Returns an acronym
    output = ""
    i = 0
    is_space = True
    while i < len(phrase):
        if is_space:
            i = find_next_letter(phrase, i)
            if i is None:
                return output
            output += phrase[i].upper()
            is_space = False
            i += 1
        elif is_space is False:
            i = find_next_space(phrase, i)
            if i is None:
                return output
            is_space = True
            i += 1
    return output


def main():
    phrase = input("Enter a phrase: ")
    print("")
    print("Acronym:", acronym(phrase))

main()
