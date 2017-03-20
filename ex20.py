# ex20: Functions and Files

# Import argv variables from the sys module
from sys import argv

# Assign the two variables to the first and second arguments
script, input_file = argv

# Define a function that is called print_all
# Description: Print the whole contents of a file
def print_all(f):
  print f.read()

# Define a function called rewind to go vacj to the first byte of the file
def rewind(f):
  f.seek(0)

# Define a function called print_a_line to print a line of the file
def print_a_line(line_count, f):
  print line_count, f.readline()

# Open a file
current_file = open(input_file)

print "First let's print the whole file:\n"

# Print out whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# Call the rewind function to go back to the beginning of the file
rewind(current_file)

print "Let's print three lines:"

# Set current line to 1 and print the current line
current_line = 1
print_a_line(current_line, current_file)

# Increase current line by one and print the current line
current_line = current_line + 1
print_a_line(current_line, current_file)

# Increase current line by one and print the current line
current_line = current_line + 1
print_a_line(current_line, current_file)
