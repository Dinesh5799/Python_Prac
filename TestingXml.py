import xml.etree.ElementTree as ET

data = '''
<html>
    <head>Hello</head>
    <h1>Dinesh</h1>
</html>'''

tree=ET.fromstring(data)

print(tree.find('head').text)