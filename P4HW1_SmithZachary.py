
# Zachary Smith 
# 10/22/2026
# Assignment Name: P4HW1 - Score Average
# This program collects scores, validates them, drops the lowest score,
# calculates the average of the remaining scores, and displays a letter grade.

# Pseudocode:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store valid scores.
# 3. Use a loop to collect each score.
# 4. Check whether each score is between 0 and 100.
# 5. If the score is invalid, display an error and ask again.
# 6. Add each valid score to the list.
# 7. Find and display the lowest score.
# 8. Remove the lowest score from the list.
# 9. Display the modified score list.
# 10. Calculate and display the average of the remaining scores.
# 11. Determine and display the letter grade.
# 12. End the program.

# Ask the user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list for the scores
scores = []

# Loop to collect the scores
for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))

    # Validate the score
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")

        score = float(input(f"Enter score #{i + 1} again: "))

    # Add valid score to the list
    scores.append(score)

# Find the lowest score
lowest_score = min(scores)

print("\n------------ Results ------------")
print(f"Lowest score  : {lowest_score}")

# Remove the lowest score
scores.remove(lowest_score)

# Display the modified list
print(f"Modified List : {scores}")

# Calculate the average
average = sum(scores) / len(scores)

print(f"Scores Average: {average:.2f}")

# Determine the letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade         : {grade}")
