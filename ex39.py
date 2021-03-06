# ex39: Dictionaries, Oh Lovely Dictionaries

# Create a mapping of state to abbreviation
states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
  'CA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# Print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# Do it by using the state then cities dict
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# Print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
  print "%s is abbreviated %s" % (state, abbrev)

# Print every city in state
print '-' * 10
for abbrev, city in cities.items():
  print "%s has the city %s" % (abbrev, city)

# Now do both at the same time
print '-' * 10
for state, abbrev in states.items():
  print "%s is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# Safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

city = cities.get("TX", "Does not Exist")
print "The city for the state 'TX' is %s" % city

# Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

# Create a mapping of province to abbreviation
canada_province = {
    'Alberta' = 'AB'
    'British Columbia' = 'BC'
    'Ontario' = 'ON'
    'Quebec' = 'QC'
}

canada_capitals = {
    'AB' = 'Edmonton'
    'BC' = 'Victoria'
    'ON' = 'Toronto'
    'QC' = 'Quebec City'

}

print '-' * 10
for prov, abbr in canada_province.items():
    print "%s has the city %s" % (prov, abbr)

print '-' * 10
canada_abbrevs = {values: keys for keys, values in canada_province.items()}
for abbrev, prov in canada_abbrevs.items():
    print "%s is abbreviated %s and has city %s" % (abbrev, prov)

print '-' * 10
for abbrev, capitals in canada_capitals.items():
    print "%s is abbreviated %s and has city %s" % (canada_province, canada_capitals[abbrev])
