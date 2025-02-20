# Importing necessary libraries
import sys   # For system-specific parameters and functions
import time  # For adding delay in execution
import random  # Import the random module to generate random choices and numbers
from time import sleep  # Import sleep if needed for future enhancements

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

def get_random_gas_level():
    """
    Returns a random gas level from a predefined list.
    Levels: "Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank".
    """
    levels = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(levels)


def get_random_station():
    """
    Returns a random gas station from a predefined list.
    """
    stations = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ee's"]
    return random.choice(stations)


def gas_alert():
    """
    Checks the gas level and prints an appropriate alert message.
    For low and quarter tank levels, it calculates a random distance to a gas station.
    """
    # Retrieve a random gas level
    gas_level = get_random_gas_level()

    # Check if gas is empty and provide appropriate alerts
    if gas_level == "Empty":
        print("WARNING: YOU ARE OUT OF GAS!")
        print("CALLING DEFAULT INSURANCE COMPANY!\n")

    # For low gas, calculate miles to a gas station and display an alert
    elif gas_level == "Low":
        miles = round(random.uniform(1, 25), 1)  # Random distance between 1 and 25 miles
        station = get_random_station()  # Get a random gas station
        print("WARNING: YOUR GAS IS LOW, CHECKING GPS FOR CLOSEST GAS STATIONS!")
        print(f"CLOSEST GAS STATION IS {station}, WHICH IS {miles} MILES AWAY!\n")

    # For quarter tank gas, calculate a slightly longer random distance to a gas station
    elif gas_level == "Quarter Tank":
        miles = round(random.uniform(25.1, 50), 1)  # Random distance between 25.1 and 50 miles
        station = get_random_station()  # Get a random gas station
        print("WARNING: YOUR GAS IS ON A QUARTER TANK, CHECKING GPS FOR CLOSEST GAS STATIONS!")
        print(f"CLOSEST GAS STATION IS {station}, WHICH IS {miles} MILES AWAY!\n")

    # For half tank gas, simply notify the user that they have enough gas
    elif gas_level == "Half Tank":
        print("WARNING: YOUR GAS IS ON A HALF TANK!")
        print("ENOUGH GAS TO GET TO YOUR DESTINATION\n")

    # For three-quarter tank gas, just provide a notification
    elif gas_level == "Three Quarter Tank":
        print("WARNING: YOUR GAS IS ON A THREE QUARTER TANK!\n")

    # For full tank, confirm the gas level is full
    else:  # gas_level == "Full Tank"
        print("YOUR GAS IS ON A FULL TANK!\n")


def main():
    """
    Main function that prints the header, calls the gas_alert function,
    and prints a closing line.
    """
    # Define a header string for visual separation
    header = "\n********************************************\n"
    print(header)
    print("Gasoline Branch - Developer: Kent Chheu\n")

    # Call the gas_alert function to display the gas level message
    gas_alert()

    # Print a closing line to match the header style

# This ensures that the main function is called only when the script is run directly
if __name__ == '__main__':
    main()

# Print a decorative header
print("*****************************************\n")
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
            sleep(1)
            print(f"VRS has been engaged, only allowing us to drive {speed} MPH.")
        else:
            print(f"\nThe National Weather Service is calling for {weather_condition} skies outside.")
            sleep(1)
            print("VRS has been disengaged, drive safe!")

# Get the current weather and determine the response
current_weather = get_weather()
vehicle_response_system(current_weather)