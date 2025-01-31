#Libraries Here
import sys
import time

print("Welcome Branch - Developer: Kent Chheu")
print("\n\tWelcome to InfoTechCenter V1.0")

x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + message)
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\nOperating System Booted Up - Retina Scanned - Access Granted")