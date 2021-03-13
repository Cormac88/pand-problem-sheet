# Displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4].
# Author: Cormac Hennnigan

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 100) 

# Here we define the values for the range on the x-axis. The The numpy.linspace() function returns
# number spaces evenly with respect to the interval. There are 5 parameters: start, stop, num, restep, and dtype.
# 
# start  : [optional] start of interval range. By default start = 0
# stop   : end of interval range
# restep : If True, return (samples, step). By deflut restep = False
# num    : [int, optional] No. of samples to generate
# dtype  : type of output array
#
# By setting num to 100, we have 100 dots to make the graph look better.
# https://www.geeksforgeeks.org/numpy-linspace-python/

y1 = x 
y2 = x ** 2 
y3 = x ** 3

# The above are each of the functions, f(x) = x, g(x) = x ** 2 and h(x) = x ** 3
# These are all going to be the y-axis values

plt.title ("Functions", fontsize = 20)
plt.xlabel ("X", fontsize = 20) 
plt.ylabel ("Y", fontsize = 20) 

# The above functions are to set the title for the graph and the x and y labels. I used some Matplotlib
# functions here to change the fontsizes.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html

plt.plot (x,y1, 'g.', label = "f(x) = x") # Plots f(x)=x
plt.plot (x,y2, 'y.', label = "g(x) = x**2") # Plots g(x)=x2
plt.plot (x,y3, 'b.', label = "h(x) = x**3") #Plots h(x)=x3
plt.legend(loc = 'upper left' , fontsize = 15) # Adds a legend
plt.grid() # draws a grid on the plot:
# https://www.w3schools.com/python/matplotlib_markers.asp
# https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python
# adding a "." after the colour label gives us points.

plt.ylim(0,70) # Sets the limit on the y-axis to 70 to make it neater. 
                #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html

plt.show() # The show function is used to display all 3 plots