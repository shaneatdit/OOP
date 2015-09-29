##########################################################################
#                                                                        #
# block.py                                                               #
#   by Shane                                                             #
#                                                                        #
# Takes as arguments a string or list and an element to be blocked,      #
# prints the input minus the blocked element                             #
#                                                                        #
##########################################################################


def block(l, b):
    output = []
    for i in range(len(l)):
        if l[i] != b:
            output.append(l[i])
    return output

print(block([4, 6, 6, 6, 0, 4, 111, 111, 222, 4, 333, 444], 4))
print(block("hello", "l"))
