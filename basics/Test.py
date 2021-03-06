# This is a base comment line
# there is no block comment like in Java and C++

"""
This is treated as documentation and not as a multi-line comment
"""

import math

print("hello!")

# Order of Prescendence: BODMAS rule:
# B(rackets) - (), [], {}
# O(rders) - x^2, sqrt
# D(ivide)
# M(ultiply)
# A(dd)
# S(ubtract)

# / is float division, // is integer division
print("5 / 2 = {}".format(5 / 2))  # 2.5
print("5 // 2 = {}".format(5 // 2))  # 2
print("8 + 2 * 3 = {}".format(8 + 2 * 3))  # 14, not 30
print("(8 + 2) * 3 = {}".format((8 + 2) * 3))  # this is 30, brackets are resolved first

# * is multiple, ** is raise to power
print("2 * 2 * 2 = {}".format(2 * 2 * 2))  # 8
print("2 ** 3 = {}".format(2 ** 3))  # 8

print("10 / 3 = {}".format(10 / 3))  # 3.33
print("10 // 3 = {}".format(10 // 3))  # 3
print("10 % 3 = {}".format(10 % 3))  # 1

# single or double quotations inside the other
print("Jason's laptop")
print("Jason's laptop")  # need to escape with '\' the middle single quote
print(
    'Jason\'s "Lenovo" laptop'
)  # need to escape the double quotes, but not the single quote since the string is surrounded by double quotes

print("Rum")  # Rum
print("Rum" + "Rum")  # RumRum
print(10 * "Rum")  # RumRumRumRumRumRumRumRumRumRum

# below print won't work unless escaped, but can use "r" telling Python it is a raw string and don't mess with it
# print("c:\test\path\")
print("c:\\test\\path\\")
print(r"c:\test\path")  # cannot have trailing \, "...path\", or Python will hork

#
# See the Python online documention under 7. Input and Output for more information of formatting
# https://docs.python.org/3/tutorial/inputoutput.html
# sprintf style formatters:
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
# https://www.geeksforgeeks.org/python-output-formatting/

year = 2016
event = "Referendum"
print(f"Results of the {year} {event}")  # 'Results of the 2016 Referendum'

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print(
    "{:-9} YES votes  {:2.2%}".format(yes_votes, percentage)
)  # ' 42572654 YES votes  49.67%'

# convert any value to a string with the repr() or str()
s = "Hello, world."
print(str(s))  # Hello, world.
print(repr(s))  # 'Hello, world.'
print(str(1 / 7))  # 0.14285714285714285

# The value of pi is approximately 3.142.
print(f"The value of pi is approximately {math.pi:.3f}.")

# : is useful for lining up columns
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678
table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
for name, phone in table.items():
    print(f"{name:10} ==> {phone:10d}")

# Other modifiers can be used to convert the value before it is formatted.
# '!a' applies ascii(), '!s' applies str(), and '!r' applies repr()
animals = "eels"
print(f"My hovercraft is full of {animals}.")  # My hovercraft is full of eels.
print(f"My hovercraft is full of {animals!r}.")  # My hovercraft is full of 'eels'.

print("{0} and {1}".format("spam", "eggs"))  # spam and eggs
print("{1} and {0}".format("spam", "eggs"))  # eggs and spam

# This spam is absolutely horrible.
print(
    "This {food} is {adjective}.".format(food="spam", adjective="absolutely horrible")
)

# The story of Bill, Manfred, and Georg.
print("The story of {0}, {1}, and {other}.".format("Bill", "Manfred", other="Georg"))

# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
print("Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}".format(table))

# this can be done by using the ‘**’ notation
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table))

# 1   1    1
# 2   4    8
# 3   9   27
# 4  16   64
# 5  25  125
# 6  36  216
# 7  49  343
# 8  64  512
# 9  81  729
# 10 100 1000
for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x * x, x * x * x))

x = 1
y = 5.33
print("X: %02d, Y: %5.2f" % (x, y))  # X: 01, Y:  5.33

# print integer and float value
# Geeks :  1, Portal :  5.33
print("Geeks : % 2d, Portal : % 5.2f" % (1, 05.333))

# print integer value
# Total students :  240, Boys :  120
print("Total students : % 3d, Boys : % 2d" % (240, 120))

# print octal value
# '    031'
print("% 7.3o" % (25))

# print exponential value
# ' 3.561E+02'
print("% 10.3E" % (356.08977))

# Geeks :12, Portal :    0.55
print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 00.546))
# Second argument:  11, first one:   47.42
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))
# Geeks:   453,  Portal:    59.06
print("Geeks: {a:5d},  Portal: {p:8.2f}".format(a=453, p=59.058))

# Geeks: 4127; For: 4098; Geeks: 8637678
# using format() in dictionary
# {0 is for tab and then [] is the key in tab
tab = {"geeks": 4127, "for": 4098, "geek": 8637678}
print("Geeks: {0[geeks]:d}; For: {0[for]:d}; Geeks: {0[geek]:d}".format(tab))

# I love GeeksForGeeks computer Portal
# using format() in dictionary
data = dict(fun="GeeksForGeeks", adj="Portal")
print("I love {fun} computer {adj}".format(**data))


# ------------------------------------------------------------------------------------------------
print("-----")
# ------------------------------------------------------------------------------------------------

x = 2
print("x = {}".format(x))  # 2
x = 2 + 3
print("x = {}".format(x))  # 5
x += 5
print("x = {}".format(x))  # 10
y = 3
print("y = {}".format(y))  # 3
print("x * y = {}".format(x * y))  # 30
x, y = 7, 3
print("x = {}, y = {}".format(x, y))

name = "Jimbo"
print(name)  # simple assignment
print(name + " is a ?")  # simple string concatenation
# Jimbo is from 0 to 4, where J is 0, i is 1, m is 2, b is 3, o is 4
# also can be done in reverse as
# Jimbo where J is -5, i is -4, m is -3, b is -2, o is -1
print(name[0])  # [J]imbo, 0 relative strings
print(name[4])  # Jimb[o]
print(name[-1])  # Jimb[o]
print(name[-5])  # [J]imbo
# print a range of characters, [{start}:{end}], if {end} is not defined then to end of string
# NOTE: {end} is not inclusive with characters from {start} to {end - 1} being included
print(name[0:2])  # Ji
print(name[0:3])  # Jim
print(name[3:])  # bo
print(name[:3])  # Jim
print(name[3:100])  # bo, even though 100 is WAY too big it will stop
# strings in Python are immutable (cannot change the value), so the following would not work
# name[3:] = "bob"
# name[0] = "T"
# but you could get around it by doing...
newName = "T" + name[1:]
print(newName)  # Timbo
newName = name[:3] + "R" + name[4:] + "b"
print(newName)  # JimRob
# show length of string
print(len(newName))  # 6

# list of values, lists are mutable (meaning the value can be changed)
numbers = [25, 12, 36, 95, 14]  # 25 at index 0, 12 at index 1, ..., 14 at index 4
print(numbers[0])  # 25
print(numbers[-5])  # 25
print(numbers[4])  # 14
print(numbers[-1])  # 14
print(numbers[2:])  # [36,95,14]

values = ["Text", 10, 25.5]  # string, integer, float
print(values)
# can combine lists
multiList = [numbers, values]
print(multiList)
# working with lists
# NOTE: when using ".", if function list does not pop up simply press CTRL + SPACE on numbers
numbers.append(63)  # [25, 12, 36, 95, 14, 63]
print(numbers)
numbers.insert(3, 77)
print(numbers)  # [25, 12, 36, 77, 95, 14, 63]
numbers.insert(6, 99)
print(numbers)  # [25, 12, 36, 77, 95, 14, 99, 63]
numbers.remove(99)  # delete by value
print(numbers)  # [25, 12, 36, 77, 95, 14, 63]
numbers.insert(6, 99)
print(numbers)  # [25, 12, 36, 77, 95, 14, 99, 63]
numbers.pop(6)  # delete by index
print(numbers)  # [25, 12, 36, 77, 95, 14, 63]

# stack based operation pop() removes last element
numbers.pop()
print(numbers)  # [25, 12, 36, 77, 95, 14]
numbers.pop()
print(numbers)  # [25, 12, 36, 77, 95]
numbers.append(14)
numbers.append(63)
print(numbers)  # [25, 12, 36, 77, 95, 14, 63]

del numbers[4:]  # delete from index 3 (value = 77) to the end
print(numbers)  # [25, 12, 36, 77]
numbers = [25, 12, 36, 77, 95, 14, 63]
del numbers[1:4]  # deletes values 12, 36, 77 (indexes 1, 2, 3, not 4)
print(numbers)  # [25, 95, 14, 63]

# add multiple values
numbers.extend([12, 36, 77])
print(numbers)  # [25, 95, 14, 63, 12, 36, 77]

# math functions
min(numbers)
print("min(numbers) = {}".format(min(numbers)))  # 12
max(numbers)
print("max(numbers) = {}".format(max(numbers)))  # 95
sum(numbers)
print("sum(numbers) = {}".format(sum(numbers)))  # 322
numbers.sort()
print("sorted numbers = {}".format(numbers))  # [12, 14, 25, 36, 63, 77, 95]

# Tuple (immutable) is like a list (mutable) -- are faster than reading from lists
tuple1 = (21, 36, 99, 52, 21)
print(tuple1)  # (21, 36, 99, 52, 21)
print(tuple1[2])  # 99
# cannot do
# tuple1[2] = 10
print(tuple1.count(21))  # 2

# Set, a list that doesn't maintain it's sequence and has no duplicate values
set1 = {22, 25, 14, 21, 5}
print(set1)  # {5, 14, 21, 22, 25}
set1 = {25, 12, 98, 63, 75, 98}
print(set1)  # {98, 75, 12, 25, 63}
# cannot be indexed like a list, so the following will fail
# set1[0]

# Dictionary, aka map
data = {1: "One", 2: "Two", 4: "Four"}
print(data)  # {1: 'One', 2: 'Two', 4: 'Four'}
print(data[4])  # Four
print(data[1])  # One
try:
    print(data[3])  # does not exist, KeyError
except KeyError as e:
    print("Not Found")
finally:
    pass
print(data.get(1))  # One
print(data.get(3, "Not Found"))  # does not exist, no output

# construct a dictionary from two lists
keys = ["Apple", "Plum", "Banana", "Orange"]
values = ["Red", "Purple", "Yellow", "Orange"]
fruits = dict(zip(keys, values))
print(
    fruits
)  # {'Apple': 'Red', 'Plum': 'Purple', 'Banana': 'Yellow', 'Orange': 'Orange'}
print(fruits["Plum"])  # Purple
try:
    print(fruits["Blackberry"])  # Keyerror
except KeyError as e:
    print("Not Found")
finally:
    pass
fruits["Blackberry"] = "Black"
print(
    fruits
)  # {'Apple': 'Red', 'Plum': 'Purple', 'Banana': 'Yellow', 'Orange': 'Orange', 'Blackberry': 'Black'}
print(fruits["Blackberry"])  # Black
del fruits["Blackberry"]
del fruits["Plum"]
print(fruits)  # {'Apple': 'Red', 'Banana': 'Yellow', 'Orange': 'Orange'}

languages = {
    "JS": "Atom",
    "CS": "VS",
    "Python": ["PyCharm", "Sublime"],
    "Java": {"JSE": "Netbeans", "J2EE": "Eclipse"},
}
# {'JS': 'Atom', 'CS': 'VS', 'Python': ['PyCharm', 'Sublime'], 'Java': {'JSE': 'Netbeans', 'J2EE': 'Eclipse'}}
print(languages)
print(languages["JS"])  # Atom
print(languages["Python"])  # ['PyCharm', 'Sublime']
print(languages["Python"][1])  # Sublime
print(languages["Java"])  # {'JSE': 'Netbeans', 'J2EE': 'Eclipse'}
print(languages["Java"]["J2EE"])  # Eclipse

# type quit to exit help
# help()
# help('topics')
# help('LISTS')

# more on variables
number = 5
print(id(number))  # print address of number
a = 2
b = a
# both point to the same address 1885665216, since they both have the same value (increased memory efficiency)
print("a address {}, b address {}".format(id(a), id(b)))
# address is not based on the name, but the value
print("a address {}, address of value 2 {}".format(id(a), id(2)))
k = 2
# a = 1885665216, value 2 = 1885665216, k = 1885665216
print("a = {}, value 2 = {}, k = {}".format(id(a), id(2), id(k)))
a = 9
k = a
# a = 1885665328, value 2 = 1885665216, b = 1885665216, k = 1885665328
print("a = {}, value 2 = {}, b = {}, k = {}".format(id(a), id(2), id(b), id(k)))

b = 2.2
type(a)
type(b)
# a = <class 'int'>, b = <class 'float'>
print("a = {}, b = {}".format(type(a), type(b)))

# BEFORE -- a = <class 'int'>,9, b = <class 'float'>,2.2, k=<class 'int'>,9
print(
    "BEFORE -- a = {},{}, b = {},{}, k={},{}".format(type(a), a, type(b), b, type(k), k)
)
a = int(b)
b = str(b)
k = float(a)
# AFTER -- a = <class 'int'>,2, b = <class 'str'>,2.2, k=<class 'float'>,2.0
print(
    "AFTER -- a = {},{}, b = {},{}, k={},{}".format(type(a), a, type(b), b, type(k), k)
)
b = float(b)
# could also use !=, <=, >=
isLess = k < b
isGreater = k > b
isEqual = k == b
# k=2.0, b=2.2, k < b: True, k > b: False, k == b: False
print(
    "k={}, b={}, k < b: {}, k > b: {}, k == b: {}".format(
        k, b, isLess, isGreater, isEqual
    )
)
print(int(True))  # 1
print(int(False))  # 0

# types
list1 = [25, 12, 82]
print("type(list1): {}".format(type(list1)))
set1 = {25, 12, 82}
print("type(set1): {}".format(type(set1)))
tuple1 = (25, 12, 82)
print("type(tuple1): {}".format(type(tuple1)))
text = "Text"
print("type(text): {}".format(type(text)))
range1 = range(10)
print("type(range1): {}".format(type(range1)))
print(range1)  # range(0, 10)
print(list(range1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range1 = list(range(2, 11, 2))
print(range1)  # [2, 4, 6, 8, 10]

d = {"apple": "red", "banana": "yellow", "orange": "orange", "blackberry": "black"}
print(
    d
)  # {'apple': 'red', 'banana': 'yellow', 'orange': 'orange', 'blackberry': 'black'}
print(d.keys())  # dict_keys(['apple', 'banana', 'orange', 'blackberry'])
print(d.values())  # dict_values(['red', 'yellow', 'orange', 'black'])
print("d['banana']: {}".format(d["banana"]))  # d['banana']: yellow
print("d.get('orange'): {}".format(d.get("orange")))  # d.get('orange'): orange

x = 3
print("x = {}".format(x))  # 3
x += 3
print("x = {}".format(x))  # 6
x *= 3
print("x = {}".format(x))  # 18
x //= 3
print("x = {}".format(x))  # 6
x -= 3
print("x = {}".format(x))  # 3

# swapping values
a, b = 5, 6
print("a,b = {},{}".format(a, b))  # 5,6

temp = a
a = b
b = temp
print("a,b = {},{}".format(a, b))  # 6,5

a = a + b
b = a - b
a = a - b
print("a,b = {},{}".format(a, b))  # 5,6

# uses ROT_TWO(), swaps the 2 top-most stack elements
a, b = b, a
print("a,b = {},{}".format(a, b))  # 6,5

# XOR bits
a = a ^ b
b = a ^ b
a = a ^ b
print("a,b = {},{}".format(a, b))  # 5,6

# bitwise operators
print(~12)
print(12 & 13)
print(12 | 13)
print(12 ^ 13)
print(20 << 2)
print(20 >> 2)

# some string functions
sentence = "My dog is named Fluffy"
print(sentence.upper())
print(sentence.lower())
print(sentence.count("f"))
print(sentence.count("is"))
print(sentence.capitalize())

first_name = "John"
last_name = "Doe"
print("Hello, " + first_name + " " + last_name)
print("Hello, {} {}".format(first_name, last_name))
print("Hello, {0} {1}".format(first_name, last_name))
print("Hello, {1} {0}".format(first_name, last_name))
# f being for format
print(f"Hello, {first_name} {last_name}")


def test_num(num):
    if num in (1, 2, 8, 9):
        print("special number")
    else:
        print("not special number")


test_num(5)
test_num(1)
test_num(7)
test_num(8)
