import re

#r = "href=\"(.+)\""
#s = "<p>Please click <a href=\"http://www.dr-chuck.com\">here</a></p>"
r = '[0-9]+'
s = "<span class=\"comments\">97</span>"
li = re.findall(r,s)
print(li)