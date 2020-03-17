"""
explicitely import numpy functions while avoiding pylint errors  
"""
# pylint: disable=unused-import
# pylint: disable=no-name-in-module
from numpy import array, transpose, zeros  # add all things you need
from numpy.random import uniform as random_uniform
# pylint: enable=no-name-in-module

