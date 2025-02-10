print("\n*****************************************\n")

print("Weather Branch - Developer: Kent Chheu\n")

#Import Libraries HERE
import random
from time import sleep

# Weather Function to Determine the Weather
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert = weather()

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
    else:
        print("\nThe National Weather Service is calling for", weatherAlert, "skys outside, drive safe!")

vehicleResponseSystem()