import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen("https://www.coursera.org/learn/python-network-data").read()
soup = BeautifulSoup(fhand,'html.parser')
tags = soup('a')
print(tags)
for tag in tags:
    print(tag.get('href',None))


