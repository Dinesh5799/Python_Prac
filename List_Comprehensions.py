x = int(input())
y = int(input())
z = int(input())
n = int(input())
res = []
for i in range(x+1):
    for j in range(y+1):
        l = list()
        for k in range(z+1):
            l = [i,j,k]
            res.append(l)
last_res = list()
for i in res:
    if not sum(i) == n:
        last_res.append(i)
print(last_res)