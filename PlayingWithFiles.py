f = open("new1.txt", "r")

#g = f.read()

# print(g)
# print(len(g))
for li in f.readlines():
    li = li.rstrip()
    if li.endswith("98}"):
        print(li)
