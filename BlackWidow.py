# Importing necessary libraries
import sys   # For system-specific parameters and functions
import time  # For adding delay in execution

# ANSI Escape Codes for Colors
CYAN = "\033[96m"   # Light cyan text color
GREEN = "\033[92m"  # Light green text color
YELLOW = "\033[93m" # Yellow text color
RESET = "\033[0m"   # Reset to default text color

# Display welcome messages with ANSI colors
print(CYAN + "\nWelcome Branch - Developer: Kent Chheu" + RESET)   # Cyan welcome message
print(GREEN + "\n\tWelcome to InfoTechCenter V1.0\n" + RESET)      # Green version information

# Initialize variables for boot-up simulation
x = 0          # Counter for loop iterations
ellipsis = 0   # Controls the number of dots displayed in the loading message

# Simulate a boot-up process with a looping loading effect
while x != 20:
    x += 1  # Increment loop counter
    
    # Create loading message with increasing dots and yellow color
    message = YELLOW + "InfoTech Center System Booting" + "." * ellipsis + RESET
    
    # Increment ellipsis to add more dots for the next iteration
    ellipsis += 1
    
    # Display the loading message, overwriting previous output
    sys.stdout.write("\r" + message)  # "\r" returns cursor to the start of the line
    sys.stdout.flush()  # Ensure the message is displayed immediately
    time.sleep(0.5)  # Pause for half a second to simulate loading delay
    
    # Reset dots after reaching 3 to create a looping effect
    if ellipsis == 4:
        ellipsis = 0
    
    # After 20 iterations, display access granted message
    if x == 20:
        print(GREEN + "\n\nOperating System Booted Up - Retina Scanned - Access Granted\n" + RESET)
        
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