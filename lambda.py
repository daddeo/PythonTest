# Lambda Functions
# A lambda is an anonymous function and an anonymous function is a function that is defined without a name.
# https://www.programiz.com/python-programming/anonymous-function


import datetime

# -------------------------------------------------------------------

# this is...
def double(x):
    return x * 2


# nearly the same as this...
double = lambda x: x * 2

# 10
print(double(5))

# -------------------------------------------------------------------

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

# [4, 6, 8, 12]
print(new_list)

# -------------------------------------------------------------------

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

# [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)

# -------------------------------------------------------------------

people = [
    {"name": "John", "id": 1},
    {"name": "Bill", "id": 4},
    {"name": "Sandra", "id": 2},
    {"name": "Jennifer", "id": 3},
]

# {'name': 'Bill', 'id': 4}
# {'name': 'Sandra', 'id': 2}
for person in filter(lambda i: i["id"] % 2 == 0, people):
    print(person)

# -------------------------------------------------------------------

items = [15, 6, 1, 8]
# 1
# 6
# 8
# 15
for i in sorted(items):
    print(i)

# 15
# 8
# 6
# 1
for i in sorted(items, reverse=True):
    print(i)

# items.sort(key=lambda s: s[::-1])
# print(items)

# -------------------------------------------------------------------
# sort() — A method that modifies the list in-place
# sorted() — A built-in function that builds a new sorted list from an iterable
#
# lambda r:r[0] is an anonymous function with a single argument, r which would
# in this case was a list, e.g.: [datetime.datetime(2016, 7, 10, 0, 58, 54), "2.59"]
#
# the lambda then returns the first element of the list, in this case the element
# that corresponds to the datetime object. This is then used as the key for the sort.

list = [
    [datetime.datetime(2016, 7, 10, 0, 58, 54), "2.59"],
    [datetime.datetime(2016, 7, 10, 0, 58, 14), "2.68"],
    [datetime.datetime(2016, 7, 10, 0, 57, 54), "2.61"],
    [datetime.datetime(2016, 7, 10, 0, 58, 34), "2.61"],
]
list.sort(key=lambda r: r[0])
print(list)

# [[datetime.datetime(2016, 7, 10, 0, 57, 54), '2.61'], [datetime.datetime(2016, 7, 10, 0, 58, 14), '2.68'], [datetime.datetime(2016, 7, 10, 0, 58, 34), '2.61'], [datetime.datetime(2016, 7, 10, 0, 58, 54), '2.59']]

# -------------------------------------------------------------------

items = [5, 10, 15]
items[1]
# 10
data = dict(enumerate(items))
print(data)

# {0: 5, 1: 10, 2: 15}
