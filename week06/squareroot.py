# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Cormac Hennigan

# From: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YEEjBWj7Qaa
# The definition for Newton's Square Root Approximation is:
# √ N ≈ ½(N/A + A)
# Where:
# N is a positive number of which you want to find the square root
# √ is the square root sign
# ≈ means "approximately equal to..."
# A is an educated guess

# Using Newton's method, you make an educated guess of a number A that when squared, will be close to equaling A.
# If N = 121 and I guess A = 5, my guess is not close enough. Entering 5 into the equation would give 
# an answer of 14.6.
# I can plug the 14.6 back into the equation which gives 11.445 which is getting closer to the correct answer
# of 11.

# This is called Iterative calculations and you can continue this until you get an accuate answer.

# The code below illustrates this
# (https://stackoverflow.com/questions/20811208/newton-s-method-for-finding-square-roots-in-python)

def sqrt(n):
    approx = n / 2.0
    # The first guess is going to be the number that the user enters divided by 2, not a good
    # Approximation but it is a starting point 
    while True:
        better = (n / approx + approx) / 2.0
        # The next approximation, or in other words, a better approximation, is to plug the first approximation in as 
        # A in the Newtons equation, and n is the value that the user inputted (N in the Newton equation).
        # The while true loop in an infinite loop
        # https://tutorial.eyehunts.com/python/while-true-python-while-loop-is-bad-break-out/
        if abs(approx - better) < 0.00001:
            return better
        approx = better
        # Here I am saying that when the calculation for the variable 'better' is complete, to move onto the if
        # statement approx-better. If the statement is not true, then move onto the next part of the function. The
        # Variable 'approx' is now equal to 'better', so now the variable 'approx' is actually different than it 
        # was for the first loop and is closer to the true square root of the user's input. The loop goes again
        # and this time approx-better is getting closer to 0. When the if statement is satisfied and the return
        # statement is hit, python immediately exits the function. In other words, when 'return better' is reached, 
        # 'sqrt' is exited and, in the process, so is the while-loop.

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
# not allowed in this formula. This is becuse you cannot get the square root of a negative number as this gets
# into complex numbers (√(-1) = i). Zero is actually allowed though because 0 squared is 0.
# The 'try-except' statement is within an infinite loop just like the while true loop in 'def sqrt(n)'. The user must
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
# https://socratic.org/questions/what-is-the-square-root-of-zero
	   
n = (inputNumber("Please enter a positive number: "))

print("Square root of {} is approx {}" .format(n, round(sqrt(n) ,1)))
# Calls the function and prints the answer rounded to one decimal place as required.