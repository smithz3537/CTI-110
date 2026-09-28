# Zachary Smith
# September 27, 2026
# P2HW2
# This program collects six module grades, stores them in a list,
# and calculates the lowest, highest, sum, and average grades.

# Pseudocode:
# Ask the user to enter a grade for Module 1.
# Ask the user to enter a grade for Module 2.
# Ask the user to enter a grade for Module 3.
# Ask the user to enter a grade for Module 4.
# Ask the user to enter a grade for Module 5.
# Ask the user to enter a grade for Module 6.
# Store all six grades in a list.
# Find the lowest grade.
# Find the highest grade.
# Find the sum of all grades.
# Calculate the average of the grades.
# Display the results with the required formatting.

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

print()
print("------------Results------------")
print(f"Lowest Grade:  {lowest_grade:.2f}")
print(f"Highest Grade: {highest_grade:.2f}")
print(f"Sum of Grades: {sum_grades:.2f}")
print(f"Average:       {average_grade:.2f}")
