"""
Title     : Set .intersection() Operation
Subdomain : Sets
Domain    : Python
"""

num_en = int(input())
en = set(map(int, input().split()))
num_fr = int(input())
fr = set(map(int, input().split()))

print(len(en.intersection(fr)))
