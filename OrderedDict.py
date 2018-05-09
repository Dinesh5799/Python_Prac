from collections import OrderedDict

od = OrderedDict()
n = int(input())
for i in range(n):
    name = input()
    qt = input()
    try:
        if name in od:
            od[qt] += qt
        else:
            od[name] = name
            od[qt] = qt
    except Exception as e:
        print(e)
print(od)