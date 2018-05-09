d = dict()
n = int(input())
while n:
    lx = []
    k = None
    s = input().split()
    for i in range(len(s)):
        if i==0:
            k = s[i]
        else :
            #print('k = ',k)
            if k in d:
                d[k].append(float(s[i]))
            else :
                d[k] = [float(s[i])]
    n -= 1

s = input()
#print('s = ',s)
print("{:0.2f}".format(sum(d[s])/len(d[s])))
