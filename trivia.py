age = float(input("How old are you? "))
weight = float(input("What do you weigh? (in kg) "))
height = float(input("How tall are you? (in cm) "))

print("")
print("The earth has travelled ", age * 12299040000 ," kilometers during your lifetime.")
print("Your body contains around", "%.2f" % (weight * 1.4e-3) ,"milligrams of gold.")
print("You are", "%.2f" % (height / 2.72) ,"% as tall as Robert Wadlow.")
