"""
Program: videoStore.py
Chapter 2 Project (page 62)
7/24/2024

Simple app that prompts user for the number of video rentals in pricing categories. Calculates and displays the grand total. 
"""

# Variables and constants 
NEW_VIDEOS = 3.00
OLD_VIDEOS = 2.00

# Input phase
numNew = int(input("please enter the number of NEW videos being rented: "))
numOld = int(input("Next, enter the number of OLD videos being rented: "))

# Processing phase
grandTotal = (NEW_VIDEOS * numNew) + (OLD_VIDEOS * numOld) 
grandTotal = round(grandTotal, 2)

# Output phase
print("The customer is renting: " + str(numNew) + " new video(s).")
print("The customer is also renting: " + str(numOld) + " old video(s).")
print("The total charge is: $" + str(grandTotal))

input("\nPress ENTER to exit this program...")