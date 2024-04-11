"""
Title     : Collections.OrderedDict()
Subdomain : Collections
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
"""

from collections import OrderedDict

num_items = int(input())
od = OrderedDict()

for _ in range(num_items):
    transaction = (input().split())
    item = " ".join(transaction[:-1])
    price = int(transaction[-1])
    
    if od.get(item):
        od[item] += price
    else:
        od[item] = price
        
for k in od.keys():
    print(k, od[k])
