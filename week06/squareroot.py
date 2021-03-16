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
# (https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method).

def newton_method(number, number_iters = 100):    # Funtion that has 2 arguments.
                                                  
    
    a = float(number)   # The first guess is going to be the same number that the user enters, not a good
                        # Approximation but it is a starting point    
                    
    for _ in range(number_iters):                     
        number = round(0.5 * (number + a / number), 1)
         
        # number_iters is the amount of times that the answer to the above equation will be plugged back into
        # the equation

    return number

# Using a for loop, the number that the user inputs is put back into the Newton eqution, and that answer is 
# then also put back in. This is done 100 times and rounded to one decimal place as requested. _ is used instead
# of a variable because the variable was not used
# (https://stackoverflow.com/questions/52792987/unused-variable-in-a-for-loop)

a = float(input("Please enter a positive number: ")) # Asks the user to input a value to find the square root of

while a <= 0:
    a = float(input("Please enter a positive number: "))

# This while loop is used to stop the error of negative numbers being used in this equation, as they are not
# allowed in this formula. This is becuse you cannot get the square root of a negative number as this gets
# into complex numbers (√(-1) = i). The while loop is completed when the user enters a positive number.
# https://stackoverflow.com/questions/22214787/python-repeat-while-user-enters-negative-number

print("Square root of {} is approx {}" .format(a, newton_method(a))) # Calls the function and prints the answer