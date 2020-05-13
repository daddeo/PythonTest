"""

src:
https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc

By defining a function that contains the yield keyword, the function is marked as a generator. We then run the generator in the following order:

1. Initialize the generator and put it in g. At this point, we have a new generator object that didn’t run yet.
2. Advance the generator by calling next() on it. This causes the generator to advance to the first yield keyword, printing “Hello” on the way.
3. Advance the generator again. It prints “Goodbye”, and since it reached the end of the function, it raises a StopIteration exception and finishes.

https://docs.python.org/3/library/inspect.html#types-and-members

"""


def gen(num):
    num += 1
    yield num
    num += 1
    yield num


g = gen(1)
num = next(g)
print(num)
num = next(g)
print(num)
