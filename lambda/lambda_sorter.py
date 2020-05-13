# instead of defining a function for each sorter {key}, just use the "anonymous" lambda function
# inplace.

# Sort alphabetically
presenters = [
    {"name": "Jason", "age": 51},
    {"name": "Susan", "age": 50},
    {"name": "Christopher", "age": 47},
]

# lambda is the function
# item is the parameter
# item["name"] is the return value
presenters.sort(key=lambda item: item["name"])
print("-- alphabetically --")
print(presenters)

# Sort by length of name (shortest to longest)
presenters.sort(key=lambda item: len(item["name"]))
print("-- length --")
print(presenters)

presenters.sort(key=lambda item: item["age"])
print("-- age --")
print(presenters)
