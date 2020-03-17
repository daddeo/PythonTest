from math import sqrt

i = 1
while i <= 5:
    print("{}: ".format(i), end="")
    j = 4
    while j > -1:
        print("{}... ".format(j), end="")
        j -= 1
    i += 1
    print()

print("-----")
s = "TESTING"
for i in s:
    print(i)

print("-----")
for i in range(11, 21, 1):
    print(i)
print("-----")
for i in range(11, 21, 2):
    print(i)
print("-----")
for i in range(11, 21, 5):
    print(i)
print("-----")
for i in range(10, 0, -1):
    if i < 10:
        print(",", end="")
    print("{}".format(i), end="")
print()
print("-----")
for i in range(1, 20):
    if i % 3 != 0:
        if i > 1:
            print(",", end="")
        print("{}".format(i), end="")
print()
print("-----")
# do print odd numbers
for i in range(1, 10):
    if i % 2 != 0:
        pass
    else:
        if i > 2:
            print(",", end="")
        print("{}".format(i), end="")
print()
print("-----")
for i in range(1, 50):
    if i % 3 == 0 or i % 5 == 0:
        continue
    if i > 1:
        print(",", end="")
    print("{}".format(i), end="")
print()
print("-----")
# no hello 3
# continue will stop current iteration loop and continue to next iteration
for i in range(5):
    if i == 3:
        continue
    print("Hello ", i)
print("-----")
# no hello past hello 2
# break will stop the loop iteration immediately and perform no further loop iteration
for i in range(5):
    if i == 3:
        break
    print("Hello ", i)

# if you want to create a function, call it, but not implement it yet then 'pass' will be needed
# def func():
#    pass


# if a body code has no implementation then pass will be needed
x = 10
if x == 10:
    pass  # condition is known to exist, but implenentation might not be defined yet
else:
    print(x)

# ----------------------------------------------------------------------------------------------------
# printing patterns
#

# print a 4 x 4 grid of hashes
for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()  # needed to add the CRLF <newline>
print("-----")

# print a left facing triangle of hashes
for i in range(4):
    for j in range(i + 1):
        print("# ", end="")
    print()  # needed to add the CRLF <newline>
print("-----")

# print a upside down left facing triangle of hashes
for i in range(4):
    for j in range(4 - i):
        print("# ", end="")
    print()  # needed to add the CRLF <newline>
print("-----")

# ----------------------------------------------------------------------------------------------------
# For Else
#


def skipFive(numbers):
    for n in numbers:
        if n % 5 == 0:
            print(n)
            break
    else:
        print("not found")


numbers = [10, 16, 18, 21, 26]
skipFive(numbers)
numbers = [33, 16, 18, 21, 26]
skipFive(numbers)
print("-----")

# ----------------------------------------------------------------------------------------------------
# Finding a prime number
#


def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return "not prime"
    else:
        return "prime"


print("{} is {}".format(10, isPrime(10)))
print("{} is {}".format(31, isPrime(31)))
print("-----")


def isPrime2(number):
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return "not prime"
    else:
        return "prime"


print("{} is {}".format(10, isPrime(10)))
print("{} is {}".format(31, isPrime(31)))
print("-----")
