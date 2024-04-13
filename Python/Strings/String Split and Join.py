"""
Title     : String Split and Join
Subdomain : Strings
Domain    : Python
"""

def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
