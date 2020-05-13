def inner():
    print("We're inside")
    value = yield 2
    print("Received", value)
    return 4


def outer():
    yield 1
    retval = yield from inner()
    print("Returned", retval)
    yield 5


g = outer()
ret = next(g)
print(ret)
# 1
ret = next(g)  # Automatically enter the inner() generator
# We're inside
print(ret)
# 2
ret = g.send(3)
# Received 3
# Returned 4
print(ret)
# 5
