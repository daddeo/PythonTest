# accessibilty in Python
# EVERYTHING is public and accessible
#
# Conventions for suggesting accessibility (both mean use at your own risk, could change):
# _ means avoid unless you really know what you're doing
# __ means do not use
#

# uses Pascal casing (each word has a capital letter, e.g. MilkTheCow)
class Presenter:
    """
    Presenter class
    """

    def __init__(self, name):
        super().__init__()
        self.name = name

    def say_hello(self):
        print("Hello " + self.__name)

    @property
    def name(self):
        return self.__name

    # @{name} should match the @property function {name}
    # e.g. if @property was
    # def fullname
    # then
    # @fullname.setter
    # would be needed
    # moreover this means that we have self.fullname, not self.name
    # and all references to self.__name would need to be self.__fullname
    @name.setter
    def name(self, name):
        # insert custom validation if needed
        self.__name = name


presenter = Presenter("Jeff")
presenter.say_hello()
# uses @property (name)
presenter.name = "Howie"
presenter.say_hello()
# uses @name.setter (name)
print("name: " + presenter.name)
