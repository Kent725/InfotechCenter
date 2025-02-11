import random

# Print a decorative header
print("\n*****************************************\n")
print("Weather Branch - Developer: Kent Chheu")

# Function to determine the weather condition randomly
def get_weather():
    weather_forecast_list = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    return random.choice(weather_forecast_list)

# Dictionary for vehicle response settings
weather_responses = {
    "snowing": (30, 55),
    "blizzard": (60, 45),
    "icy": (90, 35),
    "rainy": (10, 65),
    "windy": (5, 70),
    "sunny": (0, None)  # No delay, VRS disengaged
}

# Function to determine the vehicle response based on weather conditions
def vehicle_response_system(weather_condition):
    if weather_condition in weather_responses:
        delay, speed = weather_responses[weather_condition]
        if speed:
            print(f"\nThe National Weather Service has updated our alarm by {delay} minutes "
                  f"because of the forecast of {weather_condition} outside.")
            print(f"VRS has been engaged, only allowing us to drive {speed} MPH.")
        else:
            print(f"\nThe National Weather Service is calling for {weather_condition} skies outside.")
            print("VRS has been disengaged, drive safe!")

# Get the current weather and determine the response
current_weather = get_weather()
vehicle_response_system(current_weather)
