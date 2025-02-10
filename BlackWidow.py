# Print a decorative header
print("\n*****************************************\n")
print("Weather Branch - Developer: Kent Chheu\n")

# Import necessary libraries
import random  # Used for generating random weather conditions
from time import sleep  # (Not used in this script, but could be useful for delays)

# Function to determine the weather condition randomly
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    # Randomly select one condition from the list
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

# Generate a random weather alert
weatherAlert = weather()

# Function to determine the vehicle response based on weather conditions
def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
        " of the forecast of", weatherAlert, "outside.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 60 minutes because"
        " of the forecast of", weatherAlert, "outside.")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 90 minutes because"
        " of the forecast of", weatherAlert, "outside.")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 10 minutes because"
        " of the forecast of", weatherAlert, "outside.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
        " of the forecast of", weatherAlert, "outside.")
    else:  # Default case for "sunny"
        print("\nThe National Weather Service is calling for", weatherAlert, "skies outside, drive safe!")

# Call the function to display the weather response
vehicleResponseSystem()
