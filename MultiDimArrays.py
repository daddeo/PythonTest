# need to install numpy
# from command line: pip3 install numpy
# currently 1.18.1

from numpy import *

numbers = array([1,2,3,4,5,6])
print(numbers)
numbers = array([1,2,3,4,5,6],int)
print(numbers)
print(numbers.dtype)

# array will see 1 number is float and implicitly convert
numbers = array([1,2,3,4,5.0,6])
print(numbers)
print(numbers.dtype)

# array can be told explicitly to convert the numbers to float
numbers = array([1,2,3,4,5,6],float)
print(numbers)
print(numbers.dtype)

# -------------------------------------------------------------------------------------------------------------
# using linspace
#

numbers = linspace(0, 15, 16) # start at 0, go to 15, construct 16 numbers in the range
# [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]
print(numbers)
numbers = linspace(0, 15, 22) # start at 0, go to 15, construct 16 numbers in the range
# [ 0.          0.71428571  1.42857143  2.14285714  2.85714286  3.57142857
#   4.28571429  5.          5.71428571  6.42857143  7.14285714  7.85714286
#   8.57142857  9.28571429 10.         10.71428571 11.42857143 12.14285714
#  12.85714286 13.57142857 14.28571429 15.        ]
print(numbers)

# -------------------------------------------------------------------------------------------------------------
# using arange
#

numbers = arange(1,15,2)
print(numbers) # [ 1  3  5  7  9 11 13]
numbers = arange(1,50,5)
print(numbers) # [ 1  6 11 16 21 26 31 36 41 46]

# -------------------------------------------------------------------------------------------------------------
# using logspace
#

numbers = logspace(1,40,5)
# [1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30
#  1.00000000e+40]
print(numbers)
print("%.2g" % numbers[0]) # 10
print("%.2g" % numbers[1]) # 5.6e+10
print("%.3g" % numbers[2]) # 3.16e+20
print("%.4g" % numbers[3]) # 1.778e+30
print("%.5g" % numbers[4]) # 1e+40



