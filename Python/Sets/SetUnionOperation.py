"""
Title     : Set .union() Operation
Subdomain : Sets
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/py-set-union/problem
"""

num_eng = int(input())
eng_sub = set(map(int, input().split()))

num_fr = int(input())
fr_sub = set(map(int, input().split()))

print(len(eng_sub.union(fr_sub)))
