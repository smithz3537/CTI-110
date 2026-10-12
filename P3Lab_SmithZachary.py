
# Name: Zachary Smith
# Assignment: P3LAB
# Date: 10/11/2026
# Description: Calculate the fewest dollars and coins needed
#              to make an amount of money.

# Pseudocode:
# Ask the user to enter an amount of money.
# Convert the amount to cents.
# Calculate the number of dollars and remaining cents.
# Calculate quarters, dimes, nickels, and pennies.
# Display only denominations that are needed.
# Use singular names for one and plural names for more than one.

# Get amount of money from user
amount = float(input("Enter the amount of money as a float: $"))

# Convert dollars to cents
cents = int(round(amount * 100))

# Calculate dollars
dollars = cents // 100
cents = cents - (dollars * 100)

# Calculate quarters
quarters = cents // 25
cents = cents - (quarters * 25)

# Calculate dimes
dimes = cents // 10
cents = cents - (dimes * 10)

# Calculate nickels
nickels = cents // 5
cents = cents - (nickels * 5)

# Remaining cents are pennies
pennies = cents

# Display results
if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(f"{dollars} Dollars")

if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(f"{quarters} Quarters")

if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(f"{dimes} Dimes")

if nickels > 0:
    if nickels == 1:
        print("1 Nickel")
    else:
        print(f"{nickels} Nickels")

if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(f"{pennies} Pennies")
