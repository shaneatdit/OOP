"""Converts Celsius to Fahrenheit and offers some weather-appropriate advice."""


def main():
    print()
    celsius = float(input("Temperature in Celsius: "))
    print()
    fahr = celsius * 1.8 + 32
    print(celsius, "degrees Celsius is", fahr, " degrees Fahrenheit.")
    
    if celsius < -30:
        print("It's a bit chilly out! Have a vodka, comrade.")
    elif celsius < -20:
        print("Baby it's cold outside. Would you like a hot whiskey?")
    elif celsius < -10:
        print("Here's an Irish coffee to warm you up.")
    elif celsius < 0:
        print("How about a brandy?")
    elif celsius < 10:
        print("It's beer o'clock!")
    elif celsius < 20:
        print("Tequila!")
    else:
        print("Perfect weather for a mojito.")

main()
