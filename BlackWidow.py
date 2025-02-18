import random
from time import sleep


def get_random_gas_level():
    """Return a random gas level from the predefined list."""
    levels = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(levels)


def get_random_station():
    """Return a random gas station from the predefined list."""
    stations = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ee's"]
    return random.choice(stations)


def gas_alert():
    """Check the gas level and print an appropriate alert."""
    gas_level = get_random_gas_level()

    if gas_level == "Empty":
        print("WARNING: YOU ARE OUT OF GAS!")
        print("CALLING DEFAULT INSURANCE COMPANY!\n")

    elif gas_level == "Low":
        miles = round(random.uniform(1, 25), 1)
        station = get_random_station()
        print("WARNING: YOUR GAS IS LOW, CHECKING GPS FOR CLOSEST GAS STATIONS!")
        print(f"CLOSEST GAS STATION IS {station}, WHICH IS {miles} MILES AWAY!\n")

    elif gas_level == "Quarter Tank":
        miles = round(random.uniform(25.1, 50), 1)
        station = get_random_station()
        print("WARNING: YOUR GAS IS ON A QUARTER TANK, CHECKING GPS FOR CLOSEST GAS STATIONS!")
        print(f"CLOSEST GAS STATION IS {station}, WHICH IS {miles} MILES AWAY!\n")

    elif gas_level == "Half Tank":
        print("WARNING: YOUR GAS IS ON A HALF TANK!")
        print("ENOUGH GAS TO GET TO YOUR DESTINATION\n")

    elif gas_level == "Three Quarter Tank":
        print("WARNING: YOUR GAS IS ON A THREE QUARTER TANK!\n")

    else:  # gas_level == "Full Tank"
        print("YOUR GAS IS ON A FULL TANK!\n")


def main():
    header = "\n********************************************\n"
    print(header)
    print("Gasoline Branch - Developer: Kent Chheu")
    print(header)

    gas_alert()

    print("********************************************\n")


if __name__ == '__main__':
    main()
