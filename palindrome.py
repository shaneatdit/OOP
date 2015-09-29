##########################################################################
#                                                                        #
# palindrome.py                                                          #
#   by Shane                                                             #
#                                                                        #
# Checks whether a phrase is a palindrome                                #
#                                                                        #
##########################################################################


def alphanumeric(phrase):
    # Returns a copy of phrase that retains only alphanumeric characters
    output = ""
    for i in phrase:
        if i.isalnum():
            output += i.lower()
    return output


def ispalindrome(phrase):
    phrase = alphanumeric(phrase)
    for i in range(len(phrase) // 2):
        if phrase[i] != phrase[len(phrase) - i - 1]:
            return False
    return True


def main():
    phrase = input("Enter a phrase: ")
    print("")
    if ispalindrome(phrase):
        print('"', phrase, '" is a palindrome')
    else:
        print('"', phrase, '" is not a palindrome')

main()
