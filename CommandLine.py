import sys

# could run from command line using argc/argv
print("argc: {}".format(len(sys.argv)))
print("argv: {}".format(sys.argv))

if len(sys.argv) < 2:
    print("please try again and enter two numbers to add together.")
else:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print("x + y: {}".format(x + y))
