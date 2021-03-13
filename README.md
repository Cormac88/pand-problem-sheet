# pand-problem-sheet

## Week 2: Program that calculates somebody's Body Mass Index (BMI) called bmi.py
    I used the reference:
        > https://stackoverflow.com/questions/36048713/3-arguments-calculating-bmi-python

The calculation was in feet, inches and pounds so I re wrote the code in my own way and with cm, m and kg

## Week 3: program that takes asks a user to input a string and outputs every second letter in reverse order called secondstring.py
    I used the reference:
        > https://stackoverflow.com/questions/25375794/how-to-reverse-the-order-of-letters-in-a-string-in-python

This code only reversed the code so I changed the 1 to a 2 so that it would only print every second letter

## Week 4: program that inputs any positive integer and if the value is even, divide it by two, but if it is odd, multiply it by three and add one. The Program ends when the current value is 1.
    I used the reference:
        > https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence

This code had it's first statement as:
 if x < 1:
       return []
    while x > 1:

I changed this to:
 while number != 1:

 This makes the code a bit tidier as it has less lines.

## Week 5: Program that outputs whether or not today is a weekday.
    I used the reference:
        > https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

## Week 6: Program that takes a positive floating-point number as input and outputs an approximation of its square root.
    I used the references:
        > https://www.school-for-champions.com/algebra/square_root_approx.htm#.YEEjBWj7Qaa
        > https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method
        > https://stackoverflow.com/questions/52792987/unused-variable-in-a-for-loop

## Week 7: Program that reads in a text file and outputs the number of e's it contains.
    I used the references:
        > https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
        > https://appdividend.com/2019/01/22/python-sys-argv-tutorial-command-line-arguments-example/
    
    Please note that an arguement must be passed through the command line of this program. Add the text file that 
    you want to have analysed after the program name. Eg. python .\es.py .\moby-dick.txt

## Week 8: Program that reads in a text file and outputs the number of e's it contains.
    I used the references:
        > https://www.geeksforgeeks.org/numpy-linspace-python/
        > https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
        > https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python
        > https://www.w3schools.com/python/matplotlib_markers.asp
        > https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html

    Something to note in this plot is that the reason that the y-axis goes up to 64 is beacuse the x ranges from 0-4,
    thus the maximum value is 4 ** 3 which is 64.