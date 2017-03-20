# ex34: Accessing Elements of lists

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

# The animal at 1.
# The first(1st) animal is at 0 and is a bear.
print animals[0]

# The third (3rd) animal.
# The third (3rd) animal is at 2 and is a peacock.
print animals[2]

# The first (1st) animal.
# The first (1st) animal is at 0 and is a bear.
print animals[0]

# The animal at 3.
# The fourth (4th) animal is at 3 and is a kangaroo.
print animals[3]

# The fifth (5th) animal.
# The fifth (5th) animal is at 4 and is a whale.
print animals[4]

# The animal at 2.
# The third (3rd) animal is at 2 and is a peacock.
print animals[2]

# The sixth (6th) animal.
# The sixth (6th) animal is at 5 and is a platypus.
print animals[5]

# The animal at 4.
# The fifth (5th) animal is at 4 and is a whale.
print animals[4]


def printAnimals(i):
    if i == 1:
        numToString = "1st"
    elif i == 2:
        numToString = "2nd"
    elif i == 3:
        numToString = "3rd"
    else:
        numToString = str(i) + "th"

    print "The %s animal is at %d and is a %s" %(numToString, i - 1, animals[i-1])
    print "The animal at %d is the %s animal and is a %s" % (i -1, numToString, animals[i-1])

for i in range(1,7):
    printAnimals(i)
