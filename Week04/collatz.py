# Inputs any positive integer and if the value is even, divide it by two, but if it is odd, multiply it by three 
# and add one. The Program ends when the current value is 1.
# Author: Cormac Hennigan

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
            while userInput < 0:
                print("That's a negative number! Try again.")
                userInput = int(input(message))       
        except ValueError:
            print("That's not an integer! Try again.")
            continue
        else:
            return userInput

# This function is used to stop the error of non-integers, negative numbers and strings being used in this equation, 
# as they are not allowed in this formula. The 'try-except' statement is within an infinite loop. The user must enter
# a positive integer here. If they enter a negative number or a non-integer, the while loop within the while true
# loop is activated.
# The same messages are repeated until the user stops entering negative numbers or non-integers. 
# If the user inputs something other than a number, the program moves to the 'except' block of the function. 
# This is where we handle the error. The continue statement rejects all the remaining statements in the current 
# iteration of the loop and moves the control back to the top of the loop. The user is asked to again input a 
# positive number. The while loop is completed when the user enters a positive number.
# https://www.includehelp.com/python/asking-the-user-for-integer-input-in-python-limit-the-user-to-input-only-integer-value.aspx
# https://pythonbasics.org/try-except/
# https://stackoverflow.com/questions/22214787/python-repeat-while-user-enters-negative-number
# https://www.tutorialspoint.com/python/python_continue_statement.htm

collatz = []    # The list is empty at first because it will be appended later

number = inputNumber("Please enter a positive integer: ") # Prompts the user to enter a positive integer

while number != 1:  # Start of while loop
    if number % 2 == 0:
        number = number // 2            # If number is even, divide it by 2
    else:                               # If the number is not even (The only other outcome),
        number = (number * 3) + 1       # multiply the number by 3 and add one.
    collatz.append(number)              # The loop is complete when 1 is added to the list.

print(collatz)  # Prints the completed list