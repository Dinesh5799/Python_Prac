import xml.etree.ElementTree as ET
import urllib.request,urllib.parse,urllib.error
import re

url = input("Enter location: ")
# http://py4e-data.dr-chuck.net/comments_92296.xml
han = urllib.request.urlopen(url).read()
print("Retrieving ",url)
print("Retrieved ",len(han)," characters")
tree = ET.fromstring(han)
lst = tree.findall('.//count')
print("Count: ",len(lst))
sum = 0
for i in lst:
    sum += int(i.text)
print("Sum: ",sum)