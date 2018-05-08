import urllib.request,urllib.parse,urllib.error

fhand = urllib.request.urlopen("https://www.coursera.org/learn/python-network-data")

li = list()
for l in fhand:
     l = l.decode().strip()
     k = int(l.find('href="'))
     str = ""
     if not k == -1:
         k += 6
         #print(l)
         for i in range(len(l)):
             if l[i+k] == "\"":
                 break
             else:
                 str += l[i+k]
     if not str == "":
         li.append(str)
#print(li)
fin = list()
for re in li:
    if re.startswith("http"):
        fin.append(re)
print(fin)