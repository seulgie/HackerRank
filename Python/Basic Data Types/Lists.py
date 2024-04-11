"""
Title     : Lists
Subdomain : Data Types
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/python-lists/problem
"""

if __name__ == "__main__":
    N = int(input())
    ans = []

    for _ in range(N):
        commands = input().strip().split(" ")
        cmd = commands[0]

        if cmd == "insert":
            pos = int(commands[1])
            val = int(commands[2])
            ans.insert(pos, val)

        elif cmd == "print":
            print(ans)

        elif cmd == "remove":
            ans.remove(int(commands[1]))

        elif cmd == "append":
            ans.append(int(commands[1]))

        elif cmd == "sort":
            ans.sort()

        elif cmd == "pop":
            ans.pop()

        elif cmd == "reverse":
            ans.reverse()
