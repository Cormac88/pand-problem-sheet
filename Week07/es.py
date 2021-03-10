# Program that reads in a text file and outputs the number of e's it contains.
# Aothor: Cormac Hennigan

with open ("moby-dick.txt", "r") as f:  # Opens the text file and reads its contents:
    
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