"""
Calculates simple and compound interest and prints a quarterly table.

Prompts user for a principal amount, interest rate, number of years, and number of terms per year.
If the inputted interest rate includes a percentage sign, it is assumed to be in percentage for (e.g., 8%)
Otherwise, it is a interpreted as a decimal fraction (0.08)
"""


def convert_partial_string_to_number(number):
    """Removes % sign, etc."""
    output = ""
    for i in number:
        if i.isdigit():
            output += i
        elif i == "." or i == ",":
            output += "."
    output = float(output)
    return output


def simple_interest(principal, rate, years):
    return principal + (principal * (rate / 100) * years)


def compound_interest(principal, rate, years, terms_per_year):
    increase_per_term = 1 + (rate / (terms_per_year * 100))
    total_number_of_terms = years * terms_per_year
    new_balance = principal * (increase_per_term ** total_number_of_terms)
    return new_balance


def print_quarterly_table(balance, rate, years, terms_per_year):
    increase_per_term = 1 + (rate / (terms_per_year * 100))
    number_of_terms = years * terms_per_year
    print("{:,}".format(balance), " at ", rate, "% compounded quarterly for ", years, " years yields ", "%.2f" % compound_interest(balance, rate, years, terms_per_year), sep='')
    for i in range(number_of_terms):
        balance = balance * (increase_per_term)
        if i < 9:
            print("Quarter: ", i + 1, "Balance:", "%.2f" % balance)
        else:
            print("Quarter:", i + 1, "Balance:", "%.2f" % balance)


def main():

    # Prompt user for numbers
    principal = float(input("What's the princial amount? "))

    # Prompt user for interest rate, then convert to a float
    # Multiply by 100 if it doesn't include a percent sign
    r = input("What's the interest rate? (e.g., 8% or 0.08) ")
    if "%" in r:
        rate = convert_partial_string_to_number(r)
    else:
        rate = convert_partial_string_to_number(r) * 100
    print("Interest rate = ", rate, "%", sep='')

    years = float(input("How many years? "))
    terms_per_year = int(input("How many times does interest accrue each year? "))

    # Exercise 1: calculate simple interest
    print()
    print("After", years, "years (simple interest), you will have", "%.2f" % simple_interest(principal, rate, years))

    # Exercise 2: calculate the sifference over 20 years on a 1,000 euro balance
    # between compounding yearly and compounding monthly at 8% interest
    print()
    print("1,000 euro at 8% compounded monthly for 20 years:  ", "%.2f" % compound_interest(1000, 8, 20, 12))
    print("1,000 euro at 8% compounded annually for 20 years: ", "%.2f" % compound_interest(1000, 8, 20, 1))
    print("Difference:                                        ", "%.2f" % (compound_interest(1000, 8, 20, 12) - compound_interest(1000, 8, 20, 1)))
    print()

    # Exercises 3 & 4: print an interest table, formatted exactly as on the problem sheet
    print_quarterly_table(1500, 4.3, 3, 4)

main()
