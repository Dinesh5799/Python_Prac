import re

f = open("regex_sum_92292.txt",'r')

r = '[0-9]+'
res = list()
for lx in f:
    lx = lx.rstrip()
    st = re.findall(r,lx)
    #print(st)
    for i in st:
        res.append(int(i))

print(sum(res))