"""
Title     : Nested Lists
Subdomain : Data Types
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/nested-list/problem
"""

dic = dict()

if __name__ == "__main__":
    for _ in range(int(input())):
        name = input()
        score = float(input())

        if dic.get(score):
            dic[score] += " " + name
        else:
            dic[score] = name

    second = sorted(dic.items())[1][1]
    sorted_s = sorted(second.split(" "))

    print(*sorted_s, sep="\n")
