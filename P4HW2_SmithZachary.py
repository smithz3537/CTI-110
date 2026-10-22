# Zachary Smith 
# 10/22/2026
# P4HW2 - Salary Calculator
# This program calculates regular pay, overtime pay, and gross pay
# for multiple employees and displays the totals for all employees.

# Pseudocode:
# Ask the user to enter an employee's name.
# Set the totals for overtime pay, regular pay, gross pay,
# and number of employees to zero.
# While the employee's name is not "Done":
#     Ask the user to enter the employee's pay rate.
#     Ask the user to enter the number of hours worked.
#     If hours worked is greater than 40:
#         Calculate regular pay using 40 hours.
#         Calculate overtime hours by subtracting 40.
#         Calculate overtime pay using 1.5 times the pay rate.
#     Otherwise:
#         Calculate regular pay using hours worked.
#         Set overtime pay to zero.
#     Calculate gross pay by adding regular and overtime pay.
#     Display the employee's name, pay rate, hours worked,
#     overtime hours, overtime pay, regular pay, and gross pay.
#     Add the employee's pay amounts to the totals.
#     Increase the employee count by one.
#     Ask for the next employee's name.
# Display the total overtime pay, regular pay, gross pay,
# and number of employees.
# End the program.

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Get the first employee's name
employee_name = input("Enter employee's name or \"Done\" to terminate: ")

# Process employees until the user enters Done
while employee_name != "Done":

    pay_rate = float(input("Enter employee's pay rate: "))
    hours_worked = float(input("Enter hours worked: "))

    # Calculate regular and overtime pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
        overtime_pay = overtime_hours * pay_rate * 1.5
    else:
        overtime_hours = 0
        regular_hours = hours_worked
        overtime_pay = 0

    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Display employee information
    print()
    print(f"Employee name: {employee_name}")
    print()
    print(f"{'Hours Worked':<18}{'Pay Rate':<15}{'OverTime':<15}"
          f"{'OverTime Pay':<18}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print("-" * 96)
    print(f"{hours_worked:<18.2f}${pay_rate:<14.2f}"
          f"{overtime_hours:<15.2f}${overtime_pay:<17.2f}"
          f"${regular_pay:<14.2f}${gross_pay:<14.2f}")

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Get the next employee's name
    print()
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")

# Display final totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:,.2f}")
print(f"Total amount paid for regular pay: ${total_regular_pay:,.2f}")
print(f"Total amount paid for all employees: ${total_gross_pay:,.2f}")
