
# Name: Zachary Smith
# Date: 10/25/2026
# Assignment: P4LAB2
# Description: Displays a multiplication table for a non-negative integer
# and allows the user to run the program again.

# Pseudocode:
# 1. Set the run-again response to "yes".
# 2. While the response is "yes":
#    a. Ask the user to enter an integer.
#    b. If the integer is less than zero:
#       Display a message that negative values are not accepted.
#    c. Otherwise:
#       Use a for loop from 1 through 12.
#       Multiply the entered integer by each number.
#       Display each multiplication equation and result.
#    d. Ask the user if they want to run the program again.
#    e. If the answer is "no", exit the loop and end the program.

run_again = "yes"

while run_again == "yes":
    number = int(input("Enter an integer: "))

    if number < 0:
        print("Negative numbers are not accepted.")
    else:
        print(f"Multiplication table for {number}:")

        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")

    run_again = input(
        "Would you like to run the program again? (yes/no): "
    ).lower()

print("Program ended.")
