"""
Title     : Dot and Cross
Subdomain : Numpy
Domain    : Python
"""

import numpy

n = int(input())

arr1 = []
arr2 = []

for _ in range(n):
    arr1.append(list(map(int, input().split())))
    
for _ in range(n, 2*n):
    arr2.append(list(map(int, input().split())))
    
print(numpy.dot(arr1, arr2))
