import re

r = '^[A-Z]+ <[a-z0-9]+@[a-z]+.com>'

s = input()

if re.findall(r,s):
    print("Pattern Matches")
else:
    print('Ooops!!!')