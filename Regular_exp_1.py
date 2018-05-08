import re
s = input("Enter The Test Case: ")

r = '^[4,5,6]'

if re.search(r,s):
    print("Valid")
else:
    print("Invalid")
