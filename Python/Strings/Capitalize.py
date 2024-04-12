"""
Title     : Capitalize!
Subdomain : Strings
Domain    : Python
"""

def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))
