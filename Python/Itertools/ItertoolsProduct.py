"""
Title     : itertools.product()
Subdomain : Itertools
Domain    : Python
"""

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*sorted(list(product(A, B))))
