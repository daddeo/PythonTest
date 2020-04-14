import re

"""
Suppose you are writing a poker program where a player’s hand is represented as
a 5-character string with each character representing a card, “a” for ace, 
“k” for king, “q” for queen, “j” for jack, “t” for 10, and “2” through “9”
representing the card with that value.

To see if a given string is a valid hand, one could do the following:
"""


def displaymatch(match):
    if match is None:
        return None
    return "<Match: %r, groups=%r>" % (match.group(), match.groups())


valid = re.compile(r"^[a2-9tjqk]{5}$")
print(displaymatch(valid.match("akt5q")))  # Valid.
# "<Match: 'akt5q', groups=()>"
print(displaymatch(valid.match("akt5e")))  # Invalid.
print(displaymatch(valid.match("akt")))  # Invalid.
print(displaymatch(valid.match("727ak")))  # Valid.
# "<Match: '727ak', groups=()>"

print("---------------------------------------")

# That last hand, "727ak", contained a pair, or two of the same valued cards.
# To match this with a regular expression, one could use backreferences as such:

pair = re.compile(r".*(.).*\1")
print(displaymatch(pair.match("717ak")))  # Pair of 7s.
# "<Match: '717', groups=('7',)>"
print(displaymatch(pair.match("718ak")))  # No pairs.
print(displaymatch(pair.match("354aa")))  # Pair of aces.
# "<Match: '354aa', groups=('a',)>"

print("---------------------------------------")

# To find out what card the pair consists of, one could use the group() method
# of the match object in the following manner:

pair = re.compile(r".*(.).*\1")
print(pair.match("717ak").group(1))  # '7'

# Error because re.match() returns None, which doesn't have a group() method:
try:
    pair.match("718ak").group(1)
    # Traceback (most recent call last):
    #   File "<pyshell#23>", line 1, in <module>
    #     re.match(r".*(.).*\1", "718ak").group(1)
    # AttributeError: 'NoneType' object has no attribute 'group'
except Exception as ex:
    print(ex)

print(pair.match("354aa").group(1))  # 'a'
