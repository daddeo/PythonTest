def gen():
    print("First number")
    a = yield
    print("Second number")
    b = yield
    print("Addition result:", a + b)
    c = yield


g = gen()
next(g)  # Advance the generator to first yield
# First number
g.send(5)
# Second number
g.send(5)
# Addition result: 10
g.throw(OSError())
