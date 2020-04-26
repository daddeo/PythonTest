def tally(text):
    count = {}
    for c in text:
        count[c] = 1 + count.get(c, 0)
    return count


# {'a': 7, 'b': 2, 'c': 2}
print(tally("aaabbaccaaa"))


def tally_v2(text, count):
    for c in text:
        count[c] = 1 + count.get(c, 0)
    return count


count_dict = {}
tally_v2("aaabbaccaaa", count_dict)
tally_v2("xyzaa", count_dict)
tally_v2("qrs", count_dict)
# {'a': 9, 'b': 2, 'c': 2, 'x': 1, 'y': 1, 'z': 1, 'q': 1, 'r': 1, 's': 1}
print(count_dict)

print(tally_v2("abc", {}))  # {'a': 1, 'b': 1, 'c': 1}
print(tally_v2("def", {}))  # {'d': 1, 'e': 1, 'f': 1}
print(tally_v2("xyz", {}))  # {'x': 1, 'y': 1, 'z': 1}

# ------------------------------------------------
# failed use of default value, since default values are only intialized and evaluated once
# when the function is first encountered. This default value is mutable and will not be
# intialized each time the function is evaluated.
def tally_v3(text, count={}):
    for c in text:
        count[c] = 1 + count.get(c, 0)
    return count


print(tally_v3("abc"))  # {'a': 1, 'b': 1, 'c': 1}
print(tally_v3("def"))  # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}
print(tally_v3("xyz", {}))  # {'x': 1, 'y': 1, 'z': 1}

# ------------------------------------------------
# same problem with a global as well

global_count = {}


def tally_v4(text, count=global_count):
    for c in text:
        count[c] = 1 + count.get(c, 0)
    return count


print(tally_v4("abc"))  # {'a': 1, 'b': 1, 'c': 1}
print(tally_v4("def"))  # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}
print(tally_v4("xyz", {}))  # {'x': 1, 'y': 1, 'z': 1}

# ------------------------------------------------
# solution is to use a immutable assignment and then create a new mutable object each time
def tally_v5(text, count=None):
    if count is None:
        # create a brand new, empty dictionary
        count = {}
    for c in text:
        count[c] = 1 + count.get(c, 0)
    return count


print(tally_v5("abc"))  # {'a': 1, 'b': 1, 'c': 1}
print(tally_v5("def"))  # {'d': 1, 'e': 1, 'f': 1}
print(tally_v5("xyz", {}))  # {'x': 1, 'y': 1, 'z': 1}
