# need to install numpy
# from command line: pip3 install numpy
# currently 1.18.1

# import numpy as np
# from .core import *
# from .numeric import *
# from numpy import array as np_array, transpose as np_transpose, \
#      linspace as np_linspace, zeros as np_zeros
# from numpy.random import uniform as random_uniform
from numpy import array, linspace, logspace, concatenate, arange
from numpy.core.umath import cos, log, sin

numbers = array([1, 2, 3, 4, 5, 6])
print(numbers)
numbers = array([1, 2, 3, 4, 5, 6], int)
print(numbers)
print(numbers.dtype)

# array will see 1 number is float and implicitly convert
numbers = array([1, 2, 3, 4, 5.0, 6])
print(numbers)
print(numbers.dtype)

# array can be told explicitly to convert the numbers to float
numbers = array([1, 2, 3, 4, 5, 6], float)
print(numbers)
print(numbers.dtype)

# -------------------------------------------------------------------------------------------------------------
# using linspace
#

# start at 0, go to 15, construct 16 numbers in the range
numbers = linspace(0, 15, 16)
# [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]
print(numbers)
# start at 0, go to 15, construct 16 numbers in the range
numbers = linspace(0, 15, 22)
# [ 0.          0.71428571  1.42857143  2.14285714  2.85714286  3.57142857
#   4.28571429  5.          5.71428571  6.42857143  7.14285714  7.85714286
#   8.57142857  9.28571429 10.         10.71428571 11.42857143 12.14285714
#  12.85714286 13.57142857 14.28571429 15.        ]
print(numbers)

# -------------------------------------------------------------------------------------------------------------
# using arange
#

numbers = arange(1, 15, 2)
print(numbers)  # [ 1  3  5  7  9 11 13]
numbers = arange(1, 50, 5)
print(numbers)  # [ 1  6 11 16 21 26 31 36 41 46]

# -------------------------------------------------------------------------------------------------------------
# using logspace
#

numbers = logspace(1, 40, 5)
# [1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30
#  1.00000000e+40]
print(numbers)
print("%.2g" % numbers[0])  # 10
print("%.2g" % numbers[1])  # 5.6e+10
print("%.3g" % numbers[2])  # 3.16e+20
print("%.4g" % numbers[3])  # 1.778e+30
print("%.5g" % numbers[4])  # 1e+40


# -------------------------------------------------------------------------------------------------------------

a1 = array([1, 2, 3, 4, 5])
a1 = a1 + 5
print(a1)  # [ 6  7  8  9 10]

a2 = array([6, 1, 9, 3, 2])

a3 = a1 + a2  # vectorized operation
print(a3)  # [12  8 17 12 12]

# min, max, sqrt, pow, sort, etc
print(sin(a1))  # [-0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
print(cos(a2))  # [ 0.96017029  0.54030231 -0.91113026 -0.9899925  -0.41614684]
print(log(a3))  # [2.48490665 2.07944154 2.83321334 2.48490665 2.48490665]

a4 = concatenate((a1, a2))
print(a4)  # [ 6  7  8  9 10  6  1  9  3  2]
