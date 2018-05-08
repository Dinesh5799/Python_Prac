import re

r = '^[A-Z]+ <[a-z0-9]+@[a-z]+\.com>'

n = int(input())

while n:
    s = input()
    if re.search(r,s):
        print(s)
    n -= 1
