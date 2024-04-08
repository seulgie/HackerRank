"""
Title     : Text Wrap
Subdomain : Strings
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/text-wrap/problem
"""

import textwrap

def wrap(string, max_width):
    result = textwrap.wrap(string, width=max_width)
    return '\n'.join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
