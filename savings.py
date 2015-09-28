__author__ = 'Shane'
# Calculates how long it will take a principal amount
# to grow to reach to a savings target

principal = float(input("Please enter the principal amount: "))
rate = float(input("Please enter the interest rate: "))
goal = float(input("Please enter your savings target: "))
print("")
balance = principal
year = 0

while balance < goal:
    year += 1
    balance *= 1 + (rate / 100)
    m = "%0.2f" % balance
    print("After", year, "years, you will have $", m)

print("")
print("It will take you", year, "years to reach your target")
