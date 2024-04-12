"""
Title     : Symmetric Difference
Subdomain : Sets
Domain    : Python
"""

m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

for e in sorted(a.union(b) - a.intersection(b)):
    print(e)
  
