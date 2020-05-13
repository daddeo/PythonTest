# Inheritance
# https://docs.python.org/3/tutorial/classes.html#inheritance
#
# creates an "is a" relationship
# Student is a person
# MySqlConnection is a DatabaseConnection
#
# Composition (with properties) creates a "has a" relationship
# Student has a class
# DatabaseConnection has a connection string
#
# In Python, all methods are virtual (can override or redefine their behavior)
# use the keyword {super} to access the parent class
# must always call the parent constructor
#
# all classes inherit from Object
# and all classes have access to those methods and can override them, such as __str__ and __repr__
#


class Teacher:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)

    # basically a toString
    def __str__(self):
        return self.name


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def sing_school_song(self):
        print("Ode to " + self.school)

    def say_hello(self):
        super().say_hello()
        print("I'm rather tired.")

    # basically a toString
    def __str__(self):
        # return super().__str__()
        return f"{self.name} attends {self.school}"


student = Student("Christopher", "Michigan Tech")
# Hello, Christopher
# I'm rather tired.
student.say_hello()
# Ode to UVM
student.sing_school_song()
# What are you?

# Is this an instance of student: True
print(f"Is this an instance of student: {isinstance(student, Student)}")
# Is this an instance of person: True
print(f"Is this an instance of person: {isinstance(student, Person)}")
# Is Student a subclass of Person: True
print(f"Is Student a subclass of Person: {issubclass(Student, Person)}")

# True
print(isinstance(student, Student))
# False
print(issubclass(Person, Student))
# True
print(isinstance(student, Person))
# True
print(issubclass(Student, Person))
# False
print(issubclass(Student, Teacher))
# False
print(isinstance(student, Teacher))

# without the __str__ override in Person this would print the address of student
# Christopher attends Michigan Tech
print(str(student))

person = Person("Christopher")
# Christopher
print(str(person))

teacher = Teacher("Jeff")
# <__main__.Teacher object at 0x0000021FBA4B44C0>
print(str(teacher))
