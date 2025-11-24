# -------------------------------------------
# Study Time Tracker Program
# This program asks the user for their study
# hours for the day, calculates estimated
# weekly study hours, and displays the result.
# Includes basic error handling.
# -------------------------------------------

print("Welcome to my Python program!")
hours = input("How many hours did you study today? ")

try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

weekly_hours = hours * 7
print(f"You are on track to study {weekly_hours} hours this week.")
