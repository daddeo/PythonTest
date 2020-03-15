# This is a base comment line
# there is no block comment like in Java and C++

"""
This is treated as documentation and not as a multi-line comment
"""

print("hello!")

# Order of Prescendence: BODMAS rule:
# B(rackets) - (), [], {}
# O(rders) - x^2, sqrt
# D(ivide)
# M(ultiply)
# A(dd)
# S(ubtract)

# / is float division, // is integer division
print("5 / 2 = {}".format(5 / 2)) # 2.5
print("5 // 2 = {}".format(5 // 2)) # 2
print("8 + 2 * 3 = {}".format(8 + 2 * 3)) # 14, not 30
print("(8 + 2) * 3 = {}".format((8 + 2) * 3)) # this is 30, brackets are resolved first

# * is multiple, ** is raise to power
print("2 * 2 * 2 = {}".format(2 * 2 * 2)) # 8
print("2 ** 3 = {}".format(2 ** 3)) # 8

print("10 / 3 = {}".format(10 / 3)) # 3.33
print("10 // 3 = {}".format(10 // 3)) # 3
print("10 % 3 = {}".format(10 % 3)) # 1

# single or double quotations inside the other
print("Jason's laptop")
print('Jason\'s laptop') # need to escape with '\' the middle single quote
print("Jason's \"Lenovo\" laptop") # need to escape the double quotes, but not the single quote since the string is surrounded by double quotes

print("Rum") # Rum
print("Rum" + "Rum") # RumRum
print(10 * "Rum") # RumRumRumRumRumRumRumRumRumRum

# below print won't work unless escaped, but can use "r" telling Python it is a raw string and don't mess with it
#print("c:\test\path\")
print("c:\\test\\path\\")
print(r"c:\test\path") # cannot have trailing \, "...path\", or Python will hork

