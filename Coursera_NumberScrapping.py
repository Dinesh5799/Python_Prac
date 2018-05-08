import urllib.parse,urllib.request,urllib.error
from bs4 import BeautifulSoup

#url = "http://py4e-data.dr-chuck.net/comments_42.html"
url = "http://py4e-data.dr-chuck.net/comments_92294.html"
han = urllib.request.urlopen(url).read()
#print(han)
soupObj = BeautifulSoup(han,'html.parser')
#print(soupObj)
spanTags = soupObj('span')
#print(spanTags)

li = ""
reslist = list()
for tag in spanTags:
    #print("tag = ",tag)
    li = tag.text
    #print("li = ",li)
    if not li == "":
        reslist.append(li)
#print(reslist)
ressum = 0
for nu in reslist:
    ressum += int(nu)
print(ressum)