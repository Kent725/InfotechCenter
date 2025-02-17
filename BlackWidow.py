print("\n********************************\n")
print("Gasoline Branch - Developer: Kent Chheu\n")

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
        print("CALLING DEFAULT INSURANCE COMPANY!")
    elif gasLevelIndicator == "Low":
        print("WARNING: YOUR GAS IS LOW, CHECKING GPS FOR CLOSEST GAS STATIONS!")
        print("CLOSEST GAS STATION IS", gasStations(), "WHICH IS", milesToGasStationLow, "MILES AWAY!")
    elif gasLevelIndicator == "Quarter Tank":
        print("WARNING: YOUR GAS IS ON A QUARTER TANK, CHECKING GPS FOR CLOSEST GAS STATIONS!")
        print("CLOSEST GAS STATION IS", gasStations(), "WHICH IS", milesToGasStationQuarterTank, "MILES AWAY!")
    elif gasLevelIndicator == "Half Tank":
        print("WARNING: YOUR GAS IS ON A HALF TANK!")
        print("IS ENOUGH GAS TO GET TO YOUR DESTINATION")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("WARNING: YOUR GAS IS ON A THREE QUARTER TANK!")
    else:
        print("YOUR GAS IS ON A FULL TANK!")
gasLevelAlert()
