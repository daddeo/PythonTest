# str() calls __str__()

s = "Hello, Geeks."
# Hello, Geeks.
print(str(s))
# 0.18181818181818182
print(str(2.0 / 11.0))

# repr() calls __repr__()

s = "Hello, Geeks."
# 'Hello, Geeks.'
print(repr(s))
# 0.18181818181818182
print(repr(2.0 / 11.0))

# Following are differences:
#
# str() is used for creating output for end user while repr() is mainly used for debugging and development.
# repr’s goal is to be unambiguous and str’s is to be readable. For example, if we suspect a float has a
# small rounding error, repr will show us while str may not.
#
# repr() compute the “official” string representation of an object (a representation that has all
# information about the object) and str() is used to compute the “informal” string representation of an
# object (a representation that is useful for printing the object).
#
# The print statement and str() built-in function uses __str__ to display the string representation of
# the object while the repr() built-in function uses __repr__ to display the object.
#
# In Summary:
# str() -- Make object readable, Generate output to end user
# repr() -- Required code that reproduces object, Generate output for developer
#

import datetime

today = datetime.datetime.now()

# Prints readable format for date-time object
# str() displays today’s date in a way that the user can understand the date and time.
# 2020-05-10 22:39:41.190935
print(str(today))

# prints the official format of date-time object
# repr() prints “official” representation of a date-time object (means using the “official” string
# representation we can reconstruct the object).
# datetime.datetime(2020, 5, 10, 22, 39, 41, 190935)
print(repr(today))


# Python to demonstrate writing of __repr__ and __str__ for user defined classes
# A user defined class to represent Complex numbers
class Complex:
    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return "Rational(%s, %s)" % (self.real, self.imag)

    # For call to str(). Prints readable form
    def __str__(self):
        return "%s + i%s" % (self.real, self.imag)


# Driver program to test above
t = Complex(10, 20)

# 10 + i20
print(str(t))  # Same as "print t"
# Rational(10, 20)
print(repr(t))
