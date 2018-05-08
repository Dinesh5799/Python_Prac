import re

s = input()

r = '.+\S@\S'

if re.search(r,s):
    print("Email Id is Valid")
else:
    print("Invalid Email Id")