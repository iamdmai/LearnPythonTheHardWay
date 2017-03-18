# ex6: Strings and Text

# Defining strings as variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

# Test print to see if variables are correct
print x
print y

# Print a string with a variable string x
print "I said: %r." % x

# Print a string with a variable string y
print "I also said: '%s'." % y

# Assign a false boolean variable to variable 'hilarious'
hilarious = False

# Assian the string with an unevaluated formatting character to 'joke evaluation'
joke_evaluation = "Isn't that joke so funny?! %r"

# Print "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

# Assign string to variable 'w'
w = "This is the left side of ..."

# Assign string to variable 'e'
e = "a string with a right side."

# Print Concatenation of string variables w and e
print w + e
