# Program that outputs whether or not today is a weekday.
# Author: Cormac Hennigan

import datetime # Import a module named datetime to work with dates as date objects.

weekNumber = datetime.datetime.today().weekday() 
# This equation gives us the weekday number that we are currently on as an integer from 0 to 6, ie. Monday is day
# number 0, tuesday is day number 1, wednesday is day number 2 etc.
# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
# https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday

if weekNumber < 5: # if the number generated is less than 5, then we are currently on a weekday
                    # ie. 0 - 4 = Monday - Tuesday
    print ("Yes, unfortunately today is a weekday.")
else:               # otherwise day 5 abd 6 are Saturday and Sunday
    print ("It is the weekend, yay!")