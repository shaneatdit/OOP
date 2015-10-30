"""
Prompts user to input weight and height
(in either metric or imperial units)
then prints body mass index and category.
"""

def main():
    # Prompt user to choose metric or imperial
    while True:
        metric_or_imp = input("Metric or imperial? (M/I) ").lower()
        print()
        if metric_or_imp[0] == "m":
            system = "metric"
            print("You have chosen metric")
            units = ["kilograms", "centimeters"]
            break
        elif metric_or_imp[0] == "i":
            system = "imperial"
            print("You have chosen imperial")
            units = ["pounds", "inches"]
            break

    # Prompt user to enter weight
    while True:
        question = "Please enter your weight in " + units[0] + ": "
        string = input(question)
        try:
            float(string)
            weight = float(string)
            if weight > 0:
                break
            print()
            print(string, "is not a valid number")
        except ValueError:
            print()
            print(string, "is not a valid number")

    # Prompt user to enter height
    while True:
        question = "Please enter your height in " + units[1] + ": "
        string = input(question)
        try:
            float(string)
            height = float(string)
            if height > 0:
                break
            print()
            print(string, "is not a valid number")
        except ValueError:
            print()
            print(string, "is not a valid number")

    if system == "imperial":
        # Convert to metric
        weight /= 2.20462
        height /= 0.393701

    # Calculate and print BMI
    bmi = weight / (height / 100) ** 2
    print()
    print("Your BMI is", '%.2f' % bmi)

    # Print category
    if bmi >= 30:
        print("Category: obese")
    elif bmi >= 25:
        print("Category: overweight")
    elif bmi >= 18.5:
        print("Category: normal")
    elif bmi >= 16:
        print("Category: underweight")
    else:
        print("Category: severely underweight")

main()
