import math

print("Welcome to the Calculator Program!")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Exponentiation")
print("0: Exit")

toggle = True

while toggle:
    choice = input("Choose your operation (0-6): ")

    if choice == "1":
        num1 = float(input("Enter first value: "))
        num2 = float(input("Enter second value: "))
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == "2":
        num1 = float(input("Enter first value: "))
        num2 = float(input("Enter second value: "))
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == "3":
        num1 = float(input("Enter first value: "))
        num2 = float(input("Enter second value: "))
        print(f"{num1} x {num2} = {num1 * num2}")
    elif choice == "4":
        num1 = float(input("Enter first value: "))
        num2 = float(input("Enter second value: "))
        print(f"{num1} ÷ {num2} = {num1 / num2}")
    elif choice == "5":
        num1 = float(input("Enter radicand value: "))
        num2 = float(input("Enter index value: "))
        if num2 < 0:
            print("This is only available in complex numbers.")
        elif num2 == 0:
            print("The root of 0 is always 0.")
        else:
            if num1 == 0:
                print("The root of any number to the power of 0 is always 1.")
            else:
                print(f"{num2}√{num1} = {num1 ** (1 / num2)}")
    elif choice == "6":
        num1 = float(input("Enter base value: "))
        num2 = float(input("Enter exponent value: "))
        print(f"{num1}^{num2} = {num1 ** num2}")
    elif choice == '0':
        print("Exiting the program. Goodbye!")
        toggle = False
    else:
        print("Invalid input. Please choose a valid operation (0-6).")