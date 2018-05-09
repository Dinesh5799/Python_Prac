import hashlib
n = int(input())

s = input().split()
t = tuple()
l = list()
for i in s:
    l.append(int(i))
t = tuple(l)
print(hash(t))