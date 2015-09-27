__author__ = 'Shane'
# calculates the number of coins required to make a certain amount


principal = int(input("Please enter the total amount in cents: "))
balance = principal
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

while balance >= 100:
    dollars += 1
    balance -= 100

while balance >= 25:
    quarters += 1
    balance -= 25

while balance >= 10:
    dimes += 1
    balance -= 10

while balance >= 5:
    nickels += 1
    balance -= 5

while balance >= 1:
    pennies += 1
    balance -= 1

print(principal, "cents is:")
print(dollars, "dollars")
print(quarters, "quarters")
print(dimes, "dimes")
print(nickels, "nickels, and")
print(pennies, "pennies")
