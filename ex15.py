# ex15: Reading Files

# Lines 4-6 uses argv to get a filename
from sys import argv

script, filename = argv

# Line 9 where we use a new command open
txt = open(filename)

# Displays the text filename
print "Here's your file %r:" % filename
print txt.read()

# Close the file
txt.close()


# Prompts to ask for filename again
print "type the filename again:"

# Entering the name of the filename again
file_again = raw_input("> ")

# Opens file
txt_again = open(file_again)

# Print contents in file
print txt_again.read()


# Close the file
txt_again.close()
