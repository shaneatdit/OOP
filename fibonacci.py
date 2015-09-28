__author__ = 'Shane'
# Prints the first n Fibonacci numbers


def fibonacci(n):
    output = []
    for i in range(n):
        if i < 2:
            output.append(1)
        else:
            output.append(output[i - 2] + (output[i - 1]))
    return output


def main():
    num = 0
    while num <= 0:
        num = int(input("How many Fibonacci numbers would you like? "))
        if num <= 0:
            print("")
            print("Please enter a positive number!")
    print("")
    print(fibonacci(num))

main()
