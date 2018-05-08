from bs4 import BeautifulSoup
import urllib.request,urllib.error,urllib.parse

url = "http://www.pythonforbeginners.com"

content = urllib.request.urlopen(url).read()

soup = BeautifulSoup(content)

print(soup.prettify())