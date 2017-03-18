# ex5: More Variables And Printing


name = 'Zed A. Shaw'
age = 35.0 # not a lie
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# convert inches and pounds
# centimeters conversion
# kilograms conversion

centimeters = 2.54 * height
kilograms = .453592 * weight

# Introducing who we are talking about
print "Let's talk about %s." % name

# Height in inches
print "He's %d inches tall" % height

# Height in centimeters
print "He's %d centimeters tall" % centimeters

# Weight in lbs
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."

# Weight in kilograms
print "He's %d kilograms heavy." % kilograms

# Describe there
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % (teeth)

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (age, height, weight, (age + height + weight))
