import urllib.request,urllib.error,urllib.parse
import json

url = input("Enter location: ")
print('Retrieving ',url)
hn = urllib.request.urlopen(url).read()
print('Retrieved ',len(hn),' characters')
hn = json.loads(hn)
#print('hn = ',hn)
sum = 0
co = 0
for i in hn['comments']:
    co += 1
    sum += i['count']
print('Count: ',co)
print('Sum: ',sum)