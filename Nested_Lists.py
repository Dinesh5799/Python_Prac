n = int(input())

d = dict()
while n:
    k = input()
    v = float(input())
    if v in d:
        d[v].append(k)
    else :
        d[v] = [k]
    n -= 1

d = sorted(d.items())
h = d[1][1]
h.sort()
for i in h:
    print(i)