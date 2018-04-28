name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle.readlines():
    line = line.rstrip()
    if line.startswith('From'):
        line = line.split()
        if not len(line) > 2:
            continue
        d[line[1]] = d.get(line[1],0)+1

mx_word = None
mx_co = None
for kx,vx in d.items():
    if mx_co == None or vx > mx_co:
        mx_co = vx
        mx_word = kx

print(mx_word,mx_co)



