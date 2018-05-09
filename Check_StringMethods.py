s = input()
print(s.isalnum())
alp = False
dig = False
low = False
upp = False
for i in s:
    if i.isalpha():
        alp = True
        break
for i in s:
    if i.isnumeric():
        dig = True
        break
for i in s:
    if i.isnumeric():
        low = True
        break
for i in s:
    if i.isnumeric():
        upp = True
        break
print(alp)
print(dig)
print(low)
print(upp)




