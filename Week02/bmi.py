# bmi.py
# Calculates somebody's Body Mass Index (BMI).
# Author: Cormac Hennigan

Weight = int(input ('Enter weight (Kg): '))
Height1 = int(input ('Enter height (cm): '))   

 # Converts the height from centimeters to meters squared
Height2 = ((Height1 / 100))**2
BMI = round(Weight / Height2, 2)

print ('BMI is {}'.format (BMI))