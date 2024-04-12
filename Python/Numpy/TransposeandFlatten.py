"""
Title     : Transpose and Flatten
Subdomain : Numpy
Domain    : Python
"""

import numpy

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
arr_np = numpy.array(arr)

print(numpy.transpose(arr_np))
print(arr_np.flatten())
