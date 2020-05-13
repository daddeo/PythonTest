# https://docs.python.org/3/library/io.html
#
# Opening a file
# stream = open(file_name, mode, buffer_size)
# modes:
# r - read (default)
# w - truncate and write
# a - append if file exists
# x - write, fail if file exists
# + - updating (r/w)

# t - text (default)
# b - binary

import sys

# Open file demo.txt and read the contents
stream = open("input/filedata.txt", "rt")
# Is this readable? True
print("Is this readable? " + str(stream.readable()))
# Read one character : S
print("Read one character : " + stream.read(1))
# Read to end of line : ome useless text
print("Read to end of line : " + stream.readline())
# Read all lines to end of file :
# ['YouTube has too many videos\n', 'Programming is fun\n', 'Sales people suck\n', 'United States\n', 'Lenovo laptops rock\n',
# 'Gatorade is good, but too much sugar']
print("Read all lines to end of file :\n" + str(stream.readlines()))

# Open output.txt as a text file for writing
stream = open("output/names.txt", "wt")

# Can I write to this file? True
print("Can I write to this file? " + str(stream.writable()))

stream.write("H")  # Write a single string
# Write one or more strings w/o newlines unless specified
stream.writelines(["ello", " ", "world"])
stream.write("\n")  # Write a new line

names = ["Susan", "Christopher", "Jason"]
stream.writelines(names)

# Here"s a neat trick to insert a new line between items in the list
stream.write("\n")  # Write a new line
# adds a newline before each name, could be ',' if comma separated
stream.writelines("\n".join(names))
stream.close()  # Flush stream and close

stream = open("output/names.txt", "rt")
# Read all lines to end of file :
# ['Hello world\n', 'SusanChristopherJason\n', 'Susan\n', 'Christopher\n', 'Jason']
print("Read all lines to end of file :\n" + str(stream.readlines()))
stream.close()

# Open manage.txt file to write text
stream = open("output/manage.txt", "wt")

# Write the word demo to the file stream
stream.write("demo!")

# Move back to the start of the file stream
stream.seek(0)

# write the word cool to the file stream
stream.write("cool")

# Flush the file stream contents to the file buffer
# flushed data is written to the file and visible if opened by someone else,
# but committed to disk yet.
stream.flush()

# Flush the file stream and close the file
stream.close()

stream = open("output/manage.txt", "rt")
# Read all lines to end of file :
# ['cool!']
print("Read all lines to end of file :\n" + str(stream.readlines()))
stream.close()

# exception occurred --> [Errno 17] File exists: 'output/manage.txt'
try:
    stream = open("output/manage.txt", "xt")
    stream.write("text")
except Exception as ex:
    print(f"exception occurred --> {ex}")
finally:
    stream.close()

# exception occurred --> <class 'FileExistsError'>
try:
    stream = open("output/manage.txt", "xt")
    stream.write("text")
except:  # catch *all* exceptions
    ex = sys.exc_info()[0]
    value = sys.exc_info()[1]
    tb = sys.exc_info()[2]
    print(f"exception occurred --> {ex}, value: {value}\n{tb}")
finally:
    stream.close()

# the with version of use is designed to automatically close the stream for us
# same as:
# try:
#     stream = open("output/manage.txt", "xt")
#     stream.write("text")
# finally:
#     stream.close()
# can be used for any resource/object that has a requirement to close it when
# done using it.
with open("output/manage.txt", "wt") as stream:
    stream.write("Lorem Ipsum Dolar")
