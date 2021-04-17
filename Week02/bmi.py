# Calculates somebody's Body Mass Index (BMI).
# Author: Cormac Hennigan

def inputNumber(message):
    while True:
        try:
            userInput = float(input(message))
            while userInput < 0:
                print("That's a negative number! Try again.")
                userInput = float(input(message))       
        except ValueError:
            print("That's a string! Try again.")
            continue
        else:
            return userInput

# This function is used to stop the error of negative numbers and strings being used in this equation, as they are 
# not allowed in this formula. The 'try-except' statement is within an infinite loop just like the while true loop in 'def sqrt(n)'. The user must
# enter a positive number here. If they enter a negative number, the while loop within the while true loop is 
# activated. The same messages are repeated until the user stops entering negative numbers. If the user
# inputs something other than a number, the program moves to the 'except' block of the function. This is where we
# handle the error. The continue statement rejects all the remaining statements in the current iteration of the 
# loop and moves the control back to the top of the loop. The user is asked to again input a positive number.
# The while loop is completed when the user enters a positive number.
# https://www.includehelp.com/python/asking-the-user-for-integer-input-in-python-limit-the-user-to-input-only-integer-value.aspx
# https://pythonbasics.org/try-except/
# https://stackoverflow.com/questions/22214787/python-repeat-while-user-enters-negative-number
# https://www.tutorialspoint.com/python/python_continue_statement.htm
	   
weight = (inputNumber('Enter weight (Kg): '))
height1 = (inputNumber('Enter height (cm): '))

# Asks the user to input their weight in kg and their height in cm

height2 = ((height1 / 100))**2
BMI = round(weight / height2, 2)

# Converts the height from centimeters to meters squared. This is because the formula to calculate a person's BMI is:
# BMI = weight (kg) / (height(m ** 2))
# https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php
# https://stackoverflow.com/questions/36048713/3-arguments-calculating-bmi-python

print ('BMI is {}'.format (BMI))

# Prints out the resulting BMI in kg/m**2 (Kilograms per metre squared)