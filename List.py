lis = []
n = int(input())
while n:
    s = input().split()
    #print("s = ",s)
    if len(s) == 3 :
        i = int(s[1])
        e = int(s[2])
        lis.insert(i,e)
    elif len(s) == 2:
        if s[0] == "remove":
            lis.remove(int(s[1]))
        elif s[0] == "append":
            lis.append(int(s[1]))
    elif len(s) == 1:
        if s[0] == "sort":
            lis.sort()
        elif s[0] == "print":
            print(lis)
        elif s[0] == "pop":
            lis.pop()
        elif s[0] == "reverse":
            lis.reverse()
    n -= 1
    #print("lis = ",lis)