fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()

for line in fh:
    if line.startswith('From'):
        liner = line.split()
        if len(liner) > 2:
        	count += 1
        	lst.append(liner[1])

for lx in lst:
    print(lx)
print("There were", count, "lines in the file with From as the first word")
