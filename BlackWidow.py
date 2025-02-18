import random  # Import the random module to generate random choices and numbers
from time import sleep  # Import sleep if needed for future enhancements


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
