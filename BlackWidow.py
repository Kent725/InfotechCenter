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

print(weather())