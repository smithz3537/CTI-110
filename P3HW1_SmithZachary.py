
# Name: Zachary Smith
# Date: 10/11/2026
# Assignment: P3HW1
# Description: Collect six grades and calculate the lowest,
# highest, sum, average, and letter grade.

# Pseudocode:
# Create an empty list to store grades.
# Ask the user to enter six grades.
# Add each grade to the list.
# Find the lowest and highest grades.
# Calculate the sum and average.
# Determine the letter grade from the average.
# Display the results.

# Create a list for grades
grades = []

# Get six grades from the user
for i in range(1, 7):
    grade = float(input(f"Enter grade for module {i}: "))
    grades.append(grade)

# Calculate grade statistics
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Determine letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20} {lowest:.1f}")
print(f"{'Highest Grade:':<20} {highest:.1f}")
print(f"{'Sum of Grades:':<20} {total:.1f}")
print(f"{'Average:':<20} {average:.2f}")

print("--------------------------------")
print(f"Your grade is: {letter_grade}")
