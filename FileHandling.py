# <_io.TextIOWrapper name='filedata.txt' mode='r' encoding='cp1252'>
file = open("filedata.txt", "r")
print(file)
print(file.read()) # show entire contents of txt file
file.close()

# read a single line at a time
#print(file.readline(), end="")
# only reads X characters
#print(file.readline(x), end="")

file1 = open("abc.txt", "w", newline='\n')
file1.write("something")
file1.write("more")
file1.close()

file1 = open("abc.txt", "a", newline='\n')
file1.write("forgot to add this")
file1.close()

# copy the contents from one file to another
inFile = open("filedata.txt", "r")
outFile = open("out.txt", "w")
for data in inFile:
    outFile.write(data)

# copy a binary file
inPic = open("hockey_simple.jpg", "rb")
outPic = open("out.jpg", "wb")
for data in inPic:
    outPic.write(data)

