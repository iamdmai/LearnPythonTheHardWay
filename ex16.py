# ex16: Reading and Writing Files
from sys import argv

script, filename = argv

# Erase the filename or give you option to choose to do it or not
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# Open the file by filename entered by user
print "Opening the file..."
target = open(filename, 'w')

# Empties the file
print "Truncating the file. Goodbye!"
target.truncate()

# Asking user for input to insert in file
print"Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Write('variable') -- Writes what's in variable to file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file when done
print "And finally, we close it."
target.close()
