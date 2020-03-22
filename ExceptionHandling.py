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
