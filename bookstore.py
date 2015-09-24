coverprice = float(input("Enter cover price: "))
d = float(input("Enter discount rate: "))
discount = 1 - d / 100
quantity = int(input("Enter quantity: "))
shipping = 2.25 + 0.75 * quantity
cost = (quantity * coverprice * discount) + shipping
print("")
print(quantity, "books at ", coverprice, "per book:   ", coverprice * quantity)
print("Discount (", d, "%):            ", quantity * coverprice * d / 100)
print("Discounted price:              ", quantity * coverprice * discount)
print("Shipping cost:                 ", shipping)
print("")
print("The net cost of", quantity, "books is:   ", "%.2f" % cost)
