def gen2():
    yield "Hello"
    return "World"


g2 = gen2()
str = next(g2)  # Advance the generator
print(str)  # Hello
# str = next(g2)  # Advance again
# print(str)  # World


try:
    result = next(g2)
except StopIteration as exc:
    result = exc.args[0]
print(result)  # World
