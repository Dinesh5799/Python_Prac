import xml.etree.ElementTree as ET

try:
    #tree = ET.parse('XmlFile.xml')
    #tree = ET.fromstring('XmlFile.xml')
    #print("Resultant = ", tree)
    #print("Title: ", tree.find('title').text)
    #print("Header 1: ", tree.find('h1').text)
    tree = ET.parse('XmlFile.xml')
    root = tree.getroot()
    print(root.tag)
except Exception as e:
    print("Error in Parsing = ",e)
