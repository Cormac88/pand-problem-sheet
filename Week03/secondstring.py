# Program that inputs a string and outputs every second letter in reverse order.

# Author: Cormac Hennigan

sentence = str(input("Please enter a sentence: "))

# The below parameters are start, stop and step from left to right. Start specifies which
# posotion to start at, Stop specifies which position to stop at and Step specifies the incrementation.
# I have told the program to go in increments of 2 but in reverse order

print(sentence[::-2])
