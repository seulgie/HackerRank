"""
Title     : Zipped!
Subdomain : Built-Ins
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/zipped/problem
"""

num_students, num_subjects = map(int, input().split())

scores = []
for _ in range(num_subjects):
    scores.append(list(map(float, input().split())))

for e in zip(*scores):
    print(sum(e) / len(e))
