"""
Title     : Collections.deque()
Subdomain : Collections
Domain    : Python
"""

from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    cmd, *val = map(str, input().split())
    if cmd == "append":
        d.append(int(*val))
    elif cmd == "appendleft":
        d.appendleft(int(*val))
    elif cmd == "pop":
        d.pop()
    elif cmd == "popleft":
        d.popleft()

        
for i in d:
    print(i, end=" ")
