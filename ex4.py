# ex4: Variables And Names

# Defining the variables
cars = 100
space_in_a_car = 4.0
drivers  = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


# Prints out number of available cars
print "There are", cars, "cars available."

# Prints out number of available drivers
print "There are only", drivers, "drivers available."

# Prints out the number of cars not driven
print "There will be", cars_not_driven, "empty cars today."

# Prints out the number of people we can transport by carpool
print "We can transport", carpool_capacity, "people today."

# Prints out the number of passengers that used carpool
print "We have", passengers, "to carpool today."

# Prints out the average number of passengers in each car.
print "We need to put about", average_passengers_per_car, "in each car."
