import re
line = "From: Dinesh Kumar"
if re.search('^From:',line):
    print("Found")

greedy = "From: Dinesh Kumar CEO: Wayne Enterprise"
y = re.findall('^F.+:',greedy)
print(y)
x = re.findall('^F.+?:',greedy)
print(x)

