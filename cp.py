##########################################################################
#                                                                        #
# cp.py                                                                  #
#   by Shane                                                             #
#                                                                        #
# Copies a file                                                          #
#                                                                        #
##########################################################################


def main():
    s = input("Enter source file: ")
    source = open(s, "r")

    d = input("Enter destination: ")
    destination = open(d, "w")

    for line in source:
        destination.write(line)

    source.close()
    destination.close()

main()
