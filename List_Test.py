n = int(input())
nl = list()
s = input().split()
for lx in s:
    lx = int(lx)
    if not lx in nl:
        nl.append(lx)
nl.sort()
#print(nl)
print(nl[len(nl)-2])
