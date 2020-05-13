from xml.etree.ElementTree import parse

document = parse("./data/books.xml")

# <xml.etree.ElementTree.ElementTree object at 0x000001E8DD3F7C40>
print(document)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', '_root', '_setroot', 'find', 'findall', 'findtext', 'getiterator', 'getroot', 'iter', 'iterfind', 'parse',
# 'write', 'write_c14n']
print(dir(document))

# <Element 'book' at 0x000002332FE51C20>
# <Element 'book' at 0x000002332FE51EF0>
# <Element 'book' at 0x000002332FE551D0>
# <Element 'book' at 0x000002332FE55400>
# <Element 'book' at 0x000002332FE556D0>
# <Element 'book' at 0x000002332FE559A0>
# <Element 'book' at 0x000002332FE55C20>
# <Element 'book' at 0x000002332FE55E50>
# <Element 'book' at 0x000002332FE590E0>
# <Element 'book' at 0x000002332FE59360>
# <Element 'book' at 0x000002332FE59590>
# <Element 'book' at 0x000002332FE59860>
for item in document.iterfind("book"):
    print(item)

# Gambardella, Matthew
# Ralls, Kim
# Corets, Eva
# Corets, Eva
# Corets, Eva
# Randall, Cynthia
# Thurman, Paula
# Knorr, Stefan
# Kress, Peter
# O'Brien, Tim
# O'Brien, Tim
# Galos, Mike
for item in document.iterfind("book"):
    print(item.findtext("author"))

# XML Developer's Guide
# Midnight Rain
# Maeve Ascendant
# Oberon's Legacy
# The Sundered Grail
# Lover Birds
# Splish Splash
# Creepy Crawlies
# Paradox Lost
# Microsoft .NET: The Programming Bible
# MSXML3: A Comprehensive Guide
# Visual Studio 7: A Comprehensive Guide
for item in document.iterfind("book"):
    print(item.findtext("title"))

# 44.95
# 5.95
# 5.95
# 5.95
# 5.95
# 4.95
# 4.95
# 4.95
# 6.95
# 36.95
# 36.95
# 49.95
for item in document.iterfind("book"):
    print(item.findtext("price"))
