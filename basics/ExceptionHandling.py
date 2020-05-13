
import traceback

a = 5
b = 2

# use b = 0 for divide by zero
# use input k = "p" for value error

try:
    print("resource open")
    print(a / b)
    k = int(input("Enter a number: "))
    print(k)
    print(a / k)
except ZeroDivisionError as e:
    print("exception", e)
except ValueError as e:
    print("Invalid input")
except Exception as e:  # catch all exception handler
    print("Something went wrong... ", e)
finally:
    print("resource closed")

try:
    print("resource open")
    print(a / b)
    k = int(input("Enter a number: "))
    print(k)
    print(a / k)
except ZeroDivisionError as e:
    print("exception", e)
except:
    print("Something went wrong... ")
finally:
    print("resource closed")


(x, y) = (5, 0)
try:
    z = x / y
except ZeroDivisionError:
    print("divide by zero")

(x, y) = (5, 0)
try:
    z = x / y
except ZeroDivisionError as e:
    z = e  # representation: "<exceptions.ZeroDivisionError instance at 0x817426c>"
# division by zero
print(z)


import sys

try:
    untrusted.execute()
except:  # catch *all* exceptions
    e = sys.exc_info()[0]
    # <class 'NameError'>
    print(e)

# try:
#   do_some_stuff()
# except:
#   rollback()
#   raise
# else:
#   commit()

# try:
#   do_some_stuff()
# finally:
#   cleanup_stuff()

# try:
#     a, b, c = d
# except Exception as e:
#     e.args += (d,)
#     raise

def process_exception(ex, value, tb):
    print("--------------------------------------")
    print(">>> print_tb:\n")
    traceback.print_tb(tb)
    print("--------------------------------------")
    print(">>> print_exception:\n")
    traceback.print_exception(ex, value, tb)0
    print("--------------------------------------")
    print(">>> print_list(extract_tb):\n")
    stack_summary = traceback.extract_tb(tb)
    print(stack_summary)
    traceback.print_list(stack_summary)
    print("--------------------------------------")
    print(">>> print_list(extract_stack):\n")
    traceback.print_list(traceback.extract_stack())

# --------------------------------------
# >>> print_exc:
# Traceback (most recent call last):
#   File "c:/dev/src/Python/PythonTest/basics/ExceptionHandling.py", line 119, in <module>
#     untrusted.execute()
# NameError: name 'untrusted' is not defined
# --------------------------------------
# >>> print_stack:
#   File "c:/dev/src/Python/PythonTest/basics/ExceptionHandling.py", line 129, in <module>
#     traceback.print_stack()
# --------------------------------------
# >>> print_tb:
#   File "c:/dev/src/Python/PythonTest/basics/ExceptionHandling.py", line 119, in <module>
#     untrusted.execute()
# --------------------------------------
# >>> print_exception:
# Traceback (most recent call last):
#   File "c:/dev/src/Python/PythonTest/basics/ExceptionHandling.py", line 119, in <module>
#     untrusted.execute()
# NameError: name 'untrusted' is not defined
# --------------------------------------
# >>> print_list(extract_tb):
# [<FrameSummary file c:/dev/src/Python/PythonTest/basics/ExceptionHandling.py, line 119 in <module>>]
#   File "c:/dev/src/Python/PythonTest/basics/ExceptionHandling.py", line 119, in <module>
#     untrusted.execute()
# --------------------------------------
# >>> print_list(extract_stack):
#   File "c:/dev/src/Python/PythonTest/basics/ExceptionHandling.py", line 134, in <module>
#     process_exception(ex, value, tb)
#   File "c:/dev/src/Python/PythonTest/basics/ExceptionHandling.py", line 96, in process_exception
#     traceback.print_list(traceback.extract_stack())
try:
    untrusted.execute()
except:  # catch *all* exceptions
    print("--------------------------------------")
    print(">>> print_exc:")
    traceback.print_exc()
    # print("--------------------------------------")
    # print("print_last:")
    # traceback.print_last()
    print("--------------------------------------")
    print(">>> print_stack:")
    traceback.print_stack()

    ex = sys.exc_info()[0]
    value = sys.exc_info()[1]
    tb = sys.exc_info()[2]
    process_exception(ex, value, tb)
finally:
    pass
