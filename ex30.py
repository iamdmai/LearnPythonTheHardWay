# ex30: Else and If

# Assign 30 to variable named people
people = 30

# Assign 40 the variable named cars
cars = 40

# Assign 15 to the variable named trucks
trucks = 15

# If 40 > 30 then print out "We should take the cars." which is True
if cars > people:
    print "We should take the cars."

# Else If cars is less than people which is not true we will print out
# "We should not take the cars."
elif cars < people:
    print "We should not takee the cars."

# Else: If none of the above statements are true, print out "We can't decide."
else:
    print "We can't decide."

# If 15 > 40 then print out "That's too many trucks." - False
if trucks > cars:
    print "That's too many trucks."

# Else-If 15 < 40 then print out "Maybe we could take the trucks." - True
elif trucks < cars:
    print "Maybe we could take the trucks."

# Else if none of the above statements are true print out "We still can't decide."
else:
    print "We still can't decide."

# If 30 > 15 print out "Alright, let's just take the trucks." - True
if people > trucks:
    print "Alright, let's just take the trucks."

# Else: if the above statement is false then print "Fine, let's stay home then."
else:
    print "Fine, let's stay home then."
