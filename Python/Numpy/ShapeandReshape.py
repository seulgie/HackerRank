"""
Title     : Shape and Reshape
Subdomain : Numpy
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/np-shape-reshape/problem
"""

import numpy

arr = list(map(int, input().split()))
print(numpy.reshape(arr, (3,3)))
