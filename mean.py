__author__ = 'Shane'
# calculates the mean of a list of numbers


def mymean(l):
    total = 0
    for i in range(len(l)):
        total += l[i]
    return total / len(l)

print(mymean([4, 4, 4, 6, 6, 6, 1, 1, 1, 1, 1, 1]))
