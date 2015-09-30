##########################################################################
#                                                                        #
# letter-frequency.py                                                    #
#   by Shane                                                             #
#                                                                        #
# Calculates the frequency of each letter in a file                      #
#                                                                        #
##########################################################################


def wordlist(file):
    # Returns a list of all the words in a file
    with open(file) as f:
        return f.read().split()


def frequency_list(word_list):
    # Returns the frequency of each letter within a list
    freq_list = {}
    for word in word_list:
        word = word.lower()
        for i in word:
            if i.isalpha():
                if i not in freq_list:
                    freq_list[i] = 1
                else:
                    freq_list[i] += 1
    return freq_list


def main():
    file = input("Enter filename: ")
    print()
    freq_list = frequency_list(wordlist(file))
    for key in sorted(freq_list):
        print(key, freq_list[key])

main()
