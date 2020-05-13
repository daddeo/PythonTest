import types
from inspect import getmembers, isfunction

# from my_project import my_module
import PIL
from PIL import Image

functions_list = [o for o in getmembers(Image) if isfunction(o[1])]
# functions_list = [o for o in getmembers(my_module, isfunction)]
# functions_list = getmembers(my_module, predicate)
# functions_list = getmembers(PIL, isfunction)
for func in functions_list:
    print(func)
print("----------------------------------------------------------------------------")
# To find if the function is defined in that module (rather than imported)
# NOTE: it won't work necessarily if the imported function comes from a module with the same name as this module.
# if isfunction(o[1]) and o[1].__module__ == my_module.__name__


def print_module_functions(module):
    print(
        "\n".join(
            [
                str(module.__dict__.get(a).__name__)
                for a in dir(module)
                if isinstance(module.__dict__.get(a), types.FunctionType)
            ]
        )
    )


# print([getattr(yourmodule, a)
# for a in dir(yourmodule):
#     if isinstance(getattr(yourmodule, a), types.FunctionType)])
# print([
#     getattr(PIL, a) for a in dir(PIL)
#     if isinstance(getattr(PIL, a), types.FunctionType)
# ])
print_module_functions(PIL)

print("----------------------------------------------------------------------------")

print_module_functions(Image)
# print([
#     getattr(Image, a) for a in dir(Image)
#     if isinstance(getattr(Image, a), types.FunctionType)
# ])

print("----------------------------------------------------------------------------")

try:
    print("__all__ PIL:")
    print(PIL.__all__)
except:
    pass

print("----------------------------------------------------------------------------")

try:
    print("__all__ Image:")
    print(Image.__all__)
except:
    pass
