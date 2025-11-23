# -------------------------------------------
# Study Time Tracker Program
# This program asks the user for their study
# hours for the day, calculates estimated
# weekly study hours, and displays the result.
# Includes basic error handling.
# -------------------------------------------

# Welcome message
print("Welcome to the Study Time Tracker!")

# Ask the user for input
hours = input("How many hours did you study today? ")

# Try converting input to a number
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Perform a calculation: estimate weekly hours
weekly_hours = hours * 7

# Display result
print(f"You are on track to study approximately {weekly_hours} hours this week.")
