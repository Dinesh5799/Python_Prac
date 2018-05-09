import re

r = '[^<^</].+>'
s = '<HI>'
s1 = '<//HI>'

print("1st = ",re.findall(r,s))
print("2nd = ",re.findall(r,s1))