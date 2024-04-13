"""
Title     : Find the Runner-Up Score
Subdomain : Basic Data Types
Domain    : Python
"""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(sorted(set(arr), reverse=True)[1])
