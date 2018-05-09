s = input().split()
r = int(s[0])
c = int(s[1])
#print('r = ',r,' c =',c)
r1 = r
ma = list()
while r1:
    s = input()
    du = list()
    for i in s:
        du.append(i)
    ma.append(du)
    r1 -= 1
#print(ma)
last = ""
l = list()
for j in range(c):
    for i in range(r):
        if ma[i][j].isalnum():
            l.append(ma[i][j])
        else:
            if  l[len(l)-1].isalnum() and not j == c-1:
                l.append('%')
        if j == c-1:
            last += (ma[i][j])
#print(last)
last = ''.join(reversed(last))
res_l = ""
for i in last:
    if i.isalnum():
        break
    else:
        res_l += i
res_l = ''.join(reversed(res_l))
#print(res_l)
res = ""
#print(l)
for i in l:
    if i.isalnum():
        res += i
    else:
        res += " "
res += res_l
print(res.rstrip())