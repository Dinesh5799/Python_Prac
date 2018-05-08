import urllib.parse,urllib.error,urllib.request
from bs4 import BeautifulSoup

tag = []
def urlFetcher(url):
    han = urllib.request.urlopen(url).read()
    soupObj = BeautifulSoup(han, 'html.parser')
    temptag = soupObj('a')
    # print("Tag in here",tag)
    return temptag



#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
#han = urllib.request.urlopen(url).read()
tag = urlFetcher("http://py4e-data.dr-chuck.net/known_by_Raman.html")
#print(tag)
co = int(input('Enter count: '))
po = int(input('Enter position: '))
for i in range(co-1):
    #print("tag[po] = ",tag[po-1])
    tempurl = tag[po-1]['href']
    #print(tempurl)
    tag = urlFetcher(tempurl)
print(tag[po-1].string)

