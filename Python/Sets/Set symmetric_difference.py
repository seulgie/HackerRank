"""
Title     : Set .symmetric_difference() Operation
Subdomain : Sets
Domain    : Python
"""

num_eng = int(input())
eng_sub = set(map(int, input().split()))

num_fr = int(input())
fr_sub = set(map(int, input().split()))

print(len(eng_sub.symmetric_difference(fr_sub)))
