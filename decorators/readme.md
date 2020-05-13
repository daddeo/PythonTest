# Decorators

One can think of decorators as adjectives (add additional meaning) where Objects are nouns (data constructs) and Functions/Methods are verbs (actions). Used most commonly to add additional functionality to your code.

[Decorators](https://www.python.org/dev/peps/pep-0318/) are similar to attributes in that they add meaning or functionality to blocks of code in Python. They're frequently used in frameworks such as [Flask](http://flask.pocoo.org/) or [Django](https://www.djangoproject.com/). The most common interaction you'll have with decorators as a Python developer is through using them rather than creating them.

``` python
# Example decorator
@log(True)
def sample_function():
    print('this is a sample function')
```