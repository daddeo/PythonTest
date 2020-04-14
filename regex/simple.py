import re

# https://docs.python.org/3/library/re.html


def print_match(header, pattern, search_text):
    print("---------- ({})".format(header))
    for match in re.finditer(pattern, search_text):
        # Start index of match (integer)
        sStart = match.start()

        # Final index of match (integer)
        sEnd = match.end()

        # Complete match (string)
        sGroup = match.group()

        # Print match
        print('Match "{}" found at: [{},{}]'.format(sGroup, sStart, sEnd))


# identifier:   \d = any number (a digit)
# modifiers:    \d represents a digit. ex: \d{1,3} will look for 1 to 3 digits
pattern = re.compile(r"\d{1,3}")
print_match("find all digits between 1 and 3", pattern, r"924861639880")

pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
print_match("phone number", pattern, r"924-861-6398")

pattern = re.compile(r"((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}")
print_match("phone number 2", pattern, r"(123) 456-7890")


text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

# pattern = re.compile(r"abc", flags=re.IGNORECASE)
pattern = re.compile(r"abc")
print_match("abc", pattern, text_to_search)
# matches = pattern.search(text_to_search)
# for (letters,numbers) in re.findall(pattern, text_to_search):
#     print(m.group(2), "*", m.group(1))
# for m in re.finditer(pattern, text_to_search):
#     print(m.group(2), "*", m.group(1))
# print(matches)

pattern = re.compile(r"bca", re.I)
print_match("bca", pattern, text_to_search)
# matches = pattern.search(text_to_search)
# print(matches)

# escape the MetaCharacters
pattern = re.compile(r"\\")
print_match("backslash", pattern, text_to_search)
# matches = pattern.search(text_to_search)
# print(matches)

# \d - match any digit
pattern = re.compile(r"\d", re.I)
print_match("any digits", pattern, text_to_search)
# matches = pattern.search(text_to_search)
# print(matches)

# \D - match any non-digit
pattern = re.compile(r"\D", re.I)
print_match("any non-digits", pattern, text_to_search)
# matches = pattern.search(text_to_search)
# print(matches)

# \w - match any word character
pattern = re.compile(r"\w", re.I)
print_match("any word character", pattern, text_to_search)
# matches = pattern.search(text_to_search)
# print(matches)

# \W - match any non-word character
pattern = re.compile(r"\W", re.I)
print_match("non-word character", pattern, text_to_search)
# matches = pattern.search(text_to_search)
# print(matches)

# \s - match any whitespace
pattern = re.compile(r"\s", re.I)
print_match("any whitespace", pattern, text_to_search)
# matches = pattern.search(text_to_search)
# print(matches)

# \S - match any non-whitespace
pattern = re.compile(r"\S", re.I)
print_match("non-whitespace", pattern, text_to_search)
# matches = pattern.search(text_to_search)
# print(matches)

# anchors don't match character, but rather match invisible positions
# before and after characters (e.g. \b, \B, ^, $)
pattern = re.compile(r"\bHa", re.I)
print_match("Ha 1", pattern, text_to_search)
# matches = pattern.search(text_to_search)
# print(matches)
pattern = re.compile(r"\BHa", re.I)
matches = pattern.search(text_to_search)
print(matches)
pattern = re.compile(r"\bHa\b", re.I)
matches = pattern.search(text_to_search)
print(matches)
pattern = re.compile(r"^Ha", re.I)
matches = pattern.search(text_to_search)
print(matches)
pattern = re.compile(r"Ha$", re.I)
matches = pattern.search(text_to_search)
print(matches)

# match some phone numbers
pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d", re.I)
matches = pattern.search(text_to_search)
print(matches)


# escape the MetaCharacters
pattern = re.compile(r"coreyms\.com", re.I)
matches = pattern.search(text_to_search)
print(matches)


sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r"start", re.I)
matches = pattern.search(sentence)
print(matches)
