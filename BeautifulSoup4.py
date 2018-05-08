import urllib.parse,urllib.error,urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input("Enter url---")
url = "https://github.com/Dinesh5799/Python_Prac"
html = urllib.request.urlopen(url,context=ctx).read()
#print("html = ",html)
soup = BeautifulSoup(html,'html.parser')
#print("><><><><><><><><><><><><><><><><><><><><><",soup)
tags = soup('a')
#print(tags)
for tag in tags:
    print(tag.get('href',None))