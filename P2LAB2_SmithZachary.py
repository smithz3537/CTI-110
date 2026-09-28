# Zachary Smith
# September 27, 2026
# P2LAB2
# This program uses a dictionary to store automobile MPG values,
# asks the user to select a vehicle and enter miles driven,
# then calculates the gallons of gas needed.

# Pseudocode:
# Create a dictionary containing vehicles and their MPG.
# Get all keys from the dictionary.
# Display the vehicle keys.
# Ask the user to enter a vehicle.
# Display the MPG for the selected vehicle.
# Ask the user for the number of miles they will drive.
# Calculate gallons needed by dividing miles by MPG.
# Display the gallons needed rounded to two decimal places.

cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = cars.keys()

print(keys)

vehicle = input("Enter a vehicle to see its MPG: ")
print(f"The {vehicle} gets {cars[vehicle]} MPG.")

miles = float(input("Enter the number of miles you will drive: "))

gallons = miles / cars[vehicle]

print(f"To drive {miles} miles in the {vehicle}, you will need {gallons:.2f} gallons of gas.")
