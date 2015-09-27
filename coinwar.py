__author__ = 'Shane'
from random import randint
# Coin War


n = int(input("How coins per player? "))
coin_Same = n
coin_Diff = n

print("")
print("Coins:                   Winner:             Tally:")
while coin_Same > 0 and coin_Diff > 0:
    coinA = randint(0, 1)
    coinB = randint(0, 1)
    if coinA == coinB:
        winner = "Same"
        coin_Same += 1
        coin_Diff -= 1
    else:
        winner = "Diff"
        coin_Same -= 1
        coin_Diff += 1
    print(" A:", coinA, "B:", coinB, "              ", winner, "               Same:", coin_Same, "  Diff:", coin_Diff)

print("")
if coin_Same == 0:
    print("Diff wins!")
elif coin_Diff == 0:
    print("Same wins!")
