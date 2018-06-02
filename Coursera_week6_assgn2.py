import urllib.parse,urllib.error,urllib.request
import json

serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
address = input('Enter location: ')
if len(address) > 1:
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving: ',url)
    han = urllib.request.urlopen(url)
    data =han.read().decode()
    print('Retrieved ', len(data), ' characters')
    #print(data)
    data = json.loads(data)
    print(data['results'][0]['place_id'])#data['results'][0]['geometry']