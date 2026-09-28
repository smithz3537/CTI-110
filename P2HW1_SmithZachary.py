# Zachary Smith
# September 27, 2026
# P2HW1
# This program calculates travel expenses and displays the results
# using formatted dollar amounts and aligned columns.

# Pseudocode:
# Ask the user for their travel destination.
# Ask the user for their budget.
# Ask the user for gas expenses.
# Ask the user for accommodation expenses.
# Ask the user for food expenses.
# Calculate the remaining balance.
# Display all expenses in aligned columns with dollar signs
# and two decimal places.

destination = input("Enter your travel destination: ")
budget = float(input("Enter your budget: "))
gas = float(input("Enter the amount you will spend on gas: "))
accommodation = float(input("Enter the amount you will spend on accommodation: "))
food = float(input("Enter the amount you will spend on food: "))

remaining = budget - gas - accommodation - food

print()
print("------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Gas:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${accommodation:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining:,.2f}")