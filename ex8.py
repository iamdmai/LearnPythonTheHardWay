# ex8: Printing, Printing

# Print the variables
formatter = "%r %r %r %r"

# Format the numbers 1-4
print formatter % (1, 2, 3, 4)

# Format the string 1-4 variables
print formatter % ("one", "two", "three", "four")

# Format True or False
print formatter % (True, False, False, True)

# Format the strings
print formatter % (formatter, formatter, formatter, formatter)

# Format the 4 strings
print formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight."
)
