def my_function(x):
    print(x)


my_function(10)  # 10
my_function.yolo = "you live only once"
print(my_function.yolo)  # you live only once

# -------------------------


def first_func(x):
    return x ** 2


def second_func(x):
    return x - 2


print(first_func(2))  # 4
print(second_func(2))  # 0

# -------------------------

try:
    # exception. first_func expects an int and gets a string
    print(first_func("2"))
except Exception as ex:
    print(ex.__repr__())
    pass

try:
    print(second_func(int("2")))  # 0
    print("no exception")
except Exception as ex:
    print(ex.__repr__())
    pass

# -------------------------


def convert_to_float(func):
    # define a function within the outer function
    def new_func(x):
        return func(float(x))

    # return the newly defined function
    return new_func


#
# convert_to_float returns this function:
# def new_func(x):
#     return first_func(float(x))
#
new_first_func = convert_to_float(first_func)
print(new_first_func("2"))  # 4.0
print(convert_to_float(second_func)("2"))  # 0.0

# -------------------------
# decorate syntax


@convert_to_float
def first_func(x):
    return x ** 2


# which is equivelant to:
# first_func = convert_to_numeric(first_func)

print(first_func("2"))  # 4.0
