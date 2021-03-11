# Program that reads in a text file and outputs the number of e's it contains.
# Aothor: Cormac Hennigan

import sys  # import the module sys to enable us to manipulate different parts of the Python runtime environment.

filename = sys.argv[1] 

# This variable "filename" is going to be any text file that the user wants to input to  this program. sys.argv is
# is the list of all the command-line arguments. sys.argv[0] is this program, es.py because it is element 0.
# sys.argv[1] is the second argument that the user enters in the command line. ie. python .\es.py .\moby-dick.txt.
# If we wanted to use a third argument in the command line, then we would have another varibale called sys.argv[2].
# In this case the user would type something like python .\es.py .\moby-dick.txt. \moby-dick2.txt. and we would
# have to put that third element somewhere into the program. 
# https://appdividend.com/2019/01/22/python-sys-argv-tutorial-command-line-arguments-example/

with open (filename, "r") as f:  # Opens the text file and reads its contents:
    
    # Using the formula: n = String.count(word), where word is the string, and count() returns the number 
    # of occurrences of word in this String, the below equation can be written.

    data = f.read()

    # The variable "data" here reads the txt file.
                       
    occurrences = data.count("e")
    
    # Since the variable "data" in this case is the same thing as "String" in the above formula, we raplace "word"
    # with "e" to get the number of e's in the txt file.
    
    # This solution was derived from  https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/

print (occurrences)

# Made an assumption that the client only wanted the lower case e's counted because this information
# was not specified. If they had wanted upper and lower case they would have specified this information,
# but since I was only told to "write a program that reads in a text file and outputs the number of e's 
# it contains.", I think that it is safe to assume that the cline only wants the lower case e's