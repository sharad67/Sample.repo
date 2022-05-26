
x, y = 1, 2
print(x,y,)

# Formatted strings
# The special operator % lets you create formatted output. 
# It takes two operands: a formatted string and a value. 
# The value can be a single value, a tuple of values or a dictionary of values.
# For example:
print("pi=%s" % "3.14159")
# The formatted string has a conversion specifiers that also uses the special characters %s. 
# This conversion specifier tells Python how to convert the value. 
# Here %s means convert the value to a string.
# In fact, you could even type:
print("pi=%s" % 3.14159)
# to be more generic, you could include the value within a tuple:
print("pi=%s" % (3.14159))
# and print 2 values:
print("%s=%s" % ("pi", 3.14159))
# The width option is a positive integer specifying the minimum field width. If the converted value is shorter than width, spaces are added on left or right

# if you have a string with endline characters, 
# %s would actually show stuff on new lines while 
# %r would just give the output as \n and also keep the quotes intact.
string = "Hello\nworld"
print("Example: %s" % string)
print("Example: %r" % string)

print("(%10s)" %  "example") 
print("(%-10s)" %  "example")
# Specific number of digits with the prec option
# prec is a dot (.) followed by a positive integer specifying the precision. Note that use the %f conversion specifier here:
print("%.3f" %  3.14159)
# The replacement field {}
x = "example"
print("{0} {1}".format("The", x))
print("{first} {second}".format(first="The", second=x))
print("{0} {second} {1}".format("The", x, second="second"))
# print("{0} {second} {2}".format("The", second="second", x))
# Note that index argument should be provided before the name argument. This does not work:
d = {"first":"The", "second": x}
print("{0[first]} {0[second]} {1}".format(d, "with dictionary"))

import math
print("{0.pi}".format(math))

variable = "some value"
print(f"this is a string {variable}")

rankings = {"Gonzaga": 31, "Baylor": 28, "Michigan": 25, "Illinois": 24, "Houston": 21}
for team, score in rankings.items():
    print(f"{team:10} ==> {score:10d}")

from string import Template
print(Template("I love to learn with $name!").substitute(name="freeCodeCamp"))


