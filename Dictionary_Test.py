from collections import OrderedDict
#Using Ordered Dictionary
d = OrderedDict()
n = int(input())
while n:
    s = input().split()
    if len(s) > 2:
        key = s[0]+" "+s[1]
        value = s[2]
    else:
        key = s[0]
        value = s[1]
    if not key in d:
        d[key] = int(value)
    else:
        d[key] += int(value)
    n -= 1
for k,v in d.items():
    print(k,v)
