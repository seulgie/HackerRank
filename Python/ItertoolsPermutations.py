"""
Title     : itertools.permutations()
Subdomain : Itertools
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/itertools-permutations/problem
"""

from itertools import permutations

s, k = map(str, input().split(" "))
s = sorted(s)

for e in list(permutations(s, int(k))):
    print(''.join(e))
