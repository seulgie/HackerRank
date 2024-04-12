"""
Title     : Detect Floating Point Number
Subdomain : Regex and Parsing
Domain    : Python
"""

import re

regex = re.compile(r'^[+-]?[0-9]*\.[0-9]+$')

for _ in range(int(input())):
    print(bool(regex.match(input())))
