# Calculates somebody's Body Mass Index (BMI).
# Author: Cormac Hennigan

Weight = int(input ('Enter weight (Kg): '))
Height1 = int(input ('Enter height (cm): '))

# Asks the user to input their weight in kg and their height in cm

Height2 = ((Height1 / 100))**2
BMI = round(Weight / Height2, 2)

# Converts the height from centimeters to meters squared. This is because the formula to calculate a person's BMI is:
# BMI = weight (kg) / (height(m ** 2))
# https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php
# https://stackoverflow.com/questions/36048713/3-arguments-calculating-bmi-python

print ('BMI is {}'.format (BMI))

# Prints out the resulting BMI in kg/m**2 (Kilograms per metre squared)