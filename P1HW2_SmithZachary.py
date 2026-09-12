# Zachary Smith
# September 12, 2026
# P1HW2
# This program calculates the remaining budget for a trip after expenses.

# Pseudocode:
# Ask the user to enter their travel budget.
# Ask the user to enter their travel destination.
# Ask the user to enter their gas expense.
# Ask the user to enter their accommodation expense.
# Ask the user to enter their food expense.
# Add the gas, accommodation, and food expenses together.
# Subtract the total expenses from the budget.
# Display the destination, budget, expenses, and remaining balance.

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("How much do you think you will need for food? "))

# Add all of the expenses together.
total_expenses = gas + accommodation + food

# Subtract the expenses from the original budget.
remaining_budget = budget - total_expenses

print("\n----------Travel Expenses----------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Gas: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
