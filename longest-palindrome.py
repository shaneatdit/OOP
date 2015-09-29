##########################################################################
#                                                                        #
# longest-palindrome.py                                                  #
#   by Shane                                                             #
#                                                                        #
# Finds the longest palindrome(s) in a file                              #
#                                                                        #
##########################################################################


def wordlist(file):
    # Splits a file into a list of words
    with open(file) as f:
        return f.read().split()


def alphanumeric(phrase):
    # Returns a copy of phrase that retains only alphanumeric characters
    output = ""
    for i in phrase:
        if i.isalnum():
            output += i.lower()
    return output


def ispalindrome(phrase):
    # Returns True if phrase is palindromic
    phrase = alphanumeric(phrase)
    for i in range(len(phrase) // 2):
        if phrase[i] != phrase[len(phrase) - i - 1]:
            return False
    return True


def find_longest_palindrome(file):
    # Returns the longest palindrome(s) in a file
    max_length = 0
    max_palindrome = [""]
    for word in wordlist(file):
        if ispalindrome(word):
            if len(alphanumeric(word)) > max_length:
                max_palindrome = [word]
                max_length = len(alphanumeric(word))
            elif len(alphanumeric(word)) == max_length:
                max_palindrome.append(word)
    return max_palindrome, max_length


def main():
    file = input("Enter filename: ")
    # file = "c.txt"
    longest_palindrome, length = find_longest_palindrome(file)
    print()
    if longest_palindrome == [""]:
        print("No palindromes found")
    elif len(longest_palindrome) == 1:
        print("The longest palindrome is", longest_palindrome, "which has", length, "letters")
    else:
        print("The longest palindromes are", longest_palindrome, "which have", length, "letters")

main()
