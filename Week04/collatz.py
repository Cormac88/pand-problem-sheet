# Inputs any positive integer and if the value is even, divide it by two, but if it is odd, multiply it by three 
# and add one. The Program ends when the current value is 1.

# Author: Cormac Hennigan

collatz = []    # The list is empty at first because it will be appended later

number = int(input("Please enter a positive integer: ")) # Prompts the user to enter a positive integer

while number != 1:  # Start of while loop
    if number % 2 == 0:
        number = number // 2            # If number is even, divide it by 2
    else:                               # If the number is not even (The only other outcome),
        number = (number * 3) + 1       # multiply the number by 3 and add one.
    collatz.append(number)  # The loop is complete when 1 is added to the list.

print(collatz)  # Prints the completed list