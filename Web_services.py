import urllib.request,urllib.error,urllib.parse
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
#key=

while True:
    address = input('Enter Location: ')
    if len(address)<1:break
    url = serviceurl + urllib.parse.urlencode({'address':address})
    #url = url + "&key="
    print('Retrieving ',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved ',len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('------Failed to Retrieve------')
        print(data)
        continue
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat: ',lat,' lng: ',lng)
    location = js['results'][0]['formatted_address']
    print(location)

