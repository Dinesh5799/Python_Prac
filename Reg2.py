import re

r = '[a-z0-9]'

y = re.findall(r,'09as')
print('y = ',y)

z = re.findall(r,'az09')
print('z = ',z)