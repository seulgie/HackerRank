"""
Title     : Min and Max
Subdomain : Numpy
Domain    : Python
"""

import numpy

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr_np = numpy.array(arr)

print(numpy.max(numpy.min(arr_np, axis=1)))
