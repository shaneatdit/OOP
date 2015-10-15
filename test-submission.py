__author__ = 'd15124888'
"""OOP test, 15 October 2015."""

def calcPerimeter(side):
    """Returns the perimeter of a hexagon of side 'side'."""
    return side * 6


def calcArea(side):
    """Returns the area of a hexagon of side 'side'."""
    return (side ** 2) * 1.5 * 3 ** 0.5


def runProblemOne():
    """Prints the length, area and perimeter for hexagons of lengths from 1 to 10."""
    print("Side length          Area              Perimeter")
    for i in range(1, 11):
        print("    ", i, "            ", "%.2f" % calcArea(i), "             ", "%.2f" % calcPerimeter(i))


def runProblemTwo():
    """Prints and returns the side length where the difference between the area and the perimeter is a minimum
       for hexagons of length between 1 and 10."""
    minimumDifference = 10000000000
    bestSide = 0
    for i in range(1, 11):
        difference = abs(calcArea(i) - calcPerimeter(i))
        if difference < minimumDifference:
            bestSide = i
            minimumDifference = difference
    print("For a hexagon whose side is ", bestSide,
          ", the difference between the area and the perimeter is ", "%.2f" % minimumDifference, sep="")
    return bestSide


def calcDiscount(price):
    """Returns the discount for a given sticker price."""
    if price > 10:
        return 0.1
    elif price > 5:
        return 0.05
    else:
        return 0


def runProblemThree():
    """Prints and returns the total price for the books in bookPrices."""
    bookPrices = [15.98, 10.94, 65.00, 4.99, 2.98, 10.34]
    totalPrice = 0

    """I misunderstood the question and thought we had to print and return the discounted price for each book
    so just ignore this part:

    print("Sticker price            Discount amount              Total price")
    for price in bookPrices:
        discountedPrice = price * (1 - calcDiscount(price))
        discountedPrices.append(float("%.2f" % discountedPrice))
        discountAmount = price * calcDiscount(price)
        if price < 10:
            print(" ", end= "")
        print("%.2f" % price, "%.2f" % discountAmount, "%.2f" % discountedPrice, sep=" " * 24)
    print(discountedPrices)
    return discountedPrices
    """

    for price in bookPrices:
        discountedPrice = price * (1 - calcDiscount(price))
        totalPrice += discountedPrice
    print("The total price is", totalPrice)
    return totalPrice


def runProblemFour():
    """Prints the side length where the difference between the area and the perimeter is a minimum
       for hexagons of length between 1 and 10, to the nearest 0.01."""
    minimumDifference = 10000000000
    bestSide = 0
    side = 0
    while side <= 10:
        side += 0.01
        difference = abs(calcArea(side) - calcPerimeter(side))
        # print(side, difference)
        if difference < minimumDifference:
            bestSide = side
            minimumDifference = difference
    print("For hexagon whose side is ", "%.2f" % bestSide,
          ", the difference between the area and the perimeter is ", "%.2f" % minimumDifference, sep="")


def main():
    print(__author__)
    print(runProblemOne())
    print(runProblemTwo())
    print(runProblemThree())
    print(runProblemFour())

main()
