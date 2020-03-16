# values must be of the same type, unlike lists
# do have fixed sizes, can be expanded or shrunk dynamically
# see array_value_sizes.png for details on space requirements

from array import *

values = array('u', ['a','e','i','o','u']) # unsigned characters
for i in range(len(values)):
    print("{},".format(values[i]), end="")
print()
print("-----")

values = array('I', [5,9,8,4,2]) # unsigned integers
print(values) # array('I', [5, 9, 8, 4, 2])
values.reverse()
print(values) # array('I', [2, 4, 8, 9, 5])
print("-----")

values = array('i', [5,9,-8,4,2]) # signed integers
print(values) # array('i', [5, 9, -8, 4, 2])
print(values.buffer_info()) # tuple of (address, size) --> (30347232, 5)
print(values.typecode) # i
print(values[1]) # 9
for i in values:
    print("{},".format(i), end="")
print()
for i in range(len(values)):
    print("{},".format(values[i]), end="")
print()
print("-----")

# says I don't know the new values, but take them from n where n iterates over values
newValues = array(values.typecode, (n for n in values))
print("newValues = ", end="")
for i in newValues:
    print("{},".format(i), end="")
print()
print("-----")

from math import pow
newValues = array(values.typecode, (int(pow(n,2)) for n in values))
sortedValues = array(newValues.typecode, sorted(newValues))
sortedList = sorted(newValues)
print("newValues = ", end="")
for i in newValues:
    print("{},".format(i), end="")
print()
print(sortedValues)
print(sortedList)
print("-----")

