"""
Title     : itertools.combinations()
Subdomain : Itertools
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/itertools-combinations/problem
"""

from itertools import combinations

s, k = input().split(" ")
s = sorted(s)

for i in range(1, int(k)+1):
    for e in combinations(s, int(i)):
        print("".join(e))
