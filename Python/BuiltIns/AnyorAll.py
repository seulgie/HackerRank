"""
Title     : Any or All
Subdomain : Built-Ins
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
"""

n = input()
lst = input().split()
print(all(int(i) > 0 for i in lst) and any((i == i[::-1]) for i in lst))
