# Docstring is the standard for documenting a module, function, class or method definition
# https://www.python.org/dev/peps/pep-0257/

# type hinting: name is a str and print_hello return a str
def print_hello(name: str) -> str:
    """
    Greets the user by name

    Parameters:\n
    \tname (str): the name of the user\n
    
    Returns:\n
    \tstr: the greeting
	"""
    print("Hello, " + name)


print_hello("User")
