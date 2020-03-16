import sys

# could run from command line using argc/argv
print("argc: {}".format(len(sys.argv)))
print("argv: {}".format(sys.argv))

x = int(sys.argv[1])
y = int(sys.argv[2])
print("x + y: {}".format(x + y))
