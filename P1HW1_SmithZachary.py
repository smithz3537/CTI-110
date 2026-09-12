# Zachary Smith
# September 12, 2026
# P1HW1
# This program calculates an exponent and performs addition and subtraction using user input.

print("-----Calculating Exponents-----")

base = int(input("\nEnter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print(f"\n{base} raised to the power of {exponent} is {result} !!")

print("\n-----Addition and Subtraction-----")

starting_integer = int(input("\nEnter a starting integer: "))
add_integer = int(input("Enter an integer to add: "))
subtract_integer = int(input("Enter an integer to subtract: "))

answer = starting_integer + add_integer - subtract_integer

print(f"\n{starting_integer} + {add_integer} - {subtract_integer} is equal to {answer}")
