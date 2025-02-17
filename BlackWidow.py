print("\n********************************************\n")
print("Gasoline Branch - Developer: Kent Chheu")
print("\n********************************************\n")

import random 
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ee's"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("WARNING: YOU ARE OUT OF GAS!")
        print("\nCALLING DEFAULT INSURANCE COMPANY!\n")

    elif gasLevelIndicator == "Low":
        print("WARNING: YOUR GAS IS LOW, CHECKING GPS FOR CLOSEST GAS STATIONS!")
        print("\nCLOSEST GAS STATION IS", gasStations(), "WHICH IS", milesToGasStationLow, "MILES AWAY!\n")

    elif gasLevelIndicator == "Quarter Tank":
        print("WARNING: YOUR GAS IS ON A QUARTER TANK, CHECKING GPS FOR CLOSEST GAS STATIONS!")
        print("\nCLOSEST GAS STATION IS", gasStations(), "WHICH IS", milesToGasStationQuarterTank, "MILES AWAY!\n")

    elif gasLevelIndicator == "Half Tank":
        print("WARNING: YOUR GAS IS ON A HALF TANK!")
        print("\nIS ENOUGH GAS TO GET TO YOUR DESTINATION\n")

    elif gasLevelIndicator == "Three Quarter Tank":
        print("WARNING: YOUR GAS IS ON A THREE QUARTER TANK!\n")

    else:
        print("YOUR GAS IS ON A FULL TANK!\n")
gasLevelAlert()

print("********************************************\n")