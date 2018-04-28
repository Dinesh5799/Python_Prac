name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


ti = list()
tli = list()
for lx in handle:
    lx = lx.rstrip()
    if lx.startswith('From'):
        lx = lx.split()
        if len(lx) > 2:
            ti = lx[5]
            ti = ti.split(':')
            #print(ti)
            tli.append(ti[0])
#print(tli)
res = dict()
for i in tli:
    #if i in res:
        #print("Already",i)
    res[i] = res.get(i,0)+1
    #else:
        #print("New",i)
        #res[i] = 1
#print(res)
re = list()
re = res.items()
re = sorted(re)
for i in re:
    print(i[0],i[1])
    #print('{num:02d}'.format(num=int(i[0]))," ",int(i[1]))