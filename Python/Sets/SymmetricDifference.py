"""
Title     : Symmetric Difference
Subdomain : Sets
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/symmetric-difference/problem
"""

num_eng = int(input())
eng_sub = set(map(int, input().split()))

num_fr = int(input())
fr_sub = set(map(int, input().split()))

print(len(eng_sub.symmetric_difference(fr_sub)))
