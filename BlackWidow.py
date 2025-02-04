# Importing necessary libraries
import sys  # For system-specific parameters and functions
import time  # For adding delay in execution

# Display welcome messages
print("\nWelcome Branch - Developer: Kent Chheu")
print("\n\tWelcome to InfoTechCenter V1.0\n")

# Initialize variables
x = 0  # Counter for loop iterations
ellipsis = 0  # Controls the number of dots displayed in the loading message

# Simulate a boot-up process with a looping loading effect
while x != 20:
    x += 1  # Increment loop counter
    message = ("InfoTech Center System Booting" + "." * ellipsis)  # Create loading message with dots
    ellipsis += 1  # Increase the number of dots displayed
    sys.stdout.write("\r" + message)  # Overwrite the previous message on the same line
    time.sleep(.5)  # Delay for half a second to simulate loading effect
    
    if ellipsis == 4:  # Reset dots after reaching 3 to create a looping effect
        ellipsis = 0
    
    if x == 20:  # Stop loop after 20 iterations and display access message
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")