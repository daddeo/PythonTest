# Notes about sort
#
# {sort} can automatically handle primitive types and strings
# if we need to do anything complex we need to tell sort how to sort
# in this case we just need to specify whether to sort by name or by age
#
# the {key} parameters allows you to pass in a function to call for each list
# element before it compares items for sorting. Providing the item to compare, for
# example age or name


def name_sorter(item):
    return item["name"]


def age_sorter(item):
    return item["age"]


presenters = [
    {"name": "Jason", "age": 51},
    {"name": "Susan", "age": 50},
    {"name": "Christopher", "age": 47},
]
presenters.sort(key=name_sorter)
print(presenters)
presenters.sort(key=age_sorter)
print(presenters)
