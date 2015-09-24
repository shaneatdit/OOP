p = input("Enter cover price: ")
coverprice = int(p)
d = input("Enter discount: ")
discount = 1 - int(d) / 100
q = input("Enter quantity: ")
quantity = int(q)
shipping = 2.25 + 0.75 * quantity
cost = (quantity * coverprice * discount) + shipping
print("The wholesale cost of ", quantity, "books is", cost)
