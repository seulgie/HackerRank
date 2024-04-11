"""
Title     : Concatenate
Subdomain : Numpy
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/np-concatenate/problem
"""

import numpy

n, m, p = map(int, input().split())

arr1 = []
arr2 = []
for _ in range(n):
    arr1.append(list(map(int, input().split())))
    
for _ in range(m):
    arr2.append(list(map(int, input().split())))
    
arr1_np = numpy.array(arr1)
arr2_np = numpy.array(arr2)

print(numpy.concatenate((arr1_np, arr2_np)))

